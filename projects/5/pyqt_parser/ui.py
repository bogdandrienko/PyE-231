import asyncio
import threading
import requests
import time
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from view import get_valutes


class Ui(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("src/main.ui", self)
        self.ui.labelData.setText("Searching...")
        self.show()

        self.example()

    def example(self):
        new_thread = threading.Thread(target=self.ex)
        new_thread.start()

    def ex(self):
        time.sleep(1)
        asyncio.run(self.setData())

    async def setData(self):
        # crypto
        # vals = await get_valutes(url="https://www.coingecko.com/", filter_by_price=1000.0)
        # message = ''
        # for i in vals:
        #     message += f'{i.get_beauty_text()}\n'
        # self.ui.labelData.setText(message)

        # news
        url = "http://127.0.0.1:8000/api/news"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers).json()
        news = response['news']
        message = ''
        for i in news:
            message += f'{i}\n'
        self.ui.labelData.setText(message)
        pass