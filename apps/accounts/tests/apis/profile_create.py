import json
from typing import cast

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from apps.accounts.serializers.profile_serializers import ProfileSerializer
from apps.accounts.services.profile.command.create_profile import CreateProfileCommand, CreateProfileInput
from apps.accounts.services.profile_properties.query.search_country import SearchCountry
from apps.accounts.services.skill.command.create_skill import CreateSkill
from apps.accounts.services.skill.query.search_skill import SearchSkill

class ProfileTests(APITestCase):
    
    def test_create_profile(self):
        """
        Ensure create profile is possible.
        """
        
        with open('../json/profile_example.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        profile_info = data["info"]
        serializer = ProfileSerializer(data=profile_info)
        
        if serializer.is_valid(raise_exception=True):
            response = self.client.post("api/test/profile-create", data=profile_info, format='json')
        
        validated_info = cast(CreateProfileInput, serializer.validated_data)
        
        profile = CreateProfileCommand(
            validated_info, 
            country_service=SearchCountry(), 
            skill_create_service=CreateSkill(),
            skill_search_service=SearchSkill()
        ).create()
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        if profile is None:
            self.fail("Profile creation returned None")
            
        self.assertEqual(profile.user.username, "Bot!!!")
        self.assertEqual(profile.user.email, "bot123@gmail.com")
        self.assertTrue(profile.user.check_password("helloworld"))
        self.assertEqual(profile.first_name, "123")
        self.assertEqual(profile.last_name, "123 Bot")
        self.assertEqual(profile.gender, "male")
        self.assertEqual(profile.nationality, "Chad")
        self.assertEqual(profile.phone_number, "00000000")
        self.assertEqual(
            [skill.name for skill in profile.skills.all()], 
            ["python", "database", "django", "back-end development"]
        )