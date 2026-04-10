from typing import Optional

from apps.accounts.models.skill import Skill
from apps.accounts.services.base import ServiceBase

class CreateSkill(ServiceBase[Skill]):
    
    def __init__(self):
        super().__init__()
        
    def create_skill(self, name):
        # TODO: black-list cant be created
        
        self.obj = Skill.objects.create(name=name, verified=False)
        return self.obj