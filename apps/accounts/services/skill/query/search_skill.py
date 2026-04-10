from apps.accounts.models.skill import Skill
from apps.accounts.services.base import ServiceBase


class SearchSkill(ServiceBase[Skill]):
    
    def __init__(self):
        super().__init__()
        
    def search_by_name(self, name):
        self.obj = Skill.objects.filter(name__iexact=name).first()
        return self.obj
    
    def search_by_pk(self, pk: int):
        self.obj = Skill.objects.filter(pk=pk).first()
        return self.obj