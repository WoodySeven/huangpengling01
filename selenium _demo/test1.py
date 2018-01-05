#!/usr/bin/env python
import unittest
import time
from selenium import webdriver


class Login(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)
        self.base_url = "file:///E:/自动化测试/github/huangpengling01/test.html"

    def test_bugfree_login(self):
        self.browser.get(self.base_url)
        for i in range(8):
            if i %2 == 1:
                element = '.a:nth-child({x}) button'.format(x=i)
                self.browser.find_element_by_css_selector(element).click()
                time.sleep(2)


if __name__ == "__main__":
 unittest.main()