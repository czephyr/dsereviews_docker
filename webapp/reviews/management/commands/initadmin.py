import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            User.objects.create_superuser(
                email=os.environ.get("ADMIN_EMAIL"),
                username=os.environ.get("ADMIN_USERNAME"),
                password=os.environ.get("ADMIN_PASSWORD"),
            )
            self.stdout.write("Created admin superuser with environment credentials")
        else:
            self.stdout.write(
                "Admin accounts can only be initialized if no Accounts exist"
            )
