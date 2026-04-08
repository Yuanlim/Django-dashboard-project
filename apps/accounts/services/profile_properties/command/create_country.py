from typing import Optional

from apps.accounts.models.profile_properties import Country
from apps.accounts.services.profile_properties.base.country_base import CountryCommandBase


class CreateCountryCommand(CountryCommandBase):
    
    def __init__(self, name):
        super.__init__(name)
        
    def create(self):
        # Get skill from dataset
        self.country_obj = Country.objects.create(name=self.name)
        return
    
    @property
    def country_code(self) -> Optional[str]:
        if self.country_obj is not None:
            return self.country_obj.country_code 
        
        return None;
    
    @property
    def country_pk(self) -> Optional[int]:
        if self.country_obj is not None:
            return self.country_obj.pk
        
        return None;