from django.test import TestCase,Client
from django.urls import reverse

class TestViews(TestCase):
    def test_home_view(self):
        client=Client()
        response=client.get(reverse('home'))
        print("Response is: ", response)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home.html')