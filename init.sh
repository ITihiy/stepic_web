#!/usr/bin/env bash
sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/django_site.py /etc/gunicorn.d/django_site.py
cd /home/box/web/
sudo gunicorn -c /etc/gunicorn.d/hello.py hello:wsgi_application
cd /home/box/web/ask/
sudo gunicorn -c /etc/gunicorn.d/django_site.py ask.wsgi:application
sudo /etc/init.d/mysql restart
