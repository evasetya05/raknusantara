from .base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

from .base import *
import pymysql

pymysql.install_as_MySQLdb()

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'raknusantara',     # ganti dengan nama DB Anda
        'USER': 'eva',         # ganti user MySQL
        'PASSWORD': 'abc', # ganti password MySQL
        'HOST': 'localhost',         # atau IP server
        'PORT': '3306',              # default MySQL port
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
