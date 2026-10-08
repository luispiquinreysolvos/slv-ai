from fastapi import FastAPI
from modules.ticket.infrastructure.fastapi.ticket_router import router as ticket_router

app = FastAPI()
app.include_router(ticket_router)

