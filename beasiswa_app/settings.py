"""
Sistem Penunjang Keputusan (SPK) Universitas Terbuka
Versi 1.0 Beta
Coded by Alzea Arafat (www.zeaja.com)
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


SECRET_KEY = 'k_8h-_5goj3g(6uo@k2w308%v9lw$46afci*dm%b9d*a6_e0ie'

DEBUG = True

TEMPLATE_DEBUG = True


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

STATIC_URL = '/static/'

ADMINS = (
    ('Alzea', 'alzea.arafat@gmail.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'django_tables2',
    'mahasiswa',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
)


ROOT_URLCONF = 'beasiswa_app.urls'

WSGI_APPLICATION = 'beasiswa_app.wsgi.application'


# Database Inih

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DSS_python_DBS',
        'USER': 'root',
        'PASSWORD': 'adminadmin',
        'HOST': 'localhost',
    }
}

LANGUAGE_CODE = 'id-id'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_L10N = True
USE_TZ = True

ugettext = lambda s: s

LANGUAGES = (
    ('id', ugettext('Indonesia')),
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request', 
)

SUIT_CONFIG = {
    'ADMIN_NAME': 'SPK Univ. Terbuka'
}


DECIMAL_SEPARATOR='.'

USE_THOUSAND_SEPARATOR= True 

STATIC_URL = '/static/'

STATIC_ROOT = '/static_root/'
