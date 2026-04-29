from typing import List

from rest_framework import status
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.core.exceptions import ValidationError

from apps.accounts.domain.enums.risk_level import RiskLevel
from apps.accounts.domain.types.profile import CreateProfileInput
from apps.accounts.domain.types.service import ServiceResultType
from apps.accounts.domain.validator.user import UserExtraValidator
from apps.accounts.models.profile import Profile
from apps.accounts.models.skill import Skill
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
            skill_search_service: SearchSkill,
            user_validator: UserExtraValidator
        ):

        # initialize ServiceBase
        super().__init__(Profile, "Create Profile")
        
        # Create user info
        self.info = info
        
        # Injected service
        self.country_service = country_service
        self.skill_create_service = skill_create_service
        self.skill_search_service = skill_search_service
        self.user_validator = user_validator
        
    def create(self) -> ServiceResultType[Profile]:

        # Search country
        nat_result = self.country_service.search_by_name(name=self.info.get("nationality"))
        nat = nat_result["obj"]
        if nat is None:
            print("Nat search error")
            # create result again for Type correction: ServiceResultType[Country] -> ServiceResultType[Profile]
            self.service_result = {
                "error": True,
                "to_logger": nat_result["to_logger"],
                "risk_level": nat_result["risk_level"],
                "client_response": nat_result["client_response"],
                "from_service": self.service_name,
                "response_status": nat_result["response_status"],
                "obj": None,
            }
            return self.service_result
        
        # get group regular
        regular_group = Group.objects.get(name__iexact="regular")
        
        # create user
        user = User(
            username=self.info.get("username", ""),
            first_name=self.info.get("first_name", ""),
            last_name=self.info.get("last_name", ""),
            email=self.info.get("email", ""),
            password=make_password(self.info.get("password")), # hash password
            date_joined=timezone.now(),
        )
        
        # validate created user
        try:
            self.user_validator.validate(
                first_name=self.info.get("first_name", None),
                last_name=self.info.get("last_name", None),
                password=self.info.get("password"),
                email=self.info.get("email")
            )
            user.full_clean()
            user.save()
        except ValidationError as e:
            print("User create error")
            self.error_to_result(e, 
                risk_level=RiskLevel.NONE, 
                response_status=status.HTTP_400_BAD_REQUEST
            )
            return self.service_result
        
        user.groups.set([regular_group])
        
        # Search for skill if not create one
        skillList: List[Skill] = []
        
        for s in self.info.get("skills", []):
            s_result = self.skill_search_service.search_by_name(name=s)
            skill_obj = s_result["obj"]
            
            if skill_obj is None:
                s_result = self.skill_create_service.create_skill(name=s, user=user)
                skill_obj = s_result["obj"]
                
                if skill_obj is None:
                    print("Skill create error")
                    self.service_result = {
                        "error": True,
                        "to_logger": s_result["to_logger"],
                        "risk_level": s_result["risk_level"],
                        "client_response": s_result["client_response"],
                        "from_service": self.service_name,
                        "response_status": s_result["response_status"],
                        "obj": None,
                    }
                    
                    return self.service_result
            
            skillList.append(skill_obj)
        
        # create profile
        self.obj = Profile(
            birth_date=self.info.get("birth_date"),
            nationality=nat,
            phone_number=self.info.get("phone_number"),
            gender=self.info.get("gender"),
            user=user,
            linkedIn=self.info.get("linkedIn"),
            github=self.info.get("github")
        )
        
        # validate created profile
        try:
            self.obj.full_clean()
            self.obj.save()
        except ValidationError as e:
            print("Profile create error")
            self.error_to_result(e, 
                risk_level=RiskLevel.NONE, 
                response_status=status.HTTP_400_BAD_REQUEST
            )
            return self.service_result
        
        # many to many fields need to be assign separately
        self.obj.skills.set(skillList)
        
        # default service_result
        self.success_result()
        
        return self.service_result