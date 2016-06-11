from datetime import datetime

from django.test import TestCase
from django.http import HttpRequest
from django.core.urlresolvers import resolve
from blogpost.models import Blogpost



from blogpost.views import index, view_post


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        self.assertIn(b'<title>Welcome to my blog</title>', response.content)
    def test_blogpost_create_with_view(self):
        Blogpost.objects.create(title = 'hello', author = 'admin', slug = 'this_is_a_test', body = 'This is a blog', posted = datetime.now)
        response = self.client.get('/blog/this_is_a_test.html')
        self.assertIn(b'This is a blog', response.content)