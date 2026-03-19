from django.db import models


# Role model (e.g. backend dev)
class Role_Tag(models.Model):
    role_title = models.CharField(max_length=30, null=False, unique=True)

    # Returns a string representation of this obj
    def __str__(self):
        return {self.role_title}


# Owner Introduction model
class Owner_Introduction(models.Model):
    intro = models.CharField(max_length=2000, null=False)
    # One to many roles
    role_tag = models.ForeignKey(Role_Tag, on_delete=models.PROTECT)

    def __str__(self):
        return {self.intro}
