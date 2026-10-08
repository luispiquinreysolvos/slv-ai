from dataclasses import dataclass


@dataclass(frozen=True)
class TicketTag:
    """OCA helpdesk.ticket.tag reference (Many2many)."""

    id: int
    name: str

    def __post_init__(self) -> None:
        if self.id <= 0:
            raise ValueError("Ticket tag id must be positive")
        name = self.name.strip()
        if not name:
            raise ValueError("Ticket tag name cannot be empty")
        object.__setattr__(self, "name", name)
