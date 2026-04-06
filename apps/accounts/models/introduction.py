from django.db import models


# Role model (e.g. backend dev)
class RoleTag(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False, unique=True)
    created_by = models.ForeignKey("Profile", on_delete=models.PROTECT, null=True, blank=True)
    verified = models.BooleanField(null=False, blank=False, default=False)

    # Returns a string representation of this obj
    def __str__(self):
        return self.title


# Introduction model (e.g. Hi, I am Yuan. A passionate programmer)
class Introduction(models.Model):
    profile = models.OneToOneField(
        "Profile", on_delete=models.PROTECT, related_name="intro"
    )  # one to one model to user, because each user should only has one intro
    intro = models.CharField(max_length=2000, null=False, blank=False)
    roles = models.ManyToManyField(RoleTag, related_name="introductions", blank=True)

    def __str__(self):
        return self.intro
