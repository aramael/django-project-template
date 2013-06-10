import os
from settings.common import *

#==============================================================================
# Generic Django Project Settings
#==============================================================================

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': ''
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ secret_key }}'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'