from aaconfig.settings import *


SECRET_KEY = 'django-insecure-)3%2)uickechh96kh@%pjv16lp)(7=ay9^!ag3ht*j&h)^*6g6'

DEBUG = True 

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]