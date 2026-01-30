import io

import molsysdbs
from molsysdbs.errors import ValidationError


def test_validate_pdb_id_normalizes():
    assert molsysdbs.validate_pdb_id(" 1crn ") == "1CRN"


def test_validate_pdb_id_rejects_invalid():
    try:
        molsysdbs.validate_pdb_id("12")
    except ValidationError:
        assert True
    else:
        assert False, "Expected ValidationError"


def test_download_mmcif_builds_path_and_url(monkeypatch, tmp_path):
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
        return DummyResponse(b"data")

    monkeypatch.setattr("molsysdbs._http.urlopen", fake_urlopen)

    out_path = molsysdbs.download_mmcif("1crn", tmp_path)
    assert out_path.name == "1CRN.cif"
    assert out_path.read_bytes() == b"data"
    assert captured["url"] == "https://files.rcsb.org/download/1CRN.cif"
