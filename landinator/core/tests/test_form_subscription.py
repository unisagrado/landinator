from django.test import TestCase
from landinator.core.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()

    def test_form_has_fiels(self):
        """Form must have 6 fields"""
        expected = ['first_name',
                    'last_name',
                    'email',
                    'celphone',
                    'phone',
                    'accept']
        self.assertSequenceEqual(expected, list(self.form.fields))
