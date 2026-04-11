from rest_framework import serializers
from ..models.project import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["title", "starting_date", "ending_date", "skills"]

    def validate(self, values):
        starting_date = values.get("starting_date")
        ending_date = values.get("ending_date")

        # validate both date exist
        # if exist validate if starting is later than ending
        # if so it is invalid
        if starting_date and ending_date and starting_date > ending_date:
            raise serializers.ValidationError(
                {
                    "ending_date": "Ending date must be later than or equal to starting date"
                }
            )

        return values
