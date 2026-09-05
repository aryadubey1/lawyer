"""
Database configuration for Lex Chambers.
Uses dj-database-url to parse DATABASE_URL from environment.
"""
import dj_database_url
from decouple import config

DATABASES = {
    'default': dj_database_url.parse(
        config('DATABASE_URL', default='postgres://lex_user:lex_pass@localhost:5432/lex_chambers'),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
