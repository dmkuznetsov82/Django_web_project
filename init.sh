#!/bin/bash
sudo rm -r /etc/nginx/sites-enabled/default
sudo ln -fs /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo ln -fs /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/nginx restart

sudo rm -r /etc/gunicorn.d/test
sudo rm -r /etc/gunicorn.d/django
sudo ln -fs /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo ln -fs /home/box/web/etc/django.conf /etc/gunicorn.d/django
sudo /etc/init.d/gunicorn restart

#sudo /etc/init.d/mysql start
