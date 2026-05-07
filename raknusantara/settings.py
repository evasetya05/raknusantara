import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'django-insecure-a@)zh2e8-)^i_bk9(x3m_qj%iq0#9d&-k=(g_)nq9k74+qv5xf'


DEBUG = True
ALLOWED_HOSTS = ['raknusantara.teknusa.com', 'www.raknusantara.teknusa.com', 'localhost', '127.0.0.1', '192.168.18.111']
CSRF_TRUSTED_ORIGINS = [
    'https://raknusantara.teknusa.com',
    'https://www.raknusantara.teknusa.com',
]


db_host = os.environ.get('DB_HOST', '127.0.0.1')

# Docker Compose service names (e.g. "db") only resolve inside Docker networks.
# If app runs on host machine and DB_HOST is "db", fallback to localhost.
if db_host == 'db' and not os.path.exists('/.dockerenv'):
    db_host = '127.0.0.1'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'raknusantara_db'),
        'USER': os.environ.get('DB_USER', 'raknusantara_user'),
        'PASSWORD': os.environ.get('DB_PASSWORD', '@Pontianak123'),
        'HOST': db_host,
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Pengaturan static file untuk production
STATIC_ROOT = BASE_DIR / 'staticfiles'


LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'item',
    'dashboard',
    'conversation',
    'perpustakaan',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'raknusantara.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'raknusantara.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
