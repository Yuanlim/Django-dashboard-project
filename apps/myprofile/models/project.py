from django.db import models


class Project(models.Model):
    """
    user project details model
    """

    # Many project to one user
    owner = models.ForeignKey(
        "OwnerProfile", on_delete=models.CASCADE, related_name="projects"
    )

    # Project title: e.g. Chatbot project
    title = models.CharField(max_length=200, null=False, blank=False)

    # TODO: starting date should be earlier or equal than ending date
    # Project starting/ending date: e.g. 2026-1-1 ~ 2026-2-1
    starting_date = models.DateField()
    ending_date = models.DateField(
        null=True, blank=True
    )  # Null: I am currently working on this

    # Project description: (summary) (contribution) (task)
    description = models.CharField(max_length=3000, null=True, blank=True)

    # Project used skills
    project = models.ManyToManyField("Project", related_name="skills", blank=True)
