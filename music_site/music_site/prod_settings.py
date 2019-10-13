import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb',
        'PASSWORD': 'admin',
        'USER': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static','music')
MEDIA_ROOT = os.path.join(BASE_DIR, 'music')
MEDIA_URL = '/uploads/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'fil13698@gmail.com'
EMAIL_HOST_PASSWORD = 'kmuopwt8'