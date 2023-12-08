from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    response = requests.get("http://127.0.0.1:8002/api")
    print(response.status_code)
    # if response.status_code != 200 or response.status_code != 201:
    #     raise Exception(response.status_code)
    if response.status_code not in (200, 201, 300, 301):
        raise Exception(response.status_code)
    return f"<p>Hello, World!{response.json()}</p>"
