from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time


MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn('foo', [row.text for row in rows])
                return
            except (AssertionError, WebDriverException):
                if time.time() - start_time > MAX_WAIT:
                    raise
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Melanie has heard about a cool new to-do app.  She goes to its home page
        self.browser.get(self.live_server_url)

        # She notices To-Do in the title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item strait away
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types buy llama wool into a text box
        input_box.send_keys("Buy llama wool")
        # When she hits enter, the page updates. and now the page lists "1: But llama wool" as an item in a to-do list
        input_box.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table("1: Buy llama wool")
        # There is still a text box inviting her to add another item.  She enters use llama wool to make a mitten.
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys("Use llama wool to make a mitten")
        input_box.send_keys(Keys.ENTER)
        # The page updates again and now shows both items on her lists
        self.check_for_row_in_list_table("1: Buy llama wool")
        self.check_for_row_in_list_table("2: Use llama wool to make a mitten")

        self.fail("Finish the test!")
        # Melanie wonders whether the site will remember her list.  Then she sees that the site has generated a unique url for her -- there is some explanatory text to that effect.

        # She visits that URL her to-do list is still There

        # Satisfied she goes to sleep
        self.fail("Finish the test!")
        browser.quit()
