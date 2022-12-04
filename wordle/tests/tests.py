from django.test import TestCase

# Create your tests here.
from selenium import webdriver
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_browser(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Django', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()