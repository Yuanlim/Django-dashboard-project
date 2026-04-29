from datetime import date
import re

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .profile_properties import Gender


class Profile(models.Model):
    # auth
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )  # each user can only point to one user

    # required field
    gender = models.CharField(
        max_length=30, null=False, blank=False, choices=Gender.choices
    )  # one to one
    nationality = models.ForeignKey("Country", on_delete=models.PROTECT)  # Many to one

    # nullable field
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    linkedIn = models.URLField(max_length=1000, null=True, blank=True)
    github = models.URLField(max_length=1000, null=True, blank=True)

    # User having skills
    skills = models.ManyToManyField("Skill", related_name="Profiles", blank=True)
    
    # Extra validation/constraints
    def clean(self):
        
        # birth_date cant be future
        if isinstance(self.birth_date, date): # not a date format compare will error
            if self.birth_date and self.birth_date > date.today():
                raise ValidationError({"birth_date": _("Future date is not allowed")})
        
        # github links validate
        if self.github and not re.fullmatch(r"^https://github\.com/.+$", self.github):
            raise ValidationError({"github": _("A GitHub link should start with https://github.com/")})
        
        # linkedin links validate
        if self.linkedIn and not re.fullmatch(r"^https://www\.linkedin\.com/in/.+$", self.linkedIn):
            raise ValidationError({
                    "linkedIn": _("A LinkedIn link should start with https://www.linkedin.com/in/")
                })
        
        # phone number must be all number
        if self.phone_number and not re.fullmatch(r"^\d+$", self.phone_number):
            raise ValidationError({"phone_number": _("A phone number must be all number")})
