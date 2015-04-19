from selenium import webdriver
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3) # Browser will eventually wait 3 secs
                                        # for a thing to appear if needed

    def tearDown(self):
        self.browser.quit()