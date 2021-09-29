from datetime import date, datetime
from landinator.core.models import Subscription
from django.test import TestCase
from django.utils import timezone
from landinator.landing_pages.models import LandingPage
from django.shortcuts import resolve_url as r


class LandingPageModelTest(TestCase):
    def setUp(self):
        self.obj = self.make_valid_page()

    def test_create(self):
        self.assertTrue(LandingPage.objects.exists())

    def test_created_at(self):
        """LandingPage Must have a created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Aulão do ENEM', str(self.obj))

    def test_limit_subscriptions_default_to_zero(self):
        """By default limit subscriptions must be 0"""
        self.assertEqual(0, self.obj.limit_subscriptions)

    def test_get_absolute_url(self):
        url = r('home', self.obj.slug)
        self.assertEqual(url, self.obj.get_absolute_url())

    def test_auto_slug(self):
        LandingPage.objects.create(
            title='Aulão do ENEM',
            slug='aulao-do-enem',
            end_date=date(2020, 11, 17),
            tag='aulao_enem_2021',
        )
        qs = LandingPage.objects.all()
        expected = ['aulao-do-enem', 'aulao-do-enem-2']
        self.assertQuerysetEqual(qs, expected, lambda o: o.slug, ordered=False)

    def test_enabled(self):
        self.assertTrue(self.obj.enabled())

    def test_disabled_date(self):
        page = self.make_valid_page(
            end_date=timezone.now().date() - timezone.timedelta(days=1))
        self.assertFalse(page.enabled())

    def test_should_not_integrate(self):
        page = self.make_valid_page(tag=None)
        self.assertFalse(page.should_integrate())

    def test_should_integrate(self):
        page = self.make_valid_page()
        self.assertTrue(page.should_integrate())

    def test_disabled_subscriptions(self):
        page = self.make_valid_page(limit_subscriptions=1)
        Subscription.objects.create(first_name='Vinicius', last_name='Boscoa',
                                    email='valid@email.com', celphone='99-99999-9999',
                                    accept=True, landing_page=page)
        self.assertFalse(page.enabled())

    def make_valid_page(self, **kwargs):
        valid = dict(title='Aulão do ENEM',
                     slug='aulao-do-enem',
                     end_date=timezone.now().date() + timezone.timedelta(days=1),
                     tag='aulao_enem_2021')
        data = dict(valid, **kwargs)
        return LandingPage.objects.create(**data)
