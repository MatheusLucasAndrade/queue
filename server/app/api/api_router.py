from fastapi import APIRouter

from app.api.routes import tickets

api_router = APIRouter()
api_router.include_router(tickets.router, prefix="/ticket", tags=["Ticket"])
