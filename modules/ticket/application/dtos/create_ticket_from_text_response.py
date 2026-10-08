from dataclasses import dataclass

from ...domain.value_objects.ticket_category import TicketCategory
from ...domain.value_objects.ticket_priority import TicketPriority
from ...domain.value_objects.ticket_tag import TicketTag


@dataclass(frozen=True)
class CreateTicketFromTextResponse:
    name: str
    description: str
    priority: TicketPriority
    category: TicketCategory | None = None
    tags: tuple[TicketTag, ...] = ()
