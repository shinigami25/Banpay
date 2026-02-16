from fastapi import HTTPException

from domain.entities.user import User
from domain.repositories.user_repository import UserRepository
from application.schemas.user_schema import UserCreate, UserUpdate
from infrastructure.security.password_handler import hash_password


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_all(self) -> list[User]:
        return self.repository.get_all()

    def get_by_id(self, user_id: int) -> User:
        user = self.repository.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def create(self, data: UserCreate) -> User:
        user = User(
            username=data.username,
            role=data.role,
            password=hash_password(data.password),
        )
        return self.repository.create(user)

    def update(self, user_id: int, data: UserUpdate) -> User:
        user = self.get_by_id(user_id)
        update_data = data.model_dump(exclude_unset=True)
        if "password" in update_data:
            update_data["password"] = hash_password(update_data["password"])
        for key, value in update_data.items():
            setattr(user, key, value)
        return self.repository.update(user)

    def delete(self, user_id: int) -> None:
        deleted = self.repository.delete(user_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="User not found")
