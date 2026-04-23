from apps.accounts.models.skill import Skill
from apps.accounts.services.base import ServiceBase

from django.contrib.auth.models import User

class CreateSkill(ServiceBase[Skill]):
    
    def __init__(self):
        super().__init__()
        
    def create_skill(self, name, user: User):
        # TODO: black-list cant be created
        
        # PROBLEM: Profile must created before handle skills
        self.obj = Skill.objects.create(name=name, created_by=user, verified=False)
        return self.obj