from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from infrastructure.database import get_db
from infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from infrastructure.security.jwt_handler import decode_token
from application.services.user_service import UserService
from application.services.auth_service import AuthService
from application.services.ghibli_service import GhibliService
from infrastructure.http.ghibli_client import GhibliClient
from domain.entities.user import User

security = HTTPBearer()


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    repository = UserRepositoryImpl(db)
    return UserService(repository)


def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
    repository = UserRepositoryImpl(db)
    return AuthService(repository)


def get_ghibli_service() -> GhibliService:
    client = GhibliClient()
    return GhibliService(client)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
) -> User:
    token_data = decode_token(credentials.credentials)
    if not token_data or token_data.get("type") != "access":
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    repository = UserRepositoryImpl(db)
    user = repository.get_by_username(token_data["sub"])
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user
