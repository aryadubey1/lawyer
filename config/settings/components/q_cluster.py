"""
Django Q2 cluster configuration for Lex Chambers.
Used for async Telegram notification tasks on contact form submissions.

Run with: python manage.py qcluster
"""

Q_CLUSTER = {
    'name': 'lex_chambers',
    'workers': 2,
    'recycle': 500,
    'timeout': 60,
    'compress': True,
    'save_limit': 250,
    'queue_limit': 500,
    'cpu_affinity': 1,
    'label': 'Django Q',
    'orm': 'default',  # Use Django ORM broker (no Redis required by default)
    # To use Redis instead:
    # 'redis': {
    #     'host': 'localhost',
    #     'port': 6379,
    #     'db': 0,
    # },
}
