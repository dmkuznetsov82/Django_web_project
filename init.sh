sudo ln -fs /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo ln -fs /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/nginx restart
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start
