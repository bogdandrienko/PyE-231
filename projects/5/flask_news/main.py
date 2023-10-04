import requests
from flask import Flask

app = Flask(__name__)


@app.route("/api/news")
def api_news():
    url = "https://fakenews.squirro.com/news/sport"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers).json()
    news = response['news']
    headlines = [x['headline'] for x in news]

    return {"news": headlines, "status": "OK"}
