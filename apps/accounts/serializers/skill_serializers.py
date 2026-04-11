from rest_framework import serializers

from apps.accounts.models.skill import Skill

class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ["name"]
        
        
class SkillSearchSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200, allow_blank=False)