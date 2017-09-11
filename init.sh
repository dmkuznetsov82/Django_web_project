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

#sudo ln -fs /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo ln -fs /home/box/web/etc/gunicorn_2.conf /etc/gunicorn.d/test_2
#sudo gunicorn -c /home/box/web/etc/gunicorn.conf hello:application &
#sudo gunicorn -c /home/box/web/etc/gunicorn_2.conf ask.ask.wsgi:application &
#sudo /etc/init.d/gunicorn restart test
#sudo /etc/init.d/gunicorn restart test_2
#sudo /etc/init.d/mysql start
