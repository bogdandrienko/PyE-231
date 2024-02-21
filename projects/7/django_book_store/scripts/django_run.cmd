cd ..
python -m venv venv
call venv/scripts/activate
pip install -r requirements.txt
pip install django
pip install freeze > requirements.txt



python manage.py runserver 0.0.0.0:8000



cmd
