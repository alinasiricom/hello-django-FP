from aaconfig.settings import *


SECRET_KEY = 'django-insecure-)3%2)uickechh96kh@%pjv16lp)(7=ay9^!ag3ht*j&h)^*6g6'

DEBUG = False

CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = ['p2.alinasiri.com', 'www.p2.alinasiri.com']


DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'alinasir_p2',
    'USER':'alinasir_ali',
    'PASSWORD':'BvGQ]}naicJo',
    'HOST':'localhost',
    'PORT':'3306',
    }
}


STATIC_ROOT = '/home/alinasir/p2.alinasiri.com/static'
MEDIA_ROOT = '/home/alinasir/p2.alinasiri.com/media'

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