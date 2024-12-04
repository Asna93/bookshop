#Testing urls using client instance method

from django.test import TestCase

class TestUrl(TestCase):
    def test_cart_Page(self):
        response=self.client.get('/cart1/')
        print(response)
        self.assertEqual(response.status_code, 200)