from django.db import models
from django.contrib.auth.models import User

from .profile_properties import Gender


class Profile(models.Model):
    # auth
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )  # each user can only point to one user

    # user real name
    first_name = models.CharField(max_length=20, null=False, blank=False)  # Zu Yuan
    middle_name = models.CharField(max_length=10, null=True, blank=True)
    last_name = models.CharField(max_length=10, null=False, blank=False)  # Lim

    # required field
    gender = models.CharField(
        max_length=30, null=False, blank=False, choices=Gender.choices
    )  # one to one
    nationality = models.ForeignKey("Country", on_delete=models.PROTECT)  # Many to one

    # django User has email field this is redundant
    # email = models.EmailField(null=False, blank=False)

    acc_created_date = models.DateField(null=False, blank=False, auto_now_add=True)

    # nullable field
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    linkedIn = models.URLField(max_length=1000, null=True, blank=True)
    infineon = models.URLField(max_length=1000, null=True, blank=True)
    github = models.URLField(max_length=1000, null=True, blank=True)

    # User having skills
    skills = models.ManyToManyField("Skill", related_name="Profiles", blank=True)

    @property
    def full_name(self):
        concatNameList = [self.first_name, self.middle_name, self.last_name]
        return " ".join(
            name for name in concatNameList if name
        )  # Checks null, if not join
