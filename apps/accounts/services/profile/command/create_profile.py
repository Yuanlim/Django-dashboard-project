from typing import Any, TypedDict
from rest_framework import status

from apps.accounts.domain.enums.risk_level import RiskLevel
from apps.accounts.domain.types.profile import CreateProfileInput
from apps.accounts.models.profile import Profile
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
        self.first_name = info["first_name"]
        self.middle_name = info["middle_name"]
        self.last_name = info["last_name"]
        self.gender = info["gender"]
        self.nationality = info["nationality"]
        self.birth_date = info["birth_date"]
        self.phone_number = info["phone_number"]
        self.skills = info["skills"]
        
        # Injected service
        self.country_service = country_service
        self.skill_create_service = skill_create_service
        self.skill_search_service = skill_search_service
        
    def create(self):
        
        # Search country
        country = self.country_service.search_by_name(name=self.nationality)
        if country is None:
            self.service_result = {
                "error": True,
                "to_logger": "",
                "risk_level": RiskLevel.NONE,
                "client_response": "Unknown country, email to admin if you think it was an mistake.",
                "from_service": "Create Profile",
                "response_status": status.HTTP_404_NOT_FOUND
            }
        
        # Search for skill if not create one
        skillList = []
        
        for s in self.skills:
            skill = self.skill_search_service.search_by_name(name=s)
            
            if skill is None:
                skillList.append(self.skill_create_service.create_skill(name=s))
            
        