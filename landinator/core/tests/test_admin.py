from datetime import date, timedelta
from django.test import TestCase
from django.shortcuts import resolve_url as r

from landinator.landing_pages.models import LandingPage
from landinator.core.admin import Subscription, SubscriptionModelAdmin, admin


class SubscriptionModelAdminTest(TestCase):
    def setUp(self):
        self.landing_page = LandingPage.objects.create(
            title='Aulão do ENEM',
            slug='aulao-do-enem',
            end_date=date.today() + timedelta(days=1)
        )
        Subscription.objects.create(first_name='Vinicius',
                                    last_name='Boscoa',
                                    email='valid@email.com',
                                    celphone='(99) 99999-9999',
                                    landing_page=self.landing_page)
        self.queryset = Subscription.objects.all()
        self.model_admin = SubscriptionModelAdmin(Subscription, admin.site)

    def test_page_link(self):
        expected = '<a href="{0}">{0}</a>'.format(
            r('home', self.landing_page.slug))
        self.assertEqual(
            expected, self.model_admin.page_link(self.queryset[0]))

    def test_admin_has_export_as_csv_action(self):
        self.assertIn('export_as_csv', self.model_admin.actions)


class ExportAsCsvTest(TestCase):
    def setUp(self):
        landing_page = LandingPage.objects.create(
            title='Aulão do ENEM',
            slug='aulao-do-enem',
            end_date=date.today() + timedelta(days=1)
        )
        Subscription.objects.create(first_name='Vinicius',
                                    last_name='Boscoa',
                                    email='valid@email.com',
                                    celphone='(99) 99999-9999',
                                    landing_page=landing_page)
        model_admin = SubscriptionModelAdmin(Subscription, admin.site)
        self.resp = model_admin.export_as_csv({}, Subscription.objects.all())

    def test_response(self):
        """Export as CSV method must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_content_type(self):
        self.assertIn('/csv', self.resp['Content-Type'])
