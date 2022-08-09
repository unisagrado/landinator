from django.utils import timezone
from django.test import TestCase
from django.shortcuts import resolve_url as r
from landinator.core.forms import SubscriptionForm
from landinator.landing_pages.models import LandingPage


class HomeViewGet(TestCase):
    def setUp(self):
        landing = LandingPage.objects.create(
            title='Aulão do ENEM',
            slug='aulao-do-enem',
            end_date=timezone.now().date() + timezone.timedelta(days=1)
        )
        self.resp = self.client.get(r('home', landing.slug))

    def test_get(self):
        """GET / must return status code 200 """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use index.html template"""
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_html(self):
        """HTML must contain input tags"""
        content = (
            ('Aulão do ENEM', 2),
            ('<form', 1),
            ('<input', 8),
            ('type="text"', 4),
            ('type="email"', 1),
            ('type="checkbox"', 2),
            ('type="hidden"', 1),
            ('<button type="submit"', 1),
            ('<a href="https://unisagrado.edu.br/politica-de-privacidade">política de privacidade</a>', 1)
        )
        for expected, count in content:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

    def test_csrf(self):
        """HTML must contains csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')


class HomeViewPostValid(TestCase):
    def setUp(self):
        landing = LandingPage.objects.create(
            title='Aulão do ENEM',
            slug='aulao-do-enem',
            end_date=timezone.now().date() + timezone.timedelta(days=1)
        )
        data = dict(first_name='Vinicius', last_name='Boscoa', email='valid@email.com',
                    celphone='(99) 99999-9999', accept=True)
        self.resp = self.client.post(r('home', landing.slug), data)

    def test_post(self):
        self.assertEqual(302, self.resp.status_code)
        self.assertRedirects(self.resp, r('success'))


class HomeViewPostInvalid(TestCase):
    def setUp(self):
        landing = LandingPage.objects.create(
            title='Aulão do ENEM',
            slug='aulao-do-enem',
            end_date=timezone.now().date() + timezone.timedelta(days=1)
        )
        self.resp = self.client.post(r('home', landing.slug), {})

    def test_post(self):
        """Invalid POST must not redirect"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)


class HomeViewLandingNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get(r('home', 'slug'))
        self.assertEqual(404, resp.status_code)


class HomeViewFormExpired(TestCase):
    def setUp(self):
        landing = LandingPage.objects.create(
            title='Aulão do ENEM',
            slug='aulao-do-enem',
            end_date=timezone.now().date() - timezone.timedelta(days=1),
        )
        self.resp = self.client.get(r('home', landing.slug))

    def test_submit_disabled(self):
        """Submit button must be disabled"""
        expected = '<button type="submit" disabled'
        self.assertContains(self.resp, expected)
