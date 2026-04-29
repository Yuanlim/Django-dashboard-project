from datetime import date
import json
import profile
from typing import List, cast

from django.test import TestCase
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError

from apps.accounts.domain.types.profile import CreateProfileInput
from apps.accounts.domain.validator.user import UserExtraValidator
from apps.accounts.models.profile_properties import Country, Gender
from apps.accounts.models.skill import Skill
from apps.accounts.services.profile.command.create_profile import CreateProfileCommand
from apps.accounts.services.profile_properties.query.search_country import SearchCountry
from apps.accounts.services.skill.command.create_skill import CreateSkill
from apps.accounts.services.skill.query.search_skill import SearchSkill
from apps.accounts.tests.services.base import TestServiceBase
from core.settings import BASE_DIR


class CreateProfileTest(TestCase, TestServiceBase):
    
    def setUp(self):
        # invalid test case nationality cant all be invalid/valid
        # manually create valid ones
        more_country = ["Philippines"]
        for c in more_country:
            Country.objects.get_or_create(name=c, country_code=0)
        
        country_search_service = SearchCountry()
        skill_search_service = SearchSkill()
        skill_create_service = CreateSkill()
        user_validator = UserExtraValidator()
        Group.objects.create(name="regular")
        
        self.data: List[CreateProfileInput] = []
        self.services: List[CreateProfileCommand] = []

        with open(f"{BASE_DIR}" + "/apps/accounts/tests/json/profile_info.json", "r", encoding="utf-8") as file:
            valid_json_data = json.load(file)
            
            for i, j in enumerate(valid_json_data):
                self.data.append(cast(CreateProfileInput, j["info"]))
                
                Country.objects.get_or_create(name=self.data[i]["nationality"], country_code=0)
                
                for skill in self.data[i]["skills"]:
                    Skill.objects.get_or_create(name=skill)
                
                self.services.append(CreateProfileCommand(
                    self.data[i], 
                    country_search_service,
                    skill_create_service,
                    skill_search_service,
                    user_validator
                ))
                
        self.invalid_data: List[CreateProfileInput] = []
        self.invalid_services: List[CreateProfileCommand] = []
        
        with open(f"{BASE_DIR}" + "/apps/accounts/tests/json/profile_invalid_example.json", "r", encoding="utf-8") as file:
            invalid_json_data = json.load(file)
            
            for i, j in enumerate(invalid_json_data):
                self.invalid_data.append(cast(CreateProfileInput, j["info"]))
                
                self.invalid_services.append(CreateProfileCommand(
                    self.invalid_data[i], 
                    country_search_service,
                    skill_create_service,
                    skill_search_service,
                    user_validator
                ))
                
                
    def test_create_profile_valid(self):
        
        for i, service in enumerate(self.services):
            print(f"curr: {self.data[i]["username"]}")
            result = service.create()
            profile = result["obj"]
            
            self.assertEqual(result["error"], False)
            self.assertIsNotNone(profile)
            if profile is None:
                self.fail(self.create_report(self.data[i]))
            self.assertEqual(profile.user.first_name, self.data[i]["first_name"])
            self.assertEqual(profile.user.last_name, self.data[i]["last_name"])
            self.assertEqual(profile.user.username, self.data[i]["username"])
            self.assertEqual(profile.user.email, self.data[i]["email"])
            self.assertTrue(check_password(self.data[i]["password"], profile.user.password))
            self.assertEqual(profile.gender, self.data[i]["gender"])
            self.assertEqual(profile.nationality.name, self.data[i]["nationality"])
            self.assertEqual(profile.user.email, self.data[i]["email"])
            self.assertCountEqual(
                [skill.name for skill in profile.skills.all()],
                self.data[i]["skills"]
            )
            
            linkedIn = self.data[i].get("linkedIn")
            github = self.data[i].get("github")
            if linkedIn is not None:
                self.assertEqual(profile.linkedIn, linkedIn)
            if github is not None:
                self.assertEqual(profile.github, github)
                
            phone_number = self.data[i].get("phone_number")
            if phone_number is not None:
                self.assertEqual(profile.phone_number, self.data[i]["phone_number"])
                
            birth_date = self.data[i].get("birth_date")
            if birth_date is not None:
                self.assertEqual(profile.birth_date, date.fromisoformat(birth_date))
            
            
    def test_create_profile_invalid(self):
        
        for i, service in enumerate(self.invalid_services):
            print(f"curr: {self.invalid_data[i]["username"]}")
            result = service.create()
            
            # invalid test could only be error case
            self.assertEqual(result["error"], True)
            self.assertEqual(result["obj"], None)
            print(result["client_response"][0])