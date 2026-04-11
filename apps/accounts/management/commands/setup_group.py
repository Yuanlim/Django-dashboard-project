ROLES_I_KNOWN = [
    "Full-stack Developer",
    "Back-end Developer",
    "Front-end Developer",
    "Web Developer",
    "IoT Engineer",
    "UX/UI Designer",
    "Software Engineer"
]

from django.core.management.base import BaseCommand, CommandError
from apps.accounts.models.introduction import RoleTag

class Command(BaseCommand):
    help = "Create initial Role Tag data"

    def handle(self, *args, **options):
        for r in ROLES_I_KNOWN:
            try:
                # Inserting new skill
                RoleTag.objects.get_or_create(title=r, verified=True)
            except Exception as e:
                # When insert something happened
                raise CommandError(e)