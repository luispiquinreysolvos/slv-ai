from pydantic import BaseModel


class CreateTicketHttpRequest(BaseModel):
    text: str
