#!/usr/bin/env python
import unittest
import time
from selenium import webdriver


class BugfreeLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(20)
        self.base_url = "http://192.168.2.87/bugfree"

    def tearDown(self):
        self.browser.quit()

    def test_bugfree_login(self):
        self.browser.get(self.base_url)
        self.browser.find_element_by_id("LoginForm_username").send_keys("admin")
        self.browser.find_element_by_id("LoginForm_password").send_keys("123456")
        self.browser.find_element_by_id("LoginForm_rememberMe").click()
        self.browser.find_element_by_id("SubmitLoginBTN").click()
        time.sleep(3)
        self.assertIn("list" ,self.browser.current_url)
        self.assertIn("退出" ,self.browser.page_source)
        time.sleep(3)



if __name__ == "__main__":
    unittest.main()