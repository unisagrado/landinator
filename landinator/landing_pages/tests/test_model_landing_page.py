from datetime import date, datetime
from django.test import TestCase
from landinator.landing_pages.models import LandingPage
from django.shortcuts import resolve_url as r


class LandingPageModelTest(TestCase):
    def setUp(self):
        self.obj = LandingPage(
            title='Aulão do ENEM',
            slug='aulao-do-enem',
            end_date=date(2020, 11, 17),
        )
        self.obj.save()

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
        )
        qs = LandingPage.objects.all()
        expected = ['aulao-do-enem', 'aulao-do-enem-2']
        self.assertQuerysetEqual(qs, expected, lambda o: o.slug, ordered=False)
