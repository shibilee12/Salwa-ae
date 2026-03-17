from django.test import TestCase
from django.urls import reverse

class StudioPortfolioTests(TestCase):
    def test_studio_portfolio_status_code(self):
        # We don't need any complex setup for this simple view
        url = reverse('studio_portfolio')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
