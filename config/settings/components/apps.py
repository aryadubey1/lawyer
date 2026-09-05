"""
INSTALLED_APPS configuration for Lex Chambers.
"""

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'corsheaders',
    'django_filters',
    'django_q',
    'cloudinary',
    'cloudinary_storage',
    'tailwind',
    'theme',
    'ckeditor',
    'ckeditor_uploader',
]

LOCAL_APPS = [
    'apps.core',
    'apps.practice_areas',
    'apps.team',
    'apps.blog',
    'apps.gallery',
    'apps.clients',
    'apps.about',
    'apps.contact',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
