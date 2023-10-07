import uuid
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.models.enums.base_enum import TicketPriority


class TicketBase(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")


class TicketCreate(TicketBase):
    ticket_code: str = Field(...)
    ticket_priority: TicketPriority = Field(default=TicketPriority.LOW.value)
    client_name: str = Field(...)
    category_type: str = Field(default=None)
    description: str = Field(default=None)
    completed: bool = Field(default=False)
    created_at: str = Field(default_factory=datetime.now)
    updated_at: str = Field(default_factory=datetime.now)


class TicketUpdate(BaseModel):
    ticket_code: Optional[str]
    ticket_priority: Optional[TicketPriority]
    category_type: Optional[str]
    description: Optional[str]
    completed: Optional[bool]
    updated_at: str = Field(default_factory=datetime.now)


class TicketDelete(TicketBase):
    id: str = Field(...)
