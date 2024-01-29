import requests
from requests import Response

data: dict[str, str] = {"name": "Roman"}
response: Response = requests.post("http://127.0.0.1:8000/test/", data)
print(response, response.status_code)
print(response.json())
