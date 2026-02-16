from fastapi import APIRouter, Depends

from application.schemas.ghibli_schema import GhibliResponse
from application.services.ghibli_service import GhibliService
from domain.entities.user import User
from setup.dependencies import get_ghibli_service, get_current_user

router = APIRouter(prefix="/ghibli", tags=["Ghibli"])


@router.get("/", response_model=GhibliResponse)
async def get_ghibli_data(
    service: GhibliService = Depends(get_ghibli_service),
    current_user: User = Depends(get_current_user),
):
    return await service.get_data(current_user.role)
