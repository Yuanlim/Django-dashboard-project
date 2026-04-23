# run once py
from django.contrib.auth.models import Group

HAD_GROUP = ["OWNER", "COMPANY", "PREMIUM", "REGULAR"]

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Create initial Group"

    def handle(self, *args, **options):
        for role in HAD_GROUP:
            Group.objects.get_or_create(name=role)