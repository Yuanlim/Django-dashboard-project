from django.db import models


class EventType(models.TextChoices):
    FREE_TIME = "FREE_TIME", "free_time"
    WORKING = "WORKING", "working"
    VACATION = "VACATION", "vacation"
    PRACTICE = "PRACTICE", "practice"
    OTHER = "OTHER", "other"


class Schedule(models.Model):
    time = models.DateTimeField(null=False, blank=False)
    event_type = models.CharField(max_length=10, choices=EventType.choices)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"""
time: {str(self.time)}
event_type: {self.event_type}
description: {self.description}
                """
