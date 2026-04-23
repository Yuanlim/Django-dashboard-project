from django.contrib.auth.models import User

from django.db import models


class Project(models.Model):
    """
    user project details model
    """

    # Many project to one user
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="projects"
    )

    # Project title: e.g. Chatbot project
    title = models.CharField(max_length=200, null=False, blank=False)

    starting_date = models.DateField()
    ending_date = models.DateField(
        null=True, blank=True
    )  # Null: I am currently working on this

    # Project description: (summary) (contribution) (task)
    description = models.CharField(max_length=3000, null=True, blank=True)

    # Project used skills
    skills = models.ManyToManyField("Skill", related_name="projects", blank=True)

    def __str__(self):
        return f"""
title: {self.title}
starting_date: {self.starting_date}
ending_date: {self.ending_date}
description: {self.description}
    """
