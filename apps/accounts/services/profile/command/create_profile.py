from typing import Any

from apps.accounts.serializers.profile_serializers import ProfileSerializers
from apps.accounts.services.profile_properties.command.create_country import CreateCountryCommand
from apps.accounts.services.profile_properties.query.get_country import GetCountryQuery


class CreateProfileCommand:
    
    def __init__(self, info: dict[str, Any]):
        self.first_name = info.get("first_name")
        self.middle_name = info.get("middle_name", None)
        self.last_name = info.get("last_name")
        self.gender = info.get("gender")
        self.nationality = info.get("nationality")
        self.birth_date = info.get("birth_date", None)
        self.phone_number = info.get("phone_number", None)
        self.skills = info.get("skills", None)
        
    def create(self):
        
        # Search country if not create one
        country_pk = GetCountryQuery(name=self.nationality).country_pk
        
        if country_pk is None:
            country_pk = CreateCountryCommand(name=self.nationality).country_pk
        