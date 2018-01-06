#!/usr/bin/env python
import unittest
import time
from selenium import webdriver
import configparser

class Login(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)
        ##读配置文件打开本地文件
        cf = configparser.ConfigParser()
        cf.read("test.conf")
        self.base_url = str(cf.get("file", "file_path"))
        ##直接打开文件路径
        # self.base_url = "file:///G:/test/github/huangpengling01/selenium_demo/test.html"
    def test_bugfree_login(self):
        self.browser.get(self.base_url)
        for i in range(6):
            if i %2 == 1:
                element = '.table:nth-child({x}) input'.format(x=i)
                self.browser.find_element_by_css_selector(element).click()
                time.sleep(2)


if __name__ == "__main__":
 unittest.main()