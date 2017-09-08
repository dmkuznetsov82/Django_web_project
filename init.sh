sudo ln -fs /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo ln -fs /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/nginx restart
sudo ln -fs /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo ln -fs /home/box/web/etc/gunicorn_2.conf /etc/gunicorn.d/test_2
sudo gunicorn -c /home/box/web/etc/gunicorn.conf hello:application &
sudo gunicorn -c /home/box/web/etc/gunicorn_2.conf ask:application &
#sudo /etc/init.d/gunicorn restart test
#sudo /etc/init.d/gunicorn restart test_2
#sudo /etc/init.d/mysql start
