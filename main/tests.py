from django.test import TestCase
from django.urls import reverse
from django.test import Client


class URLsTest(TestCase):
    def test_homepage_url(self):
        """
        Test that homepage url works.
        """
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
