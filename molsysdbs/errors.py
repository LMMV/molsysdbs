"""Custom exceptions for molsysdbs."""


class MolSysDBSError(Exception):
    """Base exception for molsysdbs."""


class ValidationError(MolSysDBSError):
    """Raised when input validation fails."""


class DownloadError(MolSysDBSError):
    """Raised when a remote resource cannot be downloaded."""
