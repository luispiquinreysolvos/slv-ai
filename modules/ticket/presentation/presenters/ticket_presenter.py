from ...application.dtos.create_ticket_from_text_response import CreateTicketFromTextResponse
from ..results.operation_result import ErrorViewModel
from ..view_models.ticket_view_model import TicketViewModel


class TicketPresenter:
    def present_ticket(self, response: CreateTicketFromTextResponse) -> TicketViewModel:
        return TicketViewModel(
            name=response.name,
            description=response.description,
            priority=response.priority.name.replace("_", " ").title(),
            category=response.category.name if response.category else None,
            tags=tuple(tag.name for tag in response.tags),
        )

    def present_error(self, message: str, code: str | None = None) -> ErrorViewModel:
        return ErrorViewModel(message=message, code=code)
