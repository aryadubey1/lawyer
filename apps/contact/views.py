"""
Contact page views — renders form and handles POST.
Async Telegram notification is enqueued via django-q2 (never blocks the HTTP response).
"""
import logging
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django_q.tasks import async_task

from .forms import ContactForm

logger = logging.getLogger(__name__)


class ContactView(View):
    template_name = 'contact/contact.html'

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            submission = form.save()
            logger.info(f'New contact submission #{submission.pk} from {submission.email}')

            # Enqueue async Telegram notification — never blocks the HTTP response
            try:
                async_task(
                    'apps.contact.tasks.send_telegram_notification',
                    submission.pk,
                )
                logger.debug(f'Telegram task enqueued for submission #{submission.pk}')
            except Exception as e:
                logger.error(f'Failed to enqueue Telegram task: {e}')

            return redirect('contact:success')

        return render(request, self.template_name, {'form': form})


class ContactSuccessView(View):
    template_name = 'contact/contact_success.html'

    def get(self, request):
        return render(request, self.template_name)
