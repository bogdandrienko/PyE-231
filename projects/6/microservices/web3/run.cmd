python -m venv env
call env/scripts/activate

pip install sanic
sanic main --host=0.0.0.0 --port=8003 --debug


cmd
