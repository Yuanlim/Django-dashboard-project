from typing import Optional

from apps.accounts.models.profile_properties import Country
from apps.accounts.services.profile_properties.base.country_base import CountryCommandBase


class GetCountryQuery(CountryCommandBase):
    
    def __init__(self, name):
        super.__init__(name)
        
    def search(self):
        # Get skill from dataset
        self.country_obj = Country.objects.filter(name__iexact=self.name).first()
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