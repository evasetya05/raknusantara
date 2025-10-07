from .base import *

DEBUG = False
ALLOWED_HOSTS = ['raknusantara.teknusa.com', 'www.raknusantara.teknusa.com']


import pymysql
pymysql.install_as_MySQLdb()


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'teknusas_raknusantara',
        'USER': 'teknusas_raknusantara',
        'PASSWORD': '@Pontianak123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
    }
}

# Pengaturan static file untuk production
STATIC_ROOT = BASE_DIR / 'staticfiles'
