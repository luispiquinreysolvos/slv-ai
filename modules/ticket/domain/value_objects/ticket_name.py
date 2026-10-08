from dataclasses import dataclass


@dataclass(frozen=True)
class TicketName:
    value: str

    def __post_init__(self) -> None:
        value = self.value.strip()
        if not value:
            raise ValueError("Ticket name cannot be empty")
        object.__setattr__(self, "value", value)
