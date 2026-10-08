from dataclasses import dataclass
from typing import Generic, TypeVar, cast

T = TypeVar("T")


@dataclass(frozen=True)
class ErrorViewModel:
    message: str
    code: str | None = None


@dataclass(frozen=True)
class OperationResult(Generic[T]):
    _success: T | None = None
    _error: ErrorViewModel | None = None

    def __post_init__(self) -> None:
        if (self._success is None) == (self._error is None):
            raise ValueError("OperationResult must contain exactly one outcome")

    @property
    def is_success(self) -> bool:
        return self._error is None

    @property
    def success(self) -> T:
        if self._error is not None:
            raise ValueError("Cannot read success value from a failed operation")
        return cast(T, self._success)

    @property
    def error(self) -> ErrorViewModel | None:
        return self._error

    @classmethod
    def succeed(cls, value: T) -> "OperationResult[T]":
        return cls(_success=value)

    @classmethod
    def fail(cls, message: str, code: str | None = None) -> "OperationResult[T]":
        return cls(_error=ErrorViewModel(message, code))
