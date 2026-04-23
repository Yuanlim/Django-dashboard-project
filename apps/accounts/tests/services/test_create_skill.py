from datetime import datetime

from django.test import TestCase
from django.contrib.auth.models import User, Group

from apps.accounts.services.skill.command.create_skill import CreateSkill
from apps.accounts.tests.services.base import TestServiceBase


class CreateSkillTest(TestCase, TestServiceBase):
    
    def setUp(self):
        self.service = CreateSkill()
        
        group = Group.objects.create(name="REGULAR")
        
        self.user = User.objects.create(
            username = "Example 123",
            email="Example123@gmail.com",
            password="Vulnerabilities",
            date_joined=datetime.now()
        )
        
        self.user.groups.set([group])
        
    def test_create_skill_valid(self):
        
        skill1 = self.service.create_skill(name="Hello", user=self.user)
        skill2 = self.service.create_skill(name="YouTube", user=self.user)
        skill3 = self.service.create_skill(name="Potato", user=self.user)
        
        self.assertEqual(skill1.name, "Hello")
        self.assertEqual(skill1.verified, False)
        self.assertEqual(skill1.created_by, self.user)
        
        self.assertEqual(skill2.name, "YouTube")
        self.assertEqual(skill2.verified, False)
        self.assertEqual(skill2.created_by, self.user)
        
        self.assertEqual(skill3.name, "Potato")
        self.assertEqual(skill3.verified, False)
        self.assertEqual(skill3.created_by, self.user)
        
        self.assertRaises(Exception, self.service.create_skill, None, self.user)
        self.assertRaises(Exception, self.service.create_skill, "", self.user)
        self.assertRaises(Exception, self.service.create_skill, 
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi orci elit, imperdiet sit amet hendrerit quis, rhoncus vulputate neque. Maecenas sed massa eros. Praesent sed tempus dui, ut pellentesque ligula. Pellentesque eget dapibus ipsum, at auctor massa. Nullam id scelerisque leo. Nunc at eros vel enim vulputate fringilla ut ac orci. Pellentesque consequat sollicitudin lorem non viverra. Maecenas eleifend orci eget nulla luctus feugiat. Quisque molestie ac arcu quis elementum. Praesent ullamcorper fermentum quam condimentum dignissim. Sed consectetur est ac pretium dignissim. Proin nec gravida turpis, id gravida risus. Nulla tempus rhoncus lorem, a interdum eros aliquam id. Quisque risus nibh, facilisis ut dui nec, laoreet gravida metus. Duis varius tincidunt varius. Nulla facilisi. Morbi tortor nisi, lacinia ac tristique vel, venenatis eu leo. In consequat lectus quis blandit pretium. Proin malesuada, enim et maximus egestas, odio lorem faucibus augue, aliquet rutrum lorem urna eget sem. Duis varius massa eget laoreet ultrices. Donec quis dolor non leo rhoncus vestibulum. Proin mi enim, gravida ut quam nec, pharetra finibus enim. Ut efficitur tincidunt laoreet. Fusce imperdiet bibendum convallis. Ut laoreet dictum luctus. Donec sed sapien non dolor interdum viverra. Sed id turpis et justo sagittis ultricies sit amet id eros. In one two three", self.user)