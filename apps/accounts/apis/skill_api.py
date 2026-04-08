from typing import Optional

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.accounts.models.skill import Skill
from apps.accounts.serializers.skill_serializers import SkillSearchSerializers

class SkillSearchAndInsert(APIView):
    """
    Show matched skill id relative to database, 
    if not created and response with the ids.

    * Requires token authentication. (WIP)
    * All roles can visit this endpoint.
    """
    
    def check_existed(self, skill_name) -> Optional[int]:
        # Get skill from dataset
        skill = Skill.objects.filter(name__iexact=skill_name).first()
        
        # Check existed
        if skill is None:
            return None
            
        return skill.pk


    def post(self, request, format=None):
        """
        return matched skill id
        """
        
        # validate skill request
        serializer = SkillSearchSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
        # Extract skill name
        skill_name = request.data.get("name")
        
        # Get the id
        skill_id = self.check_existed(skill_name=skill_name)
        
        if skill_id is None:
            # Create new skill in database
            # TODO: later should have created by who
            skill = Skill.objects.create(name=skill_name, verified=False)

            return  Response(
                {"id": skill.pk},
                status=status.HTTP_201_CREATED
            )
            
        else:
            return  Response(
                {"id": skill_id},
                status=status.HTTP_200_OK
            )