from rest_framework import serializers
from ..models.profile import OwnerProfile
import re


class ProfileSerializers(serializers.ModelSerializer):

    class Meta:
        model = OwnerProfile
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "gender",
            "nationality",
            "email",
            "birth_date",
            "code",
            "phone_number",
            "linkedIn",
            "infenion",
            "github",
        ]

    def validate(self, values):
        """
        Check profile `first_name`, `middle_name` & `last_name` is valid.

        Arguments
        ---------
            Values -- JSON to be validate

        Return
        ------
            Valid JSON

        Exception
        ---------
            Throw if not valid
        """

        # No symbols or numbers regular expression
        validate_pattern = re.compile(r"^[A-Za-z]+$")
        first_name = values.get("first_name")
        middle_name = values.get("middle_name")
        last_name = values.get("last_name")

        # Check name is valid
        if not first_name and validate_pattern.fullmatch(first_name):
            raise serializers.ValidationError(
                {"first_name": "First name must contain only letters."}
            )

        if middle_name and validate_pattern.fullmatch(middle_name):
            raise serializers.ValidationError(
                {"middle_name": "Middle name must contain only letters."}
            )

        if not last_name and validate_pattern.fullmatch(last_name):
            raise serializers.ValidationError(
                {"last_name": "Last name must contain only letters."}
            )

        return values

    def validate_phone_number(self, value):
        """
        Validate if phone number is all numbers

        Arguments
        ---------
            value -- request dictionary

        Return
        ------
            Valid JSON

        Exception
        ---------
            Throw if not valid
        """
        validate_pattern = re.compile(r"^\d+$")

        if validate_pattern.fullmatch(value):
            return value

        raise serializers.ValidationError(
            "You can only have numbers in your phone number."
        )

    def validate_linkedIn(self, value):
        """
        Validate if it is a linkedIn profile

        Arguments
        ---------
            value -- request dictionary

        Return
        ------
            Valid JSON

        Exception
        ---------
            Throw if not valid
        """

        validate_pattern = re.compile(r"^https://www.linkedin\.com/in/.+$")

        if validate_pattern.fullmatch(value):
            return value

        raise serializers.ValidationError(
            "A valid LinkedIn URL should start with https://www.linkedin.com/in/"
        )

    def validate_github(self, value):
        validate_pattern = re.compile(r"^https://github\.com/.+$")

        if validate_pattern.fullmatch(value):
            return value

        raise serializers.ValidationError(
            "A valid github URL should start with https://www.github.com/in/"
        )
