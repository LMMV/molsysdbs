"""HTTP helpers for molsysdbs."""

from __future__ import annotations

from pathlib import Path
from typing import Union
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from .errors import DownloadError


def download_url(
    url: str,
    out_path: Union[str, Path],
    *,
    overwrite: bool = False,
    timeout: int = 30,
    chunk_size: int = 64 * 1024,
) -> Path:
    """Download a URL to a local file.

    Args:
        url: Remote URL to download.
        out_path: Destination file path.
        overwrite: Whether to overwrite an existing file.
        timeout: Timeout in seconds for the request.
        chunk_size: Size of read chunks in bytes.

    Returns:
        Path to the downloaded file.
    """
    out_path = Path(out_path)
    if out_path.exists() and not overwrite:
        raise DownloadError(f"File already exists: {out_path}")

    out_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with urlopen(url, timeout=timeout) as response, out_path.open("wb") as fh:
            while True:
                chunk = response.read(chunk_size)
                if not chunk:
                    break
                fh.write(chunk)
    except (HTTPError, URLError, OSError) as exc:
        raise DownloadError(f"Failed to download {url}: {exc}") from exc

    return out_path
