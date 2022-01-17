import os


SECRET_KEY = '123admin123'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'm2m-relations-1',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
    }
}