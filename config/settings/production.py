"""
Production settings.
"""
from .base import *  # noqa
from decouple import config

DEBUG = False

ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default='advsubhashmishra.clarifyweb.com'
).split(',')

# Security — toggle via env so SSL-dependent settings can be off until certs exist
SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=False, cast=bool)
SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=False, cast=bool)
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', default=False, cast=bool)

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

CSRF_TRUSTED_ORIGINS = config(
    'CSRF_TRUSTED_ORIGINS',
    default='https://advsubhashmishra.clarifyweb.com'
).split(',')

# Production email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Logging to file in production
LOG_DIR = config('LOG_DIR', default='/var/log/lawyer')
LOGGING['handlers']['file'] = {  # noqa
    'class': 'logging.FileHandler',
    'filename': f'{LOG_DIR}/django.log',
    'formatter': 'verbose',
}