from typing import Optional

from apps.accounts.models.profile_properties import Country


class CountryCommandBase:
    
    def __init__(self, name):
        self.name = name
        self.country_obj: Optional[Country] = None