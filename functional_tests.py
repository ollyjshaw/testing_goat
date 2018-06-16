from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.set_headless(headless=True)
        self.browser = webdriver.Chrome(options=options)

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)  
        self.fail('Finish the test!')  

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  