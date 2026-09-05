"""
Management command: python manage.py seed_db
Loads all JSON fixtures idempotently, ensures SiteConfig & AboutPage singletons,
creates flat pages (Privacy Policy, Disclaimer, Terms), and creates a default superuser if none exists.
"""
import os
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.contrib.flatpages.models import FlatPage
from django.conf import settings

User = get_user_model()


class Command(BaseCommand):
    help = 'Seeds database with initial dummy content, flatpages, and creates a default superuser.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING('=== Starting Subhash Mishra & Associates DB Seeding ==='))

        fixtures_dir = os.path.join(settings.BASE_DIR, 'fixtures')
        fixture_files = [
            'site_config.json',
            'about_page.json',
            'practice_areas.json',
            'team.json',
            'blog_posts.json',
            'gallery.json',
            'clients.json',
        ]

        # 1. Load Fixtures
        for fixture in fixture_files:
            fixture_path = os.path.join(fixtures_dir, fixture)
            if os.path.exists(fixture_path):
                self.stdout.write(f'Loading fixture: {fixture}...')
                try:
                    call_command('loaddata', fixture_path)
                    self.stdout.write(self.style.SUCCESS(f'✓ Successfully loaded {fixture}'))
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f'Notice loading {fixture}: {e}'))
            else:
                self.stdout.write(self.style.WARNING(f'Fixture file not found: {fixture_path}'))

        # 2. Setup Default Site
        current_site, _ = Site.objects.get_or_create(id=1, defaults={
            'domain': 'localhost:8000',
            'name': 'Subhash Mishra & Associates',
        })
        current_site.domain = 'localhost:8000'
        current_site.name = 'Subhash Mishra & Associates'
        current_site.save()
        self.stdout.write(self.style.SUCCESS('✓ Site configured for localhost:8000'))

        # 3. Create Default Legal Flatpages
        flatpages_data = [
            {
                'url': '/pages/privacy-policy/',
                'title': 'Privacy Policy',
                'content': '<h2>Privacy Policy</h2><p>Subhash Mishra & Associates is committed to safeguarding personal and confidential data in compliance with the Digital Personal Data Protection Act, 2023 (DPDP) and applicable Bar Council of India guidelines. Communications through this website are encrypted and strictly confidential.</p>',
            },
            {
                'url': '/pages/disclaimer/',
                'title': 'Disclaimer',
                'content': '<h2>Bar Council of India Disclaimer</h2><p>As per the rules of the Bar Council of India, lawyers and law firms are not permitted to solicit work or advertise. By accessing this website, the user acknowledges that they are seeking information relating to Subhash Mishra & Associates of their own accord and that there has been no form of solicitation, advertisement or inducement by Subhash Mishra & Associates or its members.</p>',
            },
            {
                'url': '/pages/terms/',
                'title': 'Terms of Use',
                'content': '<h2>Terms of Use</h2><p>The information provided on this website does not constitute legal advice. Visiting this website or communicating through the contact form does not create an advocate-client relationship until a formal engagement letter is executed.</p>',
            },
        ]

        for fp_info in flatpages_data:
            fp, created = FlatPage.objects.get_or_create(
                url=fp_info['url'],
                defaults={
                    'title': fp_info['title'],
                    'content': fp_info['content'],
                }
            )
            if (not created) and 'Lex Chambers' in (fp.content or ''):
                fp.content = fp_info['content']
                fp.title = fp_info['title']
                fp.save()
            fp.sites.add(current_site)
            fp.save()
            status_text = 'Created' if created else 'Already exists'
            self.stdout.write(self.style.SUCCESS(f'✓ Flatpage {fp_info["url"]} ({status_text})'))

        # 4. Create Default Superuser if none exists
        if not User.objects.filter(is_superuser=True).exists():
            admin_username = 'admin'
            admin_email = 'admin@lexchambers.in'
            admin_password = 'adminpassword123'
            User.objects.create_superuser(
                username=admin_username,
                email=admin_email,
                password=admin_password,
            )
            self.stdout.write(self.style.SUCCESS(
                f'✓ Created default superuser:\n'
                f'   Username: {admin_username}\n'
                f'   Password: {admin_password}\n'
                f'   Email:    {admin_email}'
            ))
        else:
            self.stdout.write(self.style.SUCCESS('✓ Superuser already exists.'))

        self.stdout.write(self.style.MIGRATE_HEADING('=== DB Seeding Complete! ==='))
