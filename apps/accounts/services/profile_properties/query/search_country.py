from apps.accounts.models.profile_properties import Country
from apps.accounts.services.base import ServiceBase


class SearchCountry(ServiceBase[Country]):
    
    def __init__(self):
        super().__init__()
        
    def search_by_name(self, name):
        self.obj = Country.objects.filter(name__iexact=name).first()
        return self.obj
    
    def search_by_pk(self, pk: int):
        self.obj = Country.objects.filter(pk=pk).first()
        return self.obj