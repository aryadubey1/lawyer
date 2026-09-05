from django.views.generic import TemplateView
from .models import GalleryImage


class GalleryView(TemplateView):
    template_name = 'gallery/gallery.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['gallery_images'] = GalleryImage.objects.all().order_by('order')
        ctx['categories'] = GalleryImage.CATEGORY_CHOICES
        return ctx
