from rest_framework import serializers

from apps.accounts.models.skill import Skill

class SkillSerializers(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ["name"]