#!/usr/bin/env python
import unittest
import time
from selenium import webdriver


class ZhiliangLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)
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
        ##关闭提示框
        self.browser.find_element_by_xpath("//*[@id='popup_header']/span").click()
        time.sleep(3)
        print(self.browser.title)
        time.sleep(3)
        ##窗口切换大窗口
        self.browser.maximize_window()
        ##进入职位搜索页面
        self.browser.find_element_by_xpath("/html/body/div[2]/div/ul/li[3]/a").click()
        #self.browser.find_element_by_xpath("//a[text()='职位搜索']").click()
        ##选择职位
        self.browser.find_element_by_xpath("//*[@id=\"buttonSelJobType\"]").click()
        ##选择IT质量管理/测试/配置管理
        self.browser.find_element_by_xpath("//*[@id=\"jobTab\"]/tbody/tr[4]/td[2]/table/tbody/tr[2]/td[1]/span").click()
        time.sleep(3)
        ##选择软件测试
        self.browser.find_element_by_xpath("//*[@id=\"c_buttonSelJobType_695\"]").click()
        ##选择系统测试
        self.browser.find_element_by_xpath("//*[@id=\"c_buttonSelJobType_696\"]").click()
        ###点击确定
        self.browser.find_element_by_xpath("/html/body/div[13]/div[2]/a[1]").click()
        time.sleep(5)
        ##选择行业类型
        self.browser.find_element_by_id("buttonSelIndustry").click()
        ##选择IT服务
        self.browser.find_element_by_id("c_buttonSelIndustry_160000").click()
        ##选择计算机软件
        self.browser.find_element_by_id("c_buttonSelIndustry_160400").click()
        time.sleep(10)
        ##点击确定
        #self.browser.find_element_by_xpath("/html/body/div[9]/div[2]/div[1]/a[1]").click()
        self.browser.find_element_by_class_name("orgButton").click()
        time.sleep(25)
        ##搜索栏
        self.browser.find_element_by_name("KeyWord").send_keys("软件测试")
        time.sleep(2)
        #self.browser.find_element_by_xpath("//*[@id=\"search\"]").click()
        ##选择地点
        self.browser.find_element_by_class_name("search-citybtn").click()
        ##取消北京
        self.browser.find_element_by_id("c_buttonSelCity_530").click()
        ##选择深圳
        self.browser.find_element_by_id("c_buttonSelCity_765").click()
        time.sleep(2)
        ##点击确定
        selector = 'div.sPopupTitle290 > div.sButtonBlock > a.orgButton'
        element = self.browser.find_element_by_css_selector(selector)
        element.click()
        # self.browser.find_element_by_class_name("orgButton").click()
        time.sleep(5)
        ##搜工作
        self.browser.find_element_by_xpath("//*[@id=\"searchForm\"]/form/div[8]/button").click()
        time.sleep(5)




if __name__ == "__main__":
    unittest.main()