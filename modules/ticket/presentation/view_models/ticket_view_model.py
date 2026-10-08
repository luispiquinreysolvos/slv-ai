from dataclasses import dataclass


@dataclass(frozen=True)
class TicketViewModel:
    name: str
    description: str
    priority: str
    category: str | None
    tags: tuple[str, ...]
