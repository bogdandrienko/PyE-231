python -m venv env
call env/scripts/activate


pip install flask requests
pip install -r requirements.txt
pip freeze > requirements.txt
flask --app main run --host=0.0.0.0 --port=8000 --debug



cmd