from django.test import TestCase
from landinator.core.context_processors import links


class LinkContextProcessorTest(TestCase):
    def test_get_link(self):
        self.assertDictContainsSubset(
            {'site': 'https://unisagrado.edu.br'}, links({}))
