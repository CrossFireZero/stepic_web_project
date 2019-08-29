sudo rm /etc/nginx/sites-available/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-available/default
sudo service nginx restart
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart﻿﻿
mysql -uroot -e "create database ask;"
mysql -uroot -e "grant all privileges on ask.* to 'box'@'localhost' with grant option;"
