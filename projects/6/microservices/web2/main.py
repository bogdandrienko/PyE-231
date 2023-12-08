import aiohttp
from fastapi import FastAPI

app = FastAPI()


@app.get("/api")
async def api():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://127.0.0.1:8003/api") as response:
            data = await response.json()
    return {"data": data}
