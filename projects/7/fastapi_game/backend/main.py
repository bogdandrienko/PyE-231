import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "localhost:3000",
        "http://127.0.0.1:3000",
        "127.0.0.1:3000",
        "http://127.0.0.1:8000",
        "127.0.0.1:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/data/")
async def get_data():
    data = {"message": "Привет, Нурдаулет!"}

    data = {"question_id": 123, "question": "Сколько у людей пальцев?", "answers": ["10", "20", "22", "9"]}

    await asyncio.sleep(1.0)

    return {"success": data}


from fastapi import Request


@app.get("/api/answer/")
async def get_answer(request: Request):
    print(request.query_params)
    return {"success": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
