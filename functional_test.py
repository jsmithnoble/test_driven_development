from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Melanie has heard about a cool new to-do app.  She goes to its home page
        self.browser.get('http://localhost:8000')

        # She notices To-Do in the title
        self.assertIn('To-Do', self.browser.title)
        self.fail("Finish the test!")

        # She is invited to enter a to-do item strait away

        # She types buy llama wool into a text box

        # When she hits enter, the page updates. and now the page lists "1: But llama wool" as an item in a to-do list

        # There is still a text box inviting her to add another item.  She enters use llama wool to make a mitten.

        # The page updates again and now shows both items on her lists

        # Melanie wonders whether the site will remember her list.  Then she sees that the site has generated a unique url for her -- there is some explanatory text to that effect.

        # She visits that URL her to-do list is still There

        # Satisfied she goes to sleep

        browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
