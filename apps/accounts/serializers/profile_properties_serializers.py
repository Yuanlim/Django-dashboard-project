from rest_framework import serializers


class EducationSerializers(serializers.ModelSerializer):

    class Meta:
        fields = ["degree", "other_degree"]

    def validation(self, values):
        """
        A validator that checks when degree is in selection of
        "other", it suppose to have an other degree description

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        degree = values.get("degree", getattr(self.instance, "degree", None))
        other_degree = values.get(
            "other_degree", getattr(self.instance, "degree", None)
        )

        if degree == "other" and not other_degree:
            raise serializers.ValidationError(
                {
                    "other_degree": "When select other degree user needs to have other degree description"
                }
            )

        return values


class AchievementSerializers(serializers.ModelSerializer):

    class Meta:
        fields = ["title", "task_description", "contribution_description"]


class CourseSerializers(serializers.ModelSerializer):

    class Meta:
        fields = ["name"]


class SchoolSerializers(serializers.ModelSerializer):

    class Meta:
        fields = ["name"]


class CountrySerializers(serializers.ModelSerializer):

    class Meta:
        fields = ["name"]


class EducationCourse(serializers.ModelSerializer):

    class Meta:
        fields = ["course_description"]
