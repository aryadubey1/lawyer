"""
Standalone script wrapper for running seed_db.
Usage: python scripts/seed_db.py
"""
import os
import sys

# Add project root to sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')

if __name__ == '__main__':
    import django
    django.setup()

    from django.core.management import call_command
    call_command('seed_db')
