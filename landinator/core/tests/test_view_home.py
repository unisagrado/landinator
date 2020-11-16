from django.test import TestCase


class HomeViewGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        """GET / must return status code 200 """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use index.html template"""
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_html(self):
        """HTML must contain input tags"""
        content = (
            ('<form', 1),
            ('<input', 7),
            ('type="text"', 4),
            ('type="email"', 1),
            ('type="checkbox"', 1),
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
