from dataclasses import dataclass


@dataclass(frozen=True)
class TicketDescription:
    """Required ticket description; OCA stores this field as sanitized HTML."""

    value: str

    def __post_init__(self) -> None:
        value = self.value.strip()
        if not value:
            raise ValueError("Ticket description cannot be empty")
        object.__setattr__(self, "value", value)
