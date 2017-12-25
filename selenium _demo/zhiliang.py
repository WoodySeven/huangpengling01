#!/usr/bin/env python
import unittest
import time
from selenium import webdriver

class ZhiliangLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(20)
        self.base_url = "http://ts.zhaopin.com/jump/index_new.html"

    def tearDown(self):
        self.browser.quit()

    def test_bugfree_login(self):
        self.browser.get(self.base_url)
        self.browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/ul/li[2]").click()
        self.browser.find_element_by_name("loginname").send_keys("15012959916")
        self.browser.find_element_by_name("password").send_keys("bella1218")
        self.browser.find_element_by_name("isautologin").click()
        self.browser.find_element_by_name("loginbutton").click()
        time.sleep(3)
        print(self.browser.title)
        self.browser.find_element_by_xpath("/html/body/div[10]/h5/span").click()
        self.browser.find_element_by_xpath("/html/body/div[3]/form/div/div[3]/input").send_keys("软件测试")
        self.browser.find_element_by_xpath("//*[@id=\"search\"]").click()
        time.sleep(3)



if __name__ == "__main__":
    unittest.main()