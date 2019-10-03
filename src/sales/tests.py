from django.test import TestCase
from .services import *

class NormalizePhoneTestCase(TestCase):


    def test_normalize_phone(self):
        phones = """
        098 015 2241
        098 015 2241
        097 606 7603
        050 058 88 62
        380 502 729840
        067 321 1696
        380 954 696069
        +380661258387
        +380 (63) 670 81 34
        (050)361-30-44
        (097)146-86-30
        +380669607785
        099 788 7595
        +38 093 917 63 24
        097 646 2517
        """
        self.assertEqual(normalize_phone("vfdv444"), '444')

