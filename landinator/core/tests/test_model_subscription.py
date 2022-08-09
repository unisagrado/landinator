from datetime import date, datetime, timedelta
from landinator.landing_pages.models import LandingPage
from django.test import TestCase
from landinator.core.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        landing_page = LandingPage.objects.create(title='Aulão do ENEM',
                                                  slug='aulao-do-enem',
                                                  end_date=date.today() + timedelta(days=1))
        self.obj = Subscription(
            first_name='Vinicius',
            last_name='Boscoa',
            email='valid@email.com',
            celphone='(99) 99999-9999',
            phone='(88) 88888-8888',
            privacity_policy=True,
            send_offers=True,
            landing_page=landing_page
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Vinicius Boscoa', str(self.obj))
