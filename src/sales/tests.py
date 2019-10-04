from django.test import TestCase
from .services import *

class NormalizePhoneTestCase(TestCase):

    def test_normalize_phone(self):
        self.assertEqual(normalize_phone("+38-0975896547"), '380975896547')
        self.assertEqual(normalize_phone("+38-097-5896-547,+38-09758-96547"), '380975896547')
        self.assertEqual(normalize_phone("+97-5896-547,+38-09758-96547"), '380975896547')
        self.assertEqual(normalize_phone("+097-5896-547,+38-09758-96547"), '380975896547')
        self.assertEqual(normalize_phone("+8097-5896-547,+38-09758-96547"), '380975896547')
        self.assertEqual(normalize_phone("+197-5896-547,+38-09758-96547"), None)
        self.assertEqual(normalize_phone("+197-5896-5473333333,+38-09758-96547"), None)
        self.assertEqual(normalize_phone("097589654"), None)
        self.assertEqual(normalize_phone("8097589654"), None)
        self.assertEqual(normalize_phone("38097589654"), None)

