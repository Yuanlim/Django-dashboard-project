from django.db import models


class Skill(models.Model):
    
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)
    created_by = models.ForeignKey("Profile", on_delete=models.PROTECT, null=True, blank=True)
    verified = models.BooleanField(null=False, blank=False, default=False)