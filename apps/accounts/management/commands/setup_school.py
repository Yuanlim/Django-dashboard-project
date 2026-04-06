SCHOOL_I_KNOW = [
    "National Kaohsiung University of Science and Technology", 
    "Massachusetts Institute of Technology", 
    "University of Oxford", "University of Cambridge", 
    "Harvard University", 
    "Imperial College London", 
    "National Taiwan University", 
    "National Tsing Hua University", 
    "National Central University"
]

from django.core.management.base import BaseCommand, CommandError
from apps.accounts.models.profile_properties import School

class Command(BaseCommand):
    help = "Create initial School data"

    def handle(self, *args, **options):
        for s in SCHOOL_I_KNOW:
            try:
                # Inserting new skill
                School.objects.get_or_create(name=s, verified=True)
            except Exception as e:
                # When insert something happened
                raise CommandError(e)