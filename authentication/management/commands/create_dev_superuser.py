from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os


class Command(BaseCommand):
    help = 'Create a superuser if not exists (for dev only)'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@gmail.com")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "1234")

        if not User.objects.filter(username=username).exists():
            self.stdout.write("Creating dev superuser...")
            User.objects.create_superuser(
                username=username, email=email, password=password)
        else:
            self.stdout.write("Superuser already exists. Skipping...")
