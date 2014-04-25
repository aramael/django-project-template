import dj_database_url
import os
from settings.common import *

#==============================================================================
# Generic Django Project Settings
#==============================================================================

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': dj_database_url.config()
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['.herokuapp.com']

# Make this unique, and don't share it with anybody.
# Set it by issuing following command
# <code>
# heroku config:add SECRET_KEY=''
# </code>
SECRET_KEY = os.environ['SECRET_KEY']


#==============================================================================
# SSL Processing
#==============================================================================

# If this is set to True, the cookie will be marked as 'secure,' which means
# browsers may ensure that the cookie is only sent under an HTTPS connection.
SESSION_COOKIE_SECURE = False

# If this is set to True, the cookie will be marked as 'secure' which means
# browsers may ensure that the cookie is only sent under an HTTPS connection.
CSRF_COOKIE_SECURE = False

# See https://docs.djangoproject.com/en/1.6/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Whether to expire the session when the user closes his or her browser. See
# https://docs.djangoproject.com/en/1.6/topics/http/sessions/#browser-length-vs-persistent-sessions
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
