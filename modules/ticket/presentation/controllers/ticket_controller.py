from dataclasses import dataclass

from ...application.dtos.create_ticket_from_text_request import CreateTicketFromTextRequest
from ...application.use_cases.create_ticket_from_text import CreateTicketFromTextUseCase
from ..results.operation_result import OperationResult
from ..presenters.ticket_presenter import TicketPresenter
from ..view_models.ticket_view_model import TicketViewModel


@dataclass
class TicketController:
    create_use_case: CreateTicketFromTextUseCase
    presenter: TicketPresenter

    def handle_create(self, text: str) -> OperationResult[TicketViewModel]:
        request = CreateTicketFromTextRequest(text=text)
        result = self.create_use_case.execute(request)
        if result.error is not None:
            error = self.presenter.present_error(result.error.message, result.error.code.value)
            return OperationResult.fail(error.message, error.code)
        return OperationResult.succeed(self.presenter.present_ticket(result.value))
