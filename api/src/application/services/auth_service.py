from fastapi import HTTPException

from domain.repositories.user_repository import UserRepository
from infrastructure.security.password_handler import verify_password
from infrastructure.security.jwt_handler import (
    create_access_token,
    create_refresh_token,
    decode_token,
)
from application.schemas.auth_schema import LoginRequest, RefreshRequest, TokenResponse


class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def login(self, data: LoginRequest) -> TokenResponse:
        user = self.repository.get_by_username(data.username)
        if not user or not verify_password(data.password, user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        payload = {"sub": user.username, "user_id": str(user.id), "role": user.role.value}
        return TokenResponse(
            access_token=create_access_token(payload),
            refresh_token=create_refresh_token(payload),
        )

    def refresh(self, data: RefreshRequest) -> TokenResponse:
        token_data = decode_token(data.refresh_token)
        if not token_data or token_data.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Invalid refresh token")

        user = self.repository.get_by_username(token_data["sub"])
        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        payload = {"sub": user.username, "user_id": str(user.id), "role": user.role.value}
        return TokenResponse(
            access_token=create_access_token(payload),
            refresh_token=create_refresh_token(payload),
        )
