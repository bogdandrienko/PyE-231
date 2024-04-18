sudo apt-get update -y
sudo apt-get install -y nginx gunicorn wget gcc make
sudo apt-get install -y build-essential libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get install -y python3.11 python3.11-venv python3.11-dev

sudo usermod -aG ubuntu www-data
sudo ufw allow 'Nginx Full'
timedatectl set-timezone Asia/Almaty
######################################

mkdir web

cd web
python3.11 -m venv venv
source venv/bin/activate
python -V
pip install django gunicorn
pip install -r requirements.txt
ip a
django-admin startproject django_settings .
# http://194.67.82.59:8000/
nano django_settings/settings.py
python manage.py runserver 0.0.0.0:8000
gunicorn --bind 0.0.0.0:8000 django_settings.wsgi
# http://192.168.1.178:8000/

#


pwd
# copy project to /root/web
pip install -r requirements.txt


########################################################################################################################
GUNICORN
########################################################################################################################
# sudo rm /etc/systemd/system/gunicorn.socket
sudo nano /etc/systemd/system/gunicorn.socket
<file>
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
</file>

# sudo rm /etc/systemd/system/gunicorn.service
sudo nano /etc/systemd/system/gunicorn.service
<file>
[Unit]
Description=Gunicorn for the Django project
Requires=gunicorn.socket
After=network.target

[Service]
Type=notify

User=ubuntu
Group=www-data

RuntimeDirectory=gunicorn
WorkingDirectory=/home/ubuntu/web
ExecStart=/home/ubuntu/web/venv/bin/gunicorn --workers 9 --bind unix:/run/gunicorn.sock django_settings.wsgi:application
ExecReload=/bin/kill -s HUP $MAINPID
KillMode=mixed
TimeoutStopSec=5
PrivateTmp=true

[Install]
WantedBy=multi-user.target
</file>

sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable --now gunicorn.service
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl status gunicorn.service

########################################################################################################################
NGINX
########################################################################################################################

sudo rm /etc/nginx/sites-available/web-http.conf
sudo rm /etc/nginx/sites-available/web-https.conf

sudo rm /etc/nginx/sites-enabled/web-http.conf
sudo rm /etc/nginx/sites-enabled/web-https.conf

sudo nano /etc/nginx/sites-available/web-http.conf
<file>
server {
listen 80;
listen [::]:80;

server_name 127.0.0.1 192.168.1.178 188.247.181.206 kgp.lol www.kgp.lol;

root /home/ubuntu/web;

location /.well-known/acme-challenge/ {}

location / {
    return 301 https://$server_name$request_uri;
}
}
</file>
sudo ln -s /etc/nginx/sites-available/web-http.conf /etc/nginx/sites-enabled/web-http.conf
sudo service nginx start
sudo systemctl reload nginx.service
sudo systemctl restart nginx
sudo systemctl status nginx.service
# http://192.168.1.178:80/



sudo snap install --classic certbot
sudo certbot delete
sudo certbot certonly --webroot -w /home/ubuntu/web -d kgp.lol -m bogdandrienko@gmail.com --agree-tos
sudo openssl dhparam -out /etc/nginx/dhparam.pem 2048

sudo nano /etc/nginx/sites-available/web-https.conf
<file>
server {
listen 443 ssl http2;
listen [::]:443 ssl http2;

ssl_certificate /etc/letsencrypt/live/kgp.lol/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/kgp.lol/privkey.pem;

ssl_session_timeout 1d;
ssl_session_cache shared:MozSSL:10m;

ssl_dhparam /etc/nginx/dhparam.pem;

ssl_protocols TLSv1.2;
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;
ssl_prefer_server_ciphers off;

ssl_stapling on;
ssl_stapling_verify on;

ssl_trusted_certificate /etc/letsencrypt/live/kgp.lol/chain.pem;

resolver 1.1.1.1;

client_max_body_size 100M;

server_name 127.0.0.1 192.168.1.178 kgp.lol www.kgp.lol;

root /home/ubuntu/web;

location /.well-known/acme-challenge/ {}

location /favicon.ico {
    alias /home/ubuntu/web/static/logo.png;

    access_log off; log_not_found off;

    expires max;
}

location /robots.txt {
    alias /home/ubuntu/web/static/robots.txt;

    access_log off; log_not_found off;

    expires max;
}

location /static/ {
    alias /home/ubuntu/web/static/;

    expires max;
}

location /media/ {
    alias /home/ubuntu/web/static/media/;

    expires max;
}

location / {
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header Host $http_host;
    proxy_redirect off;
    proxy_buffering off;
    proxy_pass http://unix:/run/gunicorn.sock;
}
}
</file>

sudo ln -s /etc/nginx/sites-available/web-https.conf /etc/nginx/sites-enabled/web-https.conf
sudo service nginx start
sudo systemctl reload nginx.service
sudo systemctl status nginx.service

sudo journalctl -u gunicorn.service -f

https://kgp.lol/