### Ref: https://docs.djangoproject.com/en/6.0/topics/testing/overview/
from django.test import TestCase

from apps.accounts.models.profile_properties import Country
from apps.accounts.services.profile_properties.query.search_country import SearchCountry
from apps.accounts.tests.apis.profile_create import ProfileTests


class QueryCountryTest(TestCase):
    
    def setUp(self):
        """
        Setup test data for querying Country table
        """
        # It is isolated from the database
        self.china = Country.objects.create(name="China", country_code=86)
        self.italy = Country.objects.create(name="Italy", country_code=39)
        self.guam = Country.objects.create(name="Guam", country_code=1)
        self.egypt = Country.objects.create(name="Egypt", country_code=20)
        
        # Service used
        self.search_country_service = SearchCountry()
    
    
    # fail message constructor
    def does_not_exist_report(self, data: int|str):
        return f"{data} doesn't exist in country table and it should not be happened."
        
        
    def test_search_country_by_name(self):
        q1 = self.search_country_service.search_by_name("china")
        q2 = self.search_country_service.search_by_name("italy")
        q3 = self.search_country_service.search_by_name("guam")
        q4 = self.search_country_service.search_by_name("egypt")
        
        # should be none
        q5 = self.search_country_service.search_by_name("")
        q6 = self.search_country_service.search_by_name("WHAT")
        q7 = self.search_country_service.search_by_name("Earth")
        
        
        self.assertIsNotNone(q1)
        if q1 is None:
            self.fail(self.does_not_exist_report("china"))
        self.assertEqual(q1.name, "China")
        self.assertEqual(q1.country_code, 86)
        
        self.assertIsNotNone(q2)
        if q2 is None:
            self.fail(self.does_not_exist_report("italy"))
        self.assertEqual(q2.name, "Italy")
        self.assertEqual(q2.country_code, 39)
        
        self.assertIsNotNone(q3)
        if q3 is None:
            self.fail(self.does_not_exist_report("guam"))
        self.assertEqual(q3.name, "Guam")
        self.assertEqual(q3.country_code, 1)
        
        self.assertIsNotNone(q4)
        if q4 is None:
            self.fail(self.does_not_exist_report("egypt"))
        self.assertEqual(q4.name, "Egypt")
        self.assertEqual(q4.country_code, 20)
        
        self.assertIsNone(q5)
        self.assertIsNone(q6)
        self.assertIsNone(q7)
    
    
    def test_search_country_by_pk(self):
        q1 = self.search_country_service.search_by_pk(pk=self.china.pk)
        q2 = self.search_country_service.search_by_pk(pk=self.italy.pk)
        q3 = self.search_country_service.search_by_pk(pk=self.guam.pk)
        q4 = self.search_country_service.search_by_pk(pk=self.egypt.pk)
        
        q5 = self.search_country_service.search_by_pk(pk=5206)
        q6 = self.search_country_service.search_by_pk(pk=2456)

        self.assertIsNotNone(q1)
        if q1 is None:
            self.fail(self.does_not_exist_report("china"))
        self.assertEqual(q1.name, "China")
        self.assertEqual(q1.country_code, 86)
        
        self.assertIsNotNone(q2)
        if q2 is None:
            self.fail(self.does_not_exist_report("italy"))
        self.assertEqual(q2.name, "Italy")
        self.assertEqual(q2.country_code, 39)
        
        self.assertIsNotNone(q3)
        if q3 is None:
            self.fail(self.does_not_exist_report("guam"))
        self.assertEqual(q3.name, "Guam")
        self.assertEqual(q3.country_code, 1)
        
        self.assertIsNotNone(q4)
        if q4 is None:
            self.fail(self.does_not_exist_report("egypt"))
        self.assertEqual(q4.name, "Egypt")
        self.assertEqual(q4.country_code, 20)
        
        self.assertIsNone(q5)
        self.assertIsNone(q6)