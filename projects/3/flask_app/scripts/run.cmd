cd ..
python -m venv env
call env/scripts/activate
flask --app main run --host=0.0.0.0 --port=8000 --debug

cmd