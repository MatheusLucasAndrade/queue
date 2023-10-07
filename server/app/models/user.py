import uuid
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.models.enums.base_enum import UserProfile


class UserBase(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")


class UserCreate(UserBase):
    user_name: str = Field(...)
    is_active: bool = Field(default_factory=False)
    user_profile: UserProfile = Field(default=UserProfile.USER.value)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


class UserUpdate(BaseModel):
    user_profile: Optional[UserProfile]
    is_active: Optional[bool]
    updated_at: datetime = Field(default_factory=datetime.now)


class UserDelete(UserBase):
    id: str = Field(...)
