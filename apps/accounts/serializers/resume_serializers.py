from rest_framework import serializers
from ..models.resume import Resume


class ResumeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Resume
        fields = ["created_datetime", "the_file"]
