cd ..
python -m venv env
call env/scripts/activate
pip install -r requirements.txt
pip install django
pip freeze > requirements.txt



python manage.py runserver 0.0.0.0:8000



cmd
