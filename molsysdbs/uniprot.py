"""UniProt helpers."""

from __future__ import annotations

from pathlib import Path
from typing import Union

from ._http import download_url
from .errors import ValidationError


def validate_uniprot_id(uniprot_id: str) -> str:
    """Validate and normalize a UniProt accession.

    Args:
        uniprot_id: UniProt accession identifier.

    Returns:
        Normalized UniProt ID in uppercase.
    """
    if uniprot_id is None:
        raise ValidationError("uniprot_id is required")

    normalized = uniprot_id.strip().upper()
    if not normalized.isalnum() or len(normalized) not in (6, 10):
        raise ValidationError(
            "uniprot_id must be 6 or 10 alphanumeric characters, e.g. 'P69905'"
        )

    return normalized


def download_uniprot_json(
    uniprot_id: str,
    out_dir: Union[str, Path] = ".",
    *,
    overwrite: bool = False,
) -> Path:
    """Download a UniProt entry as JSON.

    Args:
        uniprot_id: UniProt accession identifier.
        out_dir: Output directory for the downloaded file.
        overwrite: Whether to overwrite an existing file.

    Returns:
        Path to the downloaded JSON file.
    """
    normalized = validate_uniprot_id(uniprot_id)
    url = f"https://rest.uniprot.org/uniprotkb/{normalized}.json"
    out_path = Path(out_dir) / f"{normalized}.json"
    return download_url(url, out_path, overwrite=overwrite)
