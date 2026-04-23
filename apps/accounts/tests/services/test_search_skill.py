from django.test import TestCase

from apps.accounts.models.skill import Skill
from apps.accounts.services.skill.query.search_skill import SearchSkill
from apps.accounts.tests.services.base import TestServiceBase


class SearchSkillTest(TestCase, TestServiceBase):
    
    def setUp(self):
        """
        Test data setup
        """
        self.skill1 = Skill.objects.create(name="Write hello world", created_by=None, verified=False)
        self.skill2 = Skill.objects.create(name="ORM", created_by=None, verified=True)
        self.skill3 = Skill.objects.create(name="Python", created_by=None, verified=True)

        self.service = SearchSkill()
    
    def test_search_skill_name(self):
        q1 = self.service.search_by_name("Write hello world")
        q2 = self.service.search_by_name("orm")
        q3 = self.service.search_by_name("python")
        
        q4 = self.service.search_by_name("intern")
        q5 = self.service.search_by_name("junior")
        q6 = self.service.search_by_name("senior")
        
        self.assertIsNotNone(q1)
        if q1 is None:
            self.fail(self.does_not_exist_report("Write hello world"))
        self.assertEqual(q1.name, "Write hello world")
        self.assertEqual(q1.created_by, None)
        self.assertEqual(q1.verified, False)
        
        self.assertIsNotNone(q2)
        if q2 is None:
            self.fail(self.does_not_exist_report("orm"))
        self.assertEqual(q2.name, "ORM")
        self.assertEqual(q2.created_by, None)
        self.assertEqual(q2.verified, True)
        
        self.assertIsNotNone(q3)
        if q3 is None:
            self.fail(self.does_not_exist_report("python"))
        self.assertEqual(q3.name, "Python")
        self.assertEqual(q3.created_by, None)
        self.assertEqual(q3.verified, True)
        
        self.assertIsNone(q4)
        self.assertIsNone(q5)
        self.assertIsNone(q6)
        
    def test_search_skill_pk(self):
        q1 = self.service.search_by_pk(self.skill1.pk)
        q2 = self.service.search_by_pk(self.skill2.pk)
        q3 = self.service.search_by_pk(self.skill3.pk)
        
        q4 = self.service.search_by_pk(87)
        q5 = self.service.search_by_pk(77)
        q6 = self.service.search_by_pk(67)
        
        self.assertIsNotNone(q1)
        if q1 is None:
            self.fail(self.does_not_exist_report("Write hello world"))
        self.assertEqual(q1.name, "Write hello world")
        self.assertEqual(q1.created_by, None)
        self.assertEqual(q1.verified, False)
        
        self.assertIsNotNone(q2)
        if q2 is None:
            self.fail(self.does_not_exist_report("orm"))
        self.assertEqual(q2.name, "ORM")
        self.assertEqual(q2.created_by, None)
        self.assertEqual(q2.verified, True)
        
        self.assertIsNotNone(q3)
        if q3 is None:
            self.fail(self.does_not_exist_report("python"))
        self.assertEqual(q3.name, "Python")
        self.assertEqual(q3.created_by, None)
        self.assertEqual(q3.verified, True)
        
        self.assertIsNone(q4)
        self.assertIsNone(q5)
        self.assertIsNone(q6)