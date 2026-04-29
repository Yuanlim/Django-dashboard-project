import re

from django.core.exceptions import ValidationError

class UserExtraValidator:

    def validate(
            self, 
            first_name: str | None, 
            last_name: str | None,
            password: str | None, 
            email: str | None
        ):
        """
        extra validation on:
        inserted User first_name and last_name.
        1. Should not be empty or None.
        2. Should be all alphabets.
        
        inserted User password.
        1. Should not be empty or None.
        2. Have at least one number
        3. Have at least one uppercase letter
        4. Have at least one lowercase letter
        5. Have at least one special character
        6. 6 or more characters in length
        
        inserted User email.
        """
        all_alpha = re.compile(r"^[A-Za-z]+$")
        strong_pass = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z\d]).{6,}$"
        
        errors = {}
        if not first_name or not all_alpha.fullmatch(first_name.strip()):
            errors["first_name"] = (
                "Please insert any character or more as your first name,"
                "and cant contain not alphabet characters."
            )
        
        if not last_name or not all_alpha.fullmatch(last_name.strip()):
            errors["last_name"] = (
                "Please insert any character or more as your last name,"
                "and cant contain not alphabet characters."
            )
            
        if not password or not re.fullmatch(strong_pass, password):
            errors["password"] = (    
                "Password must not be empty, must be at least 6 characters long, "
                "and must contain at least one number, one uppercase letter, "
                "one lowercase letter, and one special character."
            )
            
        if not email:
            errors["email"] = "Email couldn't be empty."
            
        if errors:
            raise ValidationError(errors)