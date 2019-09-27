from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_id('h1').header_text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item strait away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types buy llama wool into a text box
        input_box.send_keys("Buy llama wool")
        # When she hits enter, the page updates. and now the page lists "1: But llama wool" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy llama wool' for row in rows)
        )

        # There is still a text box inviting her to add another item.  She enters use llama wool to make a mitten.
        self.fail("Finish the test!")
        # The page updates again and now shows both items on her lists

        # Melanie wonders whether the site will remember her list.  Then she sees that the site has generated a unique url for her -- there is some explanatory text to that effect.

        # She visits that URL her to-do list is still There

        # Satisfied she goes to sleep
        self.fail("Finish the test!")
        browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
