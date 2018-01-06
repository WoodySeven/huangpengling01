#!/usr/bin/env python
# @Author  : sally

from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
class BaiDu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.base_url = "https://www.zhaopin.com/"
        self.driver.get(self.base_url)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        print(driver.current_url)
        time.sleep(2)
        driver.find_element_by_id('loginname').send_keys('18126122367')
        password = driver.find_element_by_id('password')
        password.clear()
        password.send_keys('test1234')
        # 自动登录没做判断
        driver.find_element_by_xpath('//*[@id="loginForm"]/div[3]/button').click()
        time.sleep(2)
        #先关闭弹窗
        notice=driver.find_element_by_class_name('Delivery_success_popdiv_title')
        print(notice.text)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="popup_header"]/span').click()
        #选择职位搜索
        driver.maximize_window()
        driver.find_element_by_xpath('/html/body/div[2]/div/ul/li[3]/a').click()
        #搜索软件测试
        search=driver.find_element_by_name('KeyWord').send_keys('软件测试')
        driver.find_element_by_class_name('doesSearch').click()
        time.sleep(3)
        #选中复选框
        check_boxes=driver.find_elements_by_name('vacancyid')
        for i,cb in enumerate(check_boxes):
            if i%2==0:
                cb.click()
                time.sleep(1)










if __name__=='__main__':
    unittest.main()