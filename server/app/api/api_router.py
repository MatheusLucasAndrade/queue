from fastapi import APIRouter

from app.api.routes import tickets, users

api_router = APIRouter()
api_router.include_router(tickets.router, prefix="/ticket", tags=["Ticket"])
api_router.include_router(users.router, prefix="/user", tags=["Users"])
