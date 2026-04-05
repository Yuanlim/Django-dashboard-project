import pycountry
import phonenumbers

from django.core.management.base import BaseCommand, CommandError
from apps.accounts.models.profile_properties import Country

class Command(BaseCommand):
    help = "Create initial Country data with its country code"

    def handle(self, *args, **options):
        for c in pycountry.countries:
            try:
                name = c.name
                alpha_2 = c.alpha_2
                code = phonenumbers.country_code_for_valid_region(alpha_2)
                
                # Inserting new country and its country code
                Country.objects.get_or_create(name=name, country_code=code)
            except Exception as e:
                # Not valid
                print(f"Skipped: {c.name}, {c.alpha_2}, {e}")
                
