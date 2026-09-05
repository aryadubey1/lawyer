"""
DRF API view for contact form submissions.
POST /api/v1/contact/ — creates a submission and enqueues Telegram notification.
"""
import logging
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django_q.tasks import async_task

from .models import ContactSubmission
from .serializers import ContactSubmissionSerializer

logger = logging.getLogger(__name__)


class ContactCreateAPIView(generics.CreateAPIView):
    """
    POST endpoint for headless / SPA contact form submissions.
    Returns 201 on success. Telegram notification is async.
    """
    serializer_class = ContactSubmissionSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        submission = serializer.save()
        logger.info(f'API contact submission #{submission.pk} from {submission.email}')
        try:
            async_task(
                'apps.contact.tasks.send_telegram_notification',
                submission.pk,
            )
        except Exception as e:
            logger.error(f'Failed to enqueue Telegram task from API: {e}')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {'detail': 'Your message has been received. We will get back to you shortly.'},
            status=status.HTTP_201_CREATED,
        )
