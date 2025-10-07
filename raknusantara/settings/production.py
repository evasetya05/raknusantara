from .base import *

DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Contoh: konfigurasi MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'raknusantara',
        'USER': 'dbuser',
        'PASSWORD': 'dbpassword',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
    }
}

# Pengaturan static file untuk production
STATIC_ROOT = BASE_DIR / 'staticfiles'
