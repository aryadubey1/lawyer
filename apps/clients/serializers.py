from rest_framework import serializers
from .models import ClientLogo


class ClientLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientLogo
        fields = ['id', 'name', 'logo', 'logo_alt', 'url', 'order']
