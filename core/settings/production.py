from .base import *
import dj_database_url

SECRET_KEY = config('SECRET_KEY', '3dpc0ko^pq=2egiz26@yur9zi^=qbr5%%0*_3m#5l0gq-xhm!2_a&m%e@n_a+toma+Anarul>')

DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = ['https://bdonlineshop.herokuapp.com/', '127.0.0.1','0.0.0.0']

# database management
DATABASES = {'default': dj_database_url.config()}

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())

# whitenoise collectstatic
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = config('EMAIL_BACKEND')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

# cloudinary config  for heroku
# image cloud services
cloudinary.config( 
  cloud_name = config('cloud_name'),
  api_key = config('api_key'), 
  api_secret = config('api_secret')
)