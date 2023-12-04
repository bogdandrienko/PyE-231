from fastapi import FastAPI

app = FastAPI()


@app.get("/")  # URL
async def index():  # VIEW(функция)
    # TEMPLATE (html)
    return "Hello World"


@app.get("/api")  # URL
async def api():
    return {"message": "OK"}
