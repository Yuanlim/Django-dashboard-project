from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)