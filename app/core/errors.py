"""Custom exception classes and error handlers."""

from fastapi import Request
from fastapi.responses import JSONResponse


class ApiError(Exception):
    """Base API error class."""

    status_code: int = 500
    error_code: str = "INTERNAL_SERVER_ERROR"

    def __init__(self, message: str) -> None:
        """Initialize API error."""
        self.message = message
        super().__init__(self.message)


class UserAlreadyExists(ApiError):
    """Exception raised when user already exists."""

    status_code = 409
    error_code = "USER_ALREADY_EXISTS"

    def __init__(self, message: str) -> None:
        """Initialize UserAlreadyExists error."""
        super().__init__(message)


class AuthenticationError(ApiError):
    """Exception raised for authentication failures."""

    status_code = 401
    error_code = "UNAUTHORIZED"

    def __init__(self, message: str) -> None:
        """Initialize AuthenticationError."""
        super().__init__(message)


class NotFoundError(ApiError):
    """Exception raised when resource is not found."""

    status_code = 404
    error_code = "NOT_FOUND"

    def __init__(self, message: str) -> None:
        """Initialize NotFoundError."""
        super().__init__(message)


async def api_error_handler(
    request: Request,
    exc: ApiError
) -> JSONResponse:
    """Handle API errors."""
    payload = {
        "error": exc.error_code,
        "message": exc.message
    }
    return JSONResponse(status_code=exc.status_code, content=payload)


async def generic_exception_handler(
    request: Request,
    exc: Exception
) -> JSONResponse:
    """Handle generic exceptions."""
    payload = {
        "error": "INTERNAL_SERVER_ERROR",
        "message": "Internal server error"
    }
    return JSONResponse(status_code=500, content=payload)
