from django.test import TestCase


class TestPageRequests(TestCase):
    def test_respond_with_the_correct_page(self):
        response = self.client.get('/pages/2')
        self.assertIn('<p>This is page two</p>', response.content)
