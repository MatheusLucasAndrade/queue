from datetime import datetime

import uuid

from typing import Optional
from pydantic import BaseModel, Field

from app.models.enums.base_enum import TicketPriority


class TicketBase(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")


class TicketCreate(TicketBase):
    ticket_number: int = Field(...)
    ticket_priority: TicketPriority = Field(default=TicketPriority.LOW.value)
    client_name: str = Field(...)
    category_type: str = Field(default=None)
    description: str = Field(default=None)
    completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    # def __init__(self, **data):
    #     # Se o número do ticket não for fornecido, gera um novo número auto-incrementado
    #     if "ticket_number" not in data:
    #         data["ticket_number"] = self._get_next_ticket_number()
    #     super().__init__(**data)

    # @classmethod
    # def _get_next_ticket_number(cls):
    #     if not hasattr(cls, "_ticket_counter"):
    #         cls._ticket_counter = 1
    #     else:
    #         cls._ticket_counter += 1
    #     return cls._ticket_counter

    # class Config:
    #     populate_by_name = True
    #     arbitrary_types_allowed = True
    #     json_schema_extra = {
    #         "example": {
    #             "client_name": "Person name",
    #             "ticket_priority": TicketPriority.LOW.name,
    #             "category_type": "any category",
    #             "description": "O Paciente está se queixando de dor no pé",
    #             "completed": False,
    #         }
    #     }


class TicketUpdate(TicketBase):
    ticket_number: Optional[int]
    ticket_priority: Optional[TicketPriority]
    category_type: Optional[str]
    description: Optional[str]
    completed: Optional[bool]
    updated_at: datetime = Field(default_factory=datetime.now)


class TicketDelete(TicketBase):
    id: str = Field(...)
