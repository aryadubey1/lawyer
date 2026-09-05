from rest_framework import viewsets
from .models import ClientLogo
from .serializers import ClientLogoSerializer


class ClientLogoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClientLogo.objects.all().order_by('order')
    serializer_class = ClientLogoSerializer
