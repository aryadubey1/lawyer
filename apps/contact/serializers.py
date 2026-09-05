from rest_framework import serializers
from .models import ContactSubmission


class ContactSubmissionSerializer(serializers.ModelSerializer):
    """
    Public API serializer for contact form submissions.
    Excludes internal admin-only fields (is_read, telegram_sent).
    """
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'phone', 'subject', 'message']
