from dataclasses import dataclass


@dataclass(frozen=True)
class TicketCategory:
    """OCA helpdesk.ticket.category reference (Many2one)."""

    id: int
    name: str

    def __post_init__(self) -> None:
        if self.id <= 0:
            raise ValueError("Ticket category id must be positive")
        name = self.name.strip()
        if not name:
            raise ValueError("Ticket category name cannot be empty")
        object.__setattr__(self, "name", name)
