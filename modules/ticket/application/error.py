from dataclasses import dataclass
from enum import StrEnum


class ErrorCode(StrEnum):
    VALIDATION_ERROR = "VALIDATION_ERROR"


@dataclass(frozen=True)
class Error:
    code: ErrorCode
    message: str
    details: dict[str, str] | None = None

    @classmethod
    def validation_error(cls, message: str) -> "Error":
        return cls(ErrorCode.VALIDATION_ERROR, message)
