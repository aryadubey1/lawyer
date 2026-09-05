"""
Production settings for Lex Chambers.
"""
from .base import *  # noqa
from decouple import config

DEBUG = False

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='lexchambers.in,www.lexchambers.in').split(',')

# Security
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

CSRF_TRUSTED_ORIGINS = config(
    'CSRF_TRUSTED_ORIGINS',
    default='https://lexchambers.in,https://www.lexchambers.in'
).split(',')

# Production email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Logging to file in production
LOGGING['handlers']['file'] = {  # noqa
    'class': 'logging.FileHandler',
    'filename': '/var/log/lex_chambers/django.log',
    'formatter': 'verbose',
}
