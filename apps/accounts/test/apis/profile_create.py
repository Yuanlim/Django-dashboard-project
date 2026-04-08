import json
from typing import Any, cast

from rest_framework.test import APITestCase
from rest_framework.response import Response
from rest_framework import status
from apps.accounts.management.commands.setup_school import SCHOOL_I_KNOW

from apps.accounts.models.skill import Skill
from apps.accounts.serializers.profile_serializers import ProfileSerializers
from apps.accounts.serializers.skill_serializers import SkillSearchSerializers
from apps.accounts.services.profile.command.create_profile import CreateProfileCommand

class CreateProfile(APITestCase):
    """
    Ensure create profile is possible.
    """
    
    with open('../json/profile_example.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    profile_info = data["info"]
    serializer = ProfileSerializers(data=profile_info)
    serializer.is_valid(raise_exception=True)
    
    validated_info = cast(dict[str, Any], serializer.validated_data)
    service = CreateProfileCommand(validated_info)
    
    
    
    