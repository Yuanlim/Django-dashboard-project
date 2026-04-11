from rest_framework import status
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password

from apps.accounts.domain.enums.risk_level import RiskLevel
from apps.accounts.domain.types.profile import CreateProfileInput
from apps.accounts.models.profile import Profile
from apps.accounts.serializers.user_serializers import UserSerializer
from apps.accounts.services.base import ServiceBase
from apps.accounts.services.profile_properties.query.search_country import SearchCountry
from apps.accounts.services.skill.command.create_skill import CreateSkill
from apps.accounts.services.skill.query.search_skill import SearchSkill


class CreateProfileCommand(ServiceBase[Profile]):
    
    def __init__(
            self, 
            info: CreateProfileInput, 
            country_service: SearchCountry, 
            skill_create_service: CreateSkill,
            skill_search_service: SearchSkill
        ):
        # Create user info
        self.info = info
        
        # Injected service
        self.country_service = country_service
        self.skill_create_service = skill_create_service
        self.skill_search_service = skill_search_service
        
    def create(self):
        
        # Search country
        self.nationality = self.country_service.search_by_name(name=self.info["nationality"])
        if self.nationality is None:
            self.service_result = {
                "error": True,
                "to_logger": "",
                "risk_level": RiskLevel.NONE,
                "client_response": "Unknown country, email to admin if you think it was an mistake.",
                "from_service": "Create Profile",
                "response_status": status.HTTP_404_NOT_FOUND
            }
            return
        
        # Search for skill if not create one
        skillList = []
        
        for s in self.info["skills"]:
            skill = self.skill_search_service.search_by_name(name=s)
            
            if skill is None:
                skillList.append(self.skill_create_service.create_skill(name=s))
                
        self.info["skills"] = skillList
        
        # Make User but make sure there is no same user
        
        # All user should be regular unless TODO: proven
        serializer = UserSerializer(data=self.info)
        
        if not serializer.is_valid(raise_exception=True):
            self.service_result = {
                "error": True,
                "to_logger": "",
                "risk_level": RiskLevel.NONE,
                "client_response": "Create user properties error",
                "from_service": "Create Profile",
                "response_status": status.HTTP_400_BAD_REQUEST
            }
            return
        
        # hash password
        self.info["password"] = make_password(self.info["password"])
        
        # get group regular
        regular_group = Group.objects.get(name__iexact="regular")
        
        # create user
        user = User.objects.create(**self.info, group=regular_group)
        
        # create profile
        profile = Profile.objects.create(**self.info, user=user)
        
        return profile