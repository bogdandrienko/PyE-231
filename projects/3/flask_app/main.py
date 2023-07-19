import datetime
import random

from flask import Flask

app = Flask(__name__)
# https://flask.palletsprojects.com/en/2.3.x/

@app.route("/")
def hello_world():
    return f"<p>Hello, Евгений, {random.randint(1, 1000)}!</p>"


@app.route("/home")
def home():
    return f"<h1>Home Page {datetime.datetime.now()}</h1>"
