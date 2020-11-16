from landinator.landing_pages.models import LandingPage
from django.test import TestCase
from datetime import date, timedelta
from landinator.landing_pages.admin import LandingPage, LandingPageModelAdmin, admin


class LandingPageModelAdminTest(TestCase):
    def setUp(self):
        self.landing = LandingPage.objects.create(
            title='Aulão do ENEM',
            slug='aulao-do-enem',
            end_date=date.today() + timedelta(days=2)
        )
        self.queryset = LandingPage.objects.all()
        self.model_admin = LandingPageModelAdmin(LandingPage, admin.site)

    def test_page_link(self):
        expected = '<a href="{0}">{0}</a>'.format('/aulao-do-enem')
        self.assertEqual(expected, self.model_admin.link(self.queryset[0]))
