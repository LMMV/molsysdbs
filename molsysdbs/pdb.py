"""Protein Data Bank (PDB) helpers."""

from __future__ import annotations

from pathlib import Path
from typing import Union

from ._http import download_url
from .errors import ValidationError


def validate_pdb_id(pdb_id: str) -> str:
    """Validate and normalize a PDB identifier.

    Args:
        pdb_id: PDB identifier (4 alphanumeric characters).

    Returns:
        Normalized PDB ID in uppercase.
    """
    if pdb_id is None:
        raise ValidationError("pdb_id is required")

    normalized = pdb_id.strip().upper()
    if len(normalized) != 4 or not normalized.isalnum():
        raise ValidationError(
            "pdb_id must be 4 alphanumeric characters, e.g. '1CRN'"
        )

    return normalized


def download_mmcif(
    pdb_id: str,
    out_dir: Union[str, Path] = ".",
    *,
    overwrite: bool = False,
) -> Path:
    """Download a PDB entry in mmCIF format.

    Args:
        pdb_id: PDB identifier.
        out_dir: Output directory for the downloaded file.
        overwrite: Whether to overwrite an existing file.

    Returns:
        Path to the downloaded mmCIF file.
    """
    normalized = validate_pdb_id(pdb_id)
    url = f"https://files.rcsb.org/download/{normalized}.cif"
    out_path = Path(out_dir) / f"{normalized}.cif"
    return download_url(url, out_path, overwrite=overwrite)
