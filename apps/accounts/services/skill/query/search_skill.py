from apps.accounts.models.skill import Skill
from apps.accounts.services.base import ServiceBase


class SearchSkill(ServiceBase[Skill]):
    
    def __init__(self):
        super().__init__(Skill, "Search Skill")
        
    def search_by_name(self, name):
        self.obj = Skill.objects.filter(name__iexact=name).first()
        
        if self.obj is not None:
            self.success_result()
        else:
            self.search_name_404_result(
                search_keyword=name,
                additional_msg="Email to admin if you think it was an mistake."
            )
            
        return self.service_result
    
    def search_by_pk(self, pk: int):
        self.obj = Skill.objects.filter(pk=pk).first()
        
        if self.obj is not None:
            self.success_result()
        else:
            self.search_pk_404_result(pk=pk)
            
        return self.service_result