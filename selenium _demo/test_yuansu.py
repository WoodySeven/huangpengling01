#!/usr/bin/env python
import unittest
from selenium import webdriver
import time

from selenium.webdriver import ActionChains


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(20)
        self.base_url = "http://test1.zmninfo.com/SimulationElement/"

    def tearDown(self):
        self.browser.quit()

    def test_case(self):
        self.browser.get(self.base_url)
        ##单行文本框
        self.browser.find_element_by_class_name("text").send_keys("baidu")
        self.browser.find_element_by_id("t1").send_keys("111")
        self.browser.find_element_by_name("$a_dollar").send_keys("2234")
        self.browser.find_elements_by_xpath("//input[@name='textreadonly']")
        self.browser.find_elements_by_name("textreadonly")
        time.sleep(2)

        ##多行文本框
        self.browser.find_element_by_name("ta1").send_keys("今天星期天，祝大家身体健康，万事如意！")
        time.sleep(2)

        ##多选框
        list_checkbos = self.browser.find_elements_by_name("c1")
        for i in list_checkbos:
            i.click()
        time.sleep(2)

        ##选第4个多选框
        self.browser.find_element_by_xpath("/html/body/form[4]/table/tbody/descendant::input[last()]").click()

        ##单选框
        self.browser.find_element_by_xpath("/html/body/form[5]/table/tbody/tr[1]/td[2]/input").click()
        time.sleep(2)

        ##密码框
        self.browser.find_element_by_name("p1").send_keys("124566")
        time.sleep(2)

        ##下拉列表，弹窗提示你选择的文本
        self.browser.find_element_by_name("s1").click()
        self.browser.find_element_by_xpath("/html/body/form[7]/table/tbody/tr/td[2]/select/option[2]").click()
        time.sleep(2)

        ##表格-定位某个元素并打印出来
        print(self.browser.find_element_by_xpath("/html/body/form[8]/table/tbody/tr[2]/td[2]").text)
        time.sleep(2)

        ##警告框
        self.browser.find_element_by_name("b1").click()
        time.sleep(2)
        alert = self.browser.switch_to.alert  ##进入警示框跳出
        alert.accept()  ##直接进入alert - accept,点击同意
        time.sleep(2)

        ##鼠标悬浮
        target = self.browser.find_element_by_xpath("/html/body/div[4]/div")
        ActionChains(self.browser).move_to_element(target).click().perform()
        time.sleep(2)

        ##单击
        target1 = self.browser.find_element_by_xpath("/html/body/div[5]/div")
        ActionChains(self.browser).move_to_element(target1).click().perform()
        time.sleep(3)








if __name__ == "__main__":
    unittest.main()