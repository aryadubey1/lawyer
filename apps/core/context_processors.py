"""
Context processor: injects SiteConfig singleton into every template context.
Usage in templates: {{ site_config.firm_name }}, {{ site_config.phone_primary }}, etc.
"""
from apps.core.models.site_config import SiteConfig


def site_config_processor(request):
    """Make the SiteConfig singleton available in all templates."""
    return {
        'site_config': SiteConfig.get_solo(),
    }
