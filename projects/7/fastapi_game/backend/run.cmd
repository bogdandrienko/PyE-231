python -m venv env
call env/scripts/activate
pip install fastapi

uvicorn main:app --reload --host=localhost --port=8000

cmd