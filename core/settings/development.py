from .base import *

SECRET_KEY = '3dpc0ko^pq=2egiz26@yur9zi^=qbr5%%0*_3m#5l0gq-xhm!2_a&m%e@n_a+toma+Anarul>'

DEBUG = True
# SECRET_KEY = config('SECRET_KEY')
# DEBUG = config('DEBUG')

ALLOWED_HOSTS = ['*']

# INSTALLED_APPS += []

# MIDDLEWARE += []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}