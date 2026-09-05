"""
Context processor: injects active practice areas into every template.
Used for the dynamic Practice Areas dropdown in the navbar.
"""
from apps.practice_areas.models import PracticeArea


def practice_areas_processor(request):
    """Provide practice areas for the navbar dropdown."""
    return {
        'nav_practice_areas': PracticeArea.objects.filter(is_active=True).order_by('order'),
    }
