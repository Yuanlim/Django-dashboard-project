from django.db import models


class Resume(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True, null=False, blank=True)
    the_file = models.FileField(upload_to="./documents/", blank=False)

    # Relations to user (many to one)
    owner = models.ForeignKey(
        "OwnerProfile", on_delete=models.CASCADE, related_name="resumes"
    )

    # for debugging
    def __str__(self):
        return str(self.created_datetime)
