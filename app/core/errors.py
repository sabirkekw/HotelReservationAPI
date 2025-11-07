from fastapi import Request
from fastapi.responses import JSONResponse


class ApiError(Exception):
    status_code: int = 500
    error_code: str = "INTERNAL_SERVER_ERROR"

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class UserAlreadyExists(ApiError):
    status_code = 409
    error_code = "USER_ALREADY_EXISTS"

    def __init__(self, message):
        super().__init__(message)


class AuthenticationError(ApiError):
    status_code = 401
    error_code = "UNAUTHORIZED"

    def __init__(self, message):
        super().__init__(message)


class NotFoundError(ApiError):
    status_code = 404
    error_code = "NOT_FOUND"

    def __init__(self, message):
        super().__init__(message)


async def api_error_handler(request: Request, exc: ApiError):
    payload = {"error": exc.error_code, "message": exc.message}
    return JSONResponse(status_code=exc.status_code, content=payload)


async def generic_exception_handler(request: Request, exc: Exception):
    payload = {"error": "INTERNAL_SERVER_ERROR", "message": "Internal server error"}
    return JSONResponse(status_code=500, content=payload)
