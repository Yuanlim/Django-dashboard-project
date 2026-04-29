from apps.accounts.domain.enums.risk_level import RiskLevel
from apps.accounts.domain.types.service import ServiceResultType
from apps.accounts.models.skill import Skill
from apps.accounts.services.base import ServiceBase

from rest_framework import status

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CreateSkill(ServiceBase[Skill]):
    
    def __init__(self):
        super().__init__(Skill, "Create Skill")
        
    def create_skill(self, name, user: User) -> ServiceResultType[Skill]:
        # TODO: black-list cant be created
        
        # PROBLEM: Profile must created before handle skills
        self.obj = Skill(name=name, created_by=user, verified=False)
        
        try:
            self.obj.full_clean()
            self.obj.save()
        except ValidationError as e:
            self.error_to_result(
                e, 
                risk_level=RiskLevel.NONE, 
                response_status=status.HTTP_400_BAD_REQUEST
            )
            return self.service_result
        
        self.success_result()
        return self.service_result