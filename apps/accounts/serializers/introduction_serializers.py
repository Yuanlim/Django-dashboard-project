### A serializers is the one who did validations and transform
from rest_framework import serializers
from ..models.introduction import Introduction


class IntroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Introduction
        fields = ["intro", "roles"]
