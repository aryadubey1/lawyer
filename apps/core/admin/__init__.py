# apps/core/admin/__init__.py
from .homepage_admin import HeroSlideAdmin
from .site_config_admin import SiteConfigAdmin

__all__ = ['SiteConfigAdmin', 'HeroSlideInline']
