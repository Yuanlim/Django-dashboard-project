from datetime import date

from rest_framework import serializers

from apps.accounts.models.profile_properties import Achievement, Country, Course, Education, EducationCourse, School


class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = ["degree", "other_degree", "starting_date", "ending_date", "graduated"]

    def validate(self, values):
        """
        A validator that checks: 
        1. When degree is in selection of "other", it suppose to have an other degree description.
        2. When not graduated, there is no ending date. However, if graduated there is a ending date.
        3. Starting_date should not be before ending_date. Starting date is not future date.
        """
        
        # First validation
        degree = values.get("degree", getattr(self.instance, "degree", None))
        other_degree = values.get(
            "other_degree", getattr(self.instance, "other_degree", None)
        )

        if degree == "other" and not other_degree:
            raise serializers.ValidationError(
                {
                    "other_degree": "When select other degree user needs to have other degree description."
                }
            )
            
        # Second validation
        graduated = values.get("graduated", getattr(self.instance, "graduated", False))
        ending_date = values.get("ending_date", getattr(self.instance, "ending_date", None))
        
        if graduated and ending_date is None:
            raise serializers.ValidationError(
                {
                    "ending_date": "When select graduated user should insert ending_date."
                }
            )
            
        elif not graduated and ending_date is not None:
            raise serializers.ValidationError(
                {
                    "ending_date": "When graduated is not selected, user should not insert ending_date."
                }
            )

        # Third validation
        
        # Today
        today = date.today()
        starting_date = values.get("starting_date", getattr(self.instance, "starting_date"))
        
        if starting_date > today:
            raise serializers.ValidationError(
                {
                    "starting_date": "Starting date should not be future date."
                }
            )
        elif ending_date and ending_date < starting_date:
            raise serializers.ValidationError(
                {
                    "ending_date": "Ending date must be later than or equal to starting date"
                }
            )

        return values
        


class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model: Achievement
        fields = ["title", "task_description", "contribution_description"]


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model: Course
        fields = ["name", "country_code"]


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model: School
        fields = ["name"]


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model: Country
        fields = ["name"]


class EducationCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model: EducationCourse
        fields = ["course_description"]
