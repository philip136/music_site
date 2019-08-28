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


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'fil13698@gmail.com'
EMAIL_HOST_PASSWORD = 'kmuopwt8'


