from django.test import TestCase
from .models import *


class EmployerTestCase(TestCase):

    def setUp(self):
        create_vacancy = Vacancy.objects.create(position='sdev')

        Employer.objects.create(company_name='otus',
                                country='UK',
                                vacancy=create_vacancy)

        Employer.objects.create(company_name='uber',
                                country='USA',
                                vacancy=create_vacancy)

    def test_employer(self):
        otus = Employer.objects.get(,,
        uber = Employer.objects.get(,,
        self.assertEqual(otus.country, "UK")
        self.assertEqual(uber.country, "USA")
        self.assertEqual(otus.vacancy, "sdev")
        self.assertEqual(uber.vacancy, "sdev")
