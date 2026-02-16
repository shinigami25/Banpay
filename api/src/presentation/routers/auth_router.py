from fastapi import APIRouter, Depends

from application.schemas.auth_schema import LoginRequest, RefreshRequest, TokenResponse
from application.services.auth_service import AuthService
from setup.dependencies import get_auth_service

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, service: AuthService = Depends(get_auth_service)):
    return service.login(data)


@router.post("/refresh", response_model=TokenResponse)
def refresh(data: RefreshRequest, service: AuthService = Depends(get_auth_service)):
    return service.refresh(data)
