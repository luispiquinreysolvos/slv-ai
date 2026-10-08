from ...domain.entities.ticket import Ticket
from ..dtos.create_ticket_from_text_request import CreateTicketFromTextRequest
from ..dtos.create_ticket_from_text_response import CreateTicketFromTextResponse
from ..interfaces.ticket_text_generator import TicketTextGenerator
from ..error import Error
from ..result import Result


class CreateTicketFromTextUseCase:
    def __init__(self, ticket_text_generator: TicketTextGenerator) -> None:
        self.ticket_text_generator = ticket_text_generator

    def execute(self, request: CreateTicketFromTextRequest) -> Result[CreateTicketFromTextResponse]:
        if not request.text.strip():
            return Result.failure(Error.validation_error("Ticket text cannot be empty"))

        response = self.ticket_text_generator.generate_from_text(request.text)
        try:
            ticket = Ticket.create(
                name=response.name,
                description=response.description,
                priority=response.priority,
                category=response.category,
                tags=response.tags,
            )
        except ValueError as error:
            return Result.failure(Error.validation_error(str(error)))
        return Result.success(
            CreateTicketFromTextResponse(
                name=ticket.name.value,
                description=ticket.description.value,
                priority=ticket.priority,
                category=ticket.category,
                tags=ticket.tags,
            )
        )
