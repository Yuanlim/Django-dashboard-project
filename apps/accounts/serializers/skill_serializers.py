from rest_framework import serializers

from apps.accounts.models.skill import Skill

class SkillSerializers(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ["name"]
        
        
class SkillSearchSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=200, allow_blank=False)