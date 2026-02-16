import httpx

GHIBLI_BASE_URL = "https://ghibliapi.vercel.app"


class GhibliClient:
    async def fetch_by_resource(self, resource: str) -> list[dict]:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{GHIBLI_BASE_URL}/{resource}")
            response.raise_for_status()
            return response.json()
