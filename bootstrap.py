from modules.ticket.application.interfaces.ticket_text_generator import TicketTextGenerator
from modules.ticket.application.use_cases.create_ticket_from_text import CreateTicketFromTextUseCase
from modules.ticket.presentation.controllers.ticket_controller import TicketController
from modules.ticket.presentation.presenters.ticket_presenter import TicketPresenter


class Application:
    def __init__(self, ticket_text_generator: TicketTextGenerator) -> None:
        self.create_ticket_from_text = CreateTicketFromTextUseCase(ticket_text_generator)
        self.ticket_controller = TicketController(
            create_use_case=self.create_ticket_from_text,
            presenter=TicketPresenter(),
        )
