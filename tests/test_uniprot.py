import io

import molsysdbs
from molsysdbs.errors import ValidationError


def test_validate_uniprot_id_normalizes():
    assert molsysdbs.validate_uniprot_id(" p69905 ") == "P69905"


def test_validate_uniprot_id_rejects_invalid():
    try:
        molsysdbs.validate_uniprot_id("abc")
    except ValidationError:
        assert True
    else:
        assert False, "Expected ValidationError"


def test_download_uniprot_json_builds_path_and_url(monkeypatch, tmp_path):
    captured = {}

    class DummyResponse:
        def __init__(self, data: bytes):
            self._bio = io.BytesIO(data)

        def read(self, n: int = -1) -> bytes:
            return self._bio.read(n)

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

    def fake_urlopen(url, timeout=30):
        captured["url"] = url
        captured["timeout"] = timeout
        return DummyResponse(b"{}")

    monkeypatch.setattr("molsysdbs._http.urlopen", fake_urlopen)

    out_path = molsysdbs.download_uniprot_json("P69905", tmp_path)
    assert out_path.name == "P69905.json"
    assert out_path.read_bytes() == b"{}"
    assert captured["url"] == "https://rest.uniprot.org/uniprotkb/P69905.json"
