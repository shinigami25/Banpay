from uuid import UUID

from fastapi import APIRouter, Depends

from application.schemas.user_schema import UserCreate, UserUpdate, UserResponse
from application.services.user_service import UserService
from domain.entities.user import User
from setup.dependencies import get_user_service, get_current_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[UserResponse])
def get_all_users(
    service: UserService = Depends(get_user_service),
    _current_user: User = Depends(get_current_user),
):
    return service.get_all()


@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: UUID,
    service: UserService = Depends(get_user_service),
    _current_user: User = Depends(get_current_user),
):
    return service.get_by_id(user_id)


@router.post("/", response_model=UserResponse, status_code=201)
def create_user(
    data: UserCreate,
    service: UserService = Depends(get_user_service),
):
    return service.create(data)


@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: UUID,
    data: UserUpdate,
    service: UserService = Depends(get_user_service),
    _current_user: User = Depends(get_current_user),
):
    return service.update(user_id, data)


@router.delete("/{user_id}", status_code=204)
def delete_user(
    user_id: UUID,
    service: UserService = Depends(get_user_service),
    _current_user: User = Depends(get_current_user),
):
    service.delete(user_id)
