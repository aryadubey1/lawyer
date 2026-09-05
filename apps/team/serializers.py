from rest_framework import serializers
from .models import TeamMember


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['id', 'name', 'designation', 'bio', 'photo', 'photo_alt', 'is_founder', 'linkedin_url', 'order']
