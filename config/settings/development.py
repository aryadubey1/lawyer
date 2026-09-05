"""
Development settings for Lex Chambers.
"""
from .base import *  # noqa

DEBUG = True

ALLOWED_HOSTS = ['*']

# Django debug toolbar (optional — install separately)
# INSTALLED_APPS += ['debug_toolbar']
# MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

# Use console email backend in development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Relax CSRF for local API testing
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]
