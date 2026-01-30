"""Public interface for molsysdbs."""

from .errors import DownloadError, MolSysDBSError, ValidationError
from .pdb import download_mmcif, validate_pdb_id
from .uniprot import download_uniprot_json, validate_uniprot_id

__all__ = [
    "DownloadError",
    "MolSysDBSError",
    "ValidationError",
    "download_mmcif",
    "download_uniprot_json",
    "validate_pdb_id",
    "validate_uniprot_id",
]

__version__ = "0.1.0"
