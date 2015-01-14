from django.test import RequestFactory, TestCase
from mock import Mock

from pages.views import PageView


class TestPageView(TestCase):
    def setUp(self):
        self.page_repository = Mock()
        self.view = PageView.as_view(repository=self.page_repository)

    def call(self):
        return self.view(RequestFactory().get('/pages/2'), page='2')

    def test_finds_requested_page(self):
        self.call()
        self.page_repository.get.assert_called_with('2')

    def test_adds_requested_page_to_context(self):
        self.page_repository.get.return_value = 'page body'
        response = self.call()
        self.assertEqual(response.context_data.get('body'), 'page body')
