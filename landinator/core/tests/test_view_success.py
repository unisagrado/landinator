from django.test import TestCase
from django.shortcuts import resolve_url as r


class SuccessGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('success'))

    def test_get(self):
        """GET /sucesso must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use success.html"""
        self.assertTemplateUsed(self.resp, 'subscription/success.html')

    def test_html(self):
        content = 'Inscrição realizada com sucesso!'
        self.assertContains(self.resp, content)
