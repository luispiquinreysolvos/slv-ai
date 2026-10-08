from dataclasses import dataclass
from typing import Generic, TypeVar, cast

from .error import Error

T = TypeVar("T")


@dataclass(frozen=True)
class Result(Generic[T]):
    _value: T | None = None
    error: Error | None = None

    def __post_init__(self) -> None:
        if (self._value is None) == (self.error is None):
            raise ValueError("Result must contain exactly one of value or error")

    @property
    def is_success(self) -> bool:
        return self.error is None

    @property
    def value(self) -> T:
        if self.error is not None:
            raise ValueError("Cannot read value from a failed result")
        return cast(T, self._value)

    @classmethod
    def success(cls, value: T) -> "Result[T]":
        return cls(_value=value)

    @classmethod
    def failure(cls, error: Error) -> "Result[T]":
        return cls(error=error)
