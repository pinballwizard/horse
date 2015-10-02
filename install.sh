#!/bin/bash

project=santech

# Установка необходимых компонентов для RHEL7
sudo yum -y check-update
sudo yum groupinstall -y development
sudo yum -y install bash-completion zlib-dev openssl-devel sqlite-devel bzip2-devel xz-libs nmap mc nano git wget

# Выключение SELinux
sudo nano /etc/selinux/config
# echo 'SELINUX=disabled' >> /etc/selinux/config
sudo reboot

# Установка Python
wget http://www.python.org/ftp/python/3.4.3/Python-3.4.3.tar.xz
xz -d Python-3.4.3.tar.xz
tar -xvf Python-3.4.3.tar
cd Python-3.4.3
./configure
make
sudo make install
sudo rmdir Python-3.4.3
sudo rm Python-3.4.3.tar

# Добавление путей
sudo ln -s /usr/local/bin/pip3 /usr/bin/
sudo ln -s /usr/local/bin/python3 /usr/bin/

# Установка компонентов Python
sudo pip3 install virtualenv pillow uwsgi python-memcached python-social-auth markdown

# Установка компонентов Django
sudo pip3 install django django-admin-bootstrapped django-summernote django-classy-tags decorator django-ckeditor

git clone https://github.com/pinballwizard/santech

# Настройка uwsgi
sudo mkdir /var/log/uwsgi/
sudo touch /var/log/uwsgi/santech.log
sudo mkdir /etc/uwsgi/
sudo mkdir /etc/uwsgi/vassals/
sudo ln -s santech/uwsgi.ini /etc/uwsgi/vassals/
sudo cp santech/uwsgi.service /etc/systemd/system/
sudo ln -s /usr/local/bin/uwsgi /usr/bin/
sudo systemctl enable uwsgi.service
sudo systemctl start uwsgi.service

# Настройка Nginx
wget http://nginx.org/packages/rhel/7/noarch/RPMS/nginx-release-rhel-7-0.el7.ngx.noarch.rpm
sudo yum -y install nginx-release-rhel-7-0.el7.ngx.noarch.rpm
sudo rm nginx-release-rhel-7-0.el7.ngx.noarch.rpm
sudo yum -y install nginx
sudo cp santech/site_nginx.conf /etc/nginx/conf.d/
sudo systemctl enable nginx.service
sudo systemctl start nginx.service

# Настройка PostgreSQL
sudo yum -y install postgresql postgresql-libs postgresql-server postgresql-contrib postgresql-devel
sudo pip3 install psycopg2
sudo postgresql-setup initdb
#sudo initdb --locale en_US.UTF-8 -E UTF8 -D '/var/lib/pgsql/data'
sudo nano /var/lib/pgsql/data/postgresql.conf
# listen_addresses = '*', port = 5432, password_encryption = on
sudo nano /var/lib/pgsql/data/pg_hba.conf
# host all all 89.22.178.54/32 md5
sudo systemctl start postgresql.service
sudo systemctl enable postgresql.service
sudo -i -u postgres
# psql
# ALTER USER postgres WITH PASSWORD '14875264';
sudo systemctl restart postgresql.service
