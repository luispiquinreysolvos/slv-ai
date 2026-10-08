from dataclasses import dataclass, field

from ..value_objects.ticket_category import TicketCategory
from ..value_objects.ticket_description import TicketDescription
from ..value_objects.ticket_id import TicketId
from ..value_objects.ticket_name import TicketName
from ..value_objects.ticket_number import TicketNumber
from ..value_objects.ticket_priority import TicketPriority
from ..value_objects.ticket_tag import TicketTag


@dataclass
class Ticket:
    name: TicketName
    description: TicketDescription
    id: TicketId | None = None
    number: TicketNumber | None = None
    priority: TicketPriority = TicketPriority.MEDIUM
    tags: tuple[TicketTag, ...] = field(default_factory=tuple)
    category: TicketCategory | None = None

    @classmethod
    def create(
        cls,
        name: str,
        description: str,
        *,
        priority: TicketPriority = TicketPriority.MEDIUM,
        tags: tuple[TicketTag, ...] = (),
        category: TicketCategory | None = None,
    ) -> "Ticket":
        return cls(
            name=TicketName(name),
            description=TicketDescription(description),
            priority=priority,
            tags=tuple(tags),
            category=category,
        )
