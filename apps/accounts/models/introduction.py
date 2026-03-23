from django.db import models


# Role model (e.g. backend dev)
class RoleTag(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False, unique=True)

    # Returns a string representation of this obj
    def __str__(self):
        return self.title


# Introduction model (e.g. Hi, I am Yuan. A passionate programmer)
class OwnerIntroduction(models.Model):
    owner = models.OneToOneField(
        "OwnerProfile", on_delete=models.PROTECT, related_name="intro"
    )  # one to one model to user, because each user should only has one intro
    intro = models.CharField(max_length=2000, null=False, blank=False)
    roles = models.ManyToManyField(RoleTag, related_name="introductions", blank=True)

    def __str__(self):
        return self.intro
