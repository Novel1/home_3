from fastapi.exceptions import HTTPException
from typing_extensions import Annotated, Doc
from typing import Any, Dict, Optional
from starlette import status

class BaseHTTPException(HTTPException):
    pass

class HTTPBadRequestException(BaseException):
    def __init__(
        self, status_code: int, detail: Any = None, headers: Dict[str, str] | None = None
        ) -> None:
            super().__init__(status.HTTP_400_BAD_REQUEST, detail, headers)


class HTTPNotFoundException(BaseHTTPException):
    def __init__(
        self, status_code: int, detail: Any = None, headers: Dict[str, str] | None = None
        ) -> None:
            super().__init__(status.HTTP_404_NOT_FOUND, detail, headers)

