from .base import *
import dj_database_url
SECRET_KEY = '3dpc0ko^pq=2egiz26@yur9zi^=qbr5%%0*_3m#5l0gq-xhm!2_a&m%e@n_a+toma+Anarul>'

DEBUG = True

# SECRET_KEY = config('SECRET_KEY', '3dpc0ko^pq=2egiz26@yur9zi^=qbr5%%0*_3m#5l0gq-xhm!2_a&m%e@n_a+toma+Anarul>')

# DEBUG = config('DEBUG', cast=bool)
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['https://bdonlineshop.herokuapp.com/','*']

# database management
DATABASES = {'default': dj_database_url.config()}

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())

# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_BACKEND = config('EMAIL_BACKEND')
# DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mdanarul7075@gmail.com'
EMAIL_HOST_PASSWORD = 'ydaqqzkuvbwovopf'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'mdanarul7075@gmail.com'

# cloudinary config  for heroku
# image cloud services
# cloudinary.config( 
#   cloud_name = config('cloud_name'),
#   api_key = config('api_key'), 
#   api_secret = config('api_secret')
# )
cloudinary.config( 
  cloud_name = 'bdonlineshop',
  api_key = '282249648444274',
  api_secret =' 6uvJ5DlJEhnfLiRh6NPTdbxQbRo'
)