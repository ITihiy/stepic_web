#!/usr/bin/env bash
sudo pip3 install -U django==2.0.7
sudo sed -i -e "s/\/sbin\/python/\/sbin\/python3/" -e "s/17.5/19.6/" /usr/sbin/gunicorn-debian
sudo sed -i -e "s/\/sbin\/python/\/sbin\/python3/" -e "s/17.5/19.6/" /usr/bin/gunicorn
sudo sed -i -e "s/\/sbin\/python/\/sbin\/python3/" -e "s/17.5/19.6/" /usr/bin/gunicorn_django
sudo sed -i -e "s/\/sbin\/python/\/sbin\/python3/" -e "s/17.5/19.6/" /usr/bin/gunicorn_paster
sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/django_site.py /etc/gunicorn.d/django_site.py
sudo /etc/init.d/mysql restart
mysql -u root -e "create database qa_db;"
cd /home/box/web/ask/
python3 manage.py makemigrations
python3 manage.py migrate
sudo gunicorn -c /etc/gunicorn.d/django_site.py ask.wsgi:application

