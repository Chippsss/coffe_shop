from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = "Create default user roles for the coffee shop app"

    def handle(self, *args, **kwargs):
        roles = ["Customer", "Staff", "Delivery"]
        for role in roles:
            group, created = Group.objects.get_or_create(name=role)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created group: {role}"))
            else:
                self.stdout.write(f"Group {role} already exists.")
