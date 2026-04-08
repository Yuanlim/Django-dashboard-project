from typing import Optional

from apps.accounts.models.skill import Skill

class CreateSkillCommand:
    
    def __init__(self, skill_name: str):
        self.skill_name = skill_name
        self.skill_obj: Optional[Skill] = None
        self.skill_pk: Optional[int] = None
        
    def create_skill(self):
        # TODO: black-list cant be created
        
        self.skill_obj = Skill.objects.create(name=self.skill_name, verified=False)
        self.skill_pk = self.skill_obj.pk
        return