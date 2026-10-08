from abc import ABC, abstractmethod

from ..dtos.create_ticket_from_text_response import CreateTicketFromTextResponse


class TicketTextGenerator(ABC):
    @abstractmethod
    def generate_from_text(self, text: str) -> CreateTicketFromTextResponse:
        ...
