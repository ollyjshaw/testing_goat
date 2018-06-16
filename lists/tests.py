from django.test import TestCase
from django.urls import resolve
from lists.views import home_page  
from django.http import HttpRequest

class SmokeTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')  
        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))
        self.assertTemplateUsed(response, 'home.html')