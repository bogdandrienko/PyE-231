# oblako.kz (4600) / ps.kz (3200) / hoster.kz (2400)
#
# 1. Создать операционную систему - linux, ubuntu 22.04, minimal power
#
# 2. Connect to ssh
# https://www.bitvise.com/ssh-client-download
# 188.94.156.164
# root
# m2VLe1pi

# 3. Скопировать проект (github/gitlab, sftp)
#

# 4. Восстановить виртуальное окружение

# обновляют все внутренние репозитории и библитеки
# sudo apt-get update -y
# sudo apt-get upgrade -y

# установка дополнительных библиотек
# sudo apt-get install -y nginx gunicorn wget gcc make
# sudo apt-get install -y build-essential libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev

# добавление python3.11
# sudo add-apt-repository ppa:deadsnakes/ppa
# sudo apt-get install -y python3.11 python3.11-venv python3.11-dev

# cd web
# python3.11 -m venv env
# source env/bin/activate
# python -V
# pip install -r requirements.txt
# uvicorn main:app --reload --host=0.0.0.0 --port=8000

# 5. Запустить fastapi
#
