from sanic import Sanic
from sanic.response import json

app = Sanic("MyHelloWorldApp")


@app.get("/api")
async def api(request):
    data = {"name": "Евгений", "items": [x for x in range(1, 10)]}
    return json({"data": data})
