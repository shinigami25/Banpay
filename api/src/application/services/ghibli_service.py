from fastapi import HTTPException

from domain.enums.role_enum import RoleEnum
from infrastructure.http.ghibli_client import GhibliClient
from application.schemas.ghibli_schema import GhibliResponse


class GhibliService:
    def __init__(self, client: GhibliClient):
        self.client = client

    async def get_data(self, role: RoleEnum) -> GhibliResponse:
        if role == RoleEnum.ADMIN:
            raise HTTPException(
                status_code=403,
                detail="ADMIN role does not have access to Ghibli data",
            )

        resource = role.value
        data = await self.client.fetch_by_resource(resource)
        return GhibliResponse(resource=resource, data=data)
