from aaconfig.settings import *


SECRET_KEY = 'django-insecure-)3%2)uickechh96kh@%pjv16lp)(7=ay9^!ag3ht*j&h)^*6g6'

DEBUG = True

CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = ['p2.alinasiri.com', 'www.p2.alinasiri.com']


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


#django compressor
COMPRESS_ENABLED = True
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_OFFLINE = True

if not COMPRESS_ENABLED:
    COMPRESS_ENABLED = True
    COMPRESS_CSS_FILTERS = ["compressor.filters.cssmin.CSSMinFilter"]
    COMPRESS_JS_FILTERS = ["compressor.filters.jsmin.JSMinFilter"]