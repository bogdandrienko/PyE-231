from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")
# http://127.0.0.1:8000/


@app.route("/")
def index():
    return render_template('Index.html')

@app.route("/pricing")
def pricing():
    return render_template('Pricing.html')
