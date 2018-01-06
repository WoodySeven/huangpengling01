#!/usr/bin/env python
import unittest
import time
from selenium import webdriver


class Login(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)
        self.base_url = "file:///E:/自动化测试/github/huangpengling01/selenium _demo/test.html"

    def test_bugfree_login(self):
        self.browser.get(self.base_url)
        for i in range(6):
            if i %2 == 1:
                element = 'label:nth-child({x}) input'.format(x=i)
                self.browser.find_element_by_css_selector(element).click()
                time.sleep(2)


if __name__ == "__main__":
 unittest.main()