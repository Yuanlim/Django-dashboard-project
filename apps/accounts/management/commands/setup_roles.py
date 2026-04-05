# run once py
from django.contrib.auth.models import Group

HAD_ROLES = ["OWNER", "COMPANY", "REGULAR"]


def setup_roles():
    for role in HAD_ROLES:
        Group.objects.get_or_create(name=role)