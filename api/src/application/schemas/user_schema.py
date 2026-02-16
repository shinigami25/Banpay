from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from domain.enums.role_enum import RoleEnum


class UserCreate(BaseModel):
    username: str
    role: RoleEnum
    password: str


class UserUpdate(BaseModel):
    username: str | None = None
    role: RoleEnum | None = None
    password: str | None = None


class UserResponse(BaseModel):
    id: UUID
    username: str
    role: RoleEnum
    creation_date: datetime

    model_config = {"from_attributes": True}
