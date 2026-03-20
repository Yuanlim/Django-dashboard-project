from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)

    # User included skills
    owner = models.ManyToManyField(
        "OwnerProfile", related_name="skills", null=True, blank=True
    )
