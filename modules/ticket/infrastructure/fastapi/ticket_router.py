from fastapi import APIRouter, HTTPException

from bootstrap import Application
from ...application.error import ErrorCode
from ...presentation.dtos.create_ticket_http_request import CreateTicketHttpRequest

def create_ticket_router(application: Application | None) -> APIRouter:
    router = APIRouter(prefix="/tickets", tags=["tickets"])

    @router.post("", status_code=201)
    def create_ticket(http_request: CreateTicketHttpRequest) -> dict[str, str | list[str] | None]:
        if application is None:
            raise HTTPException(status_code=503, detail="Ticket text generation is not configured")
        result = application.ticket_controller.handle_create(http_request.text)
        error = result.error
        if error is not None:
            status_code = 422 if error.code == ErrorCode.VALIDATION_ERROR.value else 500
            raise HTTPException(status_code=status_code, detail=error.message)

        view_model = result.success
        return {
            "name": view_model.name,
            "description": view_model.description,
            "priority": view_model.priority,
            "category": view_model.category,
            "tags": list(view_model.tags),
        }

    return router
