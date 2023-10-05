import sys
from PyQt6.QtWidgets import QApplication
from ui import Ui

if __name__ == "__main__":
    """
    MVP:
    1. Ядро
    2. Обёртка
    3. Мясо(доп фичи)
    """

    app = QApplication(sys.argv)
    ui = Ui()
    sys.exit(app.exec())
