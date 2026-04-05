# this api wont be in the production code
import random

from rest_framework.test import APIClient
from django.contrib.auth.models import User

from ...models.profile import Profile


class CreateRandom(APIClient):
    
    
    def create_random_user(self):
        """
        Valid Testing of creating users
        """
        
        # regular user
        username = f"BotUser{random.randint(1, 1000)}"
        user_email = f"{username}@gmail.com"
        password = "helloworld"
        
        user = User.objects.create_user(username=username, email=user_email, password=password)
        
        # random gender
        gender = ["male", "female", "prefer not to say"]
        random_gender = gender[random.randint(0, len(gender) - 1)]
        
        # new profile and link relation
        profile = Profile.objects.create(
            user=user,
            first_name = f"{random.randint(1, 1000)}",
            middle_name = "Bot",
            last_name = "Test",
            gender = random_gender
        )