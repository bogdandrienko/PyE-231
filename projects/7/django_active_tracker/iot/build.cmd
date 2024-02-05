python -m venv venv
call venv/scripts/activate
pip install pyinstaller requests
pyinstaller --onefile --console main.py
cmd