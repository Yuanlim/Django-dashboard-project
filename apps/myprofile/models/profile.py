from django.db import models
from django.contrib.auth.models import User


# A one property model to one with user
class Gender(models.TextChoices):
    """
    A one to one property model with user
    """

    MALE = "male", "Male"
    FEMALE = "female", "Female"
    PREFER_NOT_TO_SAY = "prefer not to say", "Prefer not disclosed"


class Country(models.Model):
    """
    A one to one property model with user
    """

    name = models.CharField(max_length=20, null=False)


class Degree(models.TextChoices):
    """
    A one to one property model with education
    """

    PHD = "phd", "PHD"
    MASTERS = "masters", "MASTERS"
    BACHELOR = "bachelor", "BACHELOR"
    DIPLOMA = "diploma", "DIPLOMA"
    DEGREE = "degree", "DEGREE"
    OTHERS = "others", "OTHERS"


class School(models.Model):
    """
    A one to one property model with education
    """

    name = models.CharField(max_length=200, null=False)


class Course(models.Model):
    """
    A one to one property model with education course
    """

    name = models.CharField(max_length=100, null=False)


class Education(models.Model):
    """
    A many to one property model with user
    """

    owner = models.ForeignKey(
        "OwnerProfile", on_delete=models.CASCADE, related_name="educations"
    )
    # When delete to not also delete relation ones
    degree = models.CharField(max_length=10, null=False, choices=Degree.choices)
    other_degree = models.CharField(
        max_length=30, null=True
    )  # When choose other -> this field suppose to be not null
    school = models.ForeignKey(School, on_delete=models.PROTECT)  # one to one


class EducationCourse(models.Model):
    """
    A many to one property model with education
    """

    education = models.ForeignKey(
        Education, on_delete=models.CASCADE, related_name="education_courses"
    )

    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    course_description = models.CharField(max_length=500, null=True)


# A many property model to one with user
class Achievement(models.Model):
    """
    A many to one property model with user
    """

    owner = models.ForeignKey(
        "OwnerProfile", on_delete=models.CASCADE, related_name="achievements"
    )
    title = models.CharField(max_length=200, null=False)
    task_description = models.CharField(max_length=1000, null=True)
    contribution_description = models.CharField(max_length=1000, null=False)


class CountryCode(models.Model):
    """
    A one to one property model with user
    """

    code = models.CharField(max_length=200, null=False)


class OwnerProfile(
    models.Model
):  # Prob should rename it to user in later development for global model
    # auth
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )  # each user can only point to one user

    # user real/login name
    first_name = models.CharField(max_length=20, null=False)  # Zu Yuan
    middle_name = models.CharField(max_length=10, null=True)
    last_name = models.CharField(max_length=10, null=False)  # Lim
    login_name = models.CharField(max_length=40, null=False, unique=True)  # YuanLim
    # required field
    gender = models.CharField(
        max_length=10, null=False, choices=Gender.choices
    )  # one to one
    nationality = models.ForeignKey(Country, on_delete=models.PROTECT)  # one to one
    email = models.EmailField(null=False)
    acc_created_date = models.DateField(null=False)
    # nullable field
    birth_day = models.DateField(null=True)
    code = models.ForeignKey(
        CountryCode, null=True, on_delete=models.PROTECT
    )  # one to one
    phone_number = models.CharField(max_length=10, null=True)  # one to one
    linkedIn = models.URLField(max_length=1000, null=True)
    infineon = models.URLField(max_length=1000, null=True)
    github = models.URLField(max_length=1000, null=True)

    @property
    def full_name(self):
        concatNameList = [self.first_name, self.middle_name, self.last_name]
        return " ".join(
            name for name in concatNameList if name
        )  # Checks null, if not join
