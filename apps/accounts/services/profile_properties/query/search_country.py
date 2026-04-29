from apps.accounts.domain.types.service import ServiceResultType
from apps.accounts.models.profile_properties import Country
from apps.accounts.services.base import ServiceBase

class SearchCountry(ServiceBase[Country]):
    
    def __init__(self):
        super().__init__(Country, "Search Country")
        
    def search_by_name(self, name) -> ServiceResultType[Country]:
        self.obj = Country.objects.filter(name__iexact=name).first()
        
        if self.obj is not None:
            self.success_result()
        else:
            self.search_name_404_result(
                search_keyword=name, 
                additional_msg="Email to admin if you think it was an mistake."
            )
            
        return self.service_result
    
    def search_by_pk(self, pk: int) -> ServiceResultType[Country]:
        self.obj = Country.objects.filter(pk=pk).first()
        
        if self.obj is not None:
            self.success_result()
        else:
            self.search_pk_404_result(pk=pk)
        
        return self.service_result