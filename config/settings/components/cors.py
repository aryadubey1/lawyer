"""
CORS configuration for Lex Chambers.
Public read-only API — allows all origins for safe methods.
POST to /api/v1/contact/ is also open for the contact form.
"""

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'HEAD',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# For production, restrict to your domain:
# CORS_ALLOWED_ORIGINS = [
#     "https://lexchambers.in",
#     "https://www.lexchambers.in",
# ]
