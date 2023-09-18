python -m venv venv
call env/scripts/activate
pip install Flask
pip install -r requirements.txt

flask --app main run --host=0.0.0.0 --port=8000 --debug


cmd