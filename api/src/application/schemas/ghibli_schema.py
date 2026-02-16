from pydantic import BaseModel


class GhibliResponse(BaseModel):
    resource: str
    data: list[dict]
