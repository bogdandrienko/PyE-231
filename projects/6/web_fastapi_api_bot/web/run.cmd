python -m venv env
call env/scripts/activate

pip install fastapi[all] jinja2 uvicorn openpyxl

uvicorn main:app --reload --port=8000


cmd
