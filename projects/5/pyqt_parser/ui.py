import asyncio
import threading
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
        vals = await get_valutes(url="https://www.coingecko.com/", filter_by_price=1000.0)
        message = ''
        for i in vals:
            message += f'{i.get_beauty_text()}\n'
        self.ui.labelData.setText(message)
