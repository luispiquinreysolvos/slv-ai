from dataclasses import dataclass


@dataclass(frozen=True)
class CreateTicketFromTextRequest:
    text: str
