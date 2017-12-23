#!/usr/bin/env python
import time
from selenium import webdriver
"""
登录bugfree的网页：
1. 打开浏览器
2. 转到bugfree的网址： 192.168.2.87/bugfree
3. 输入用户名、密码
4. 点击登录按钮
5. 检查登录是否成功
"""
base_url = "http://192.168.2.87/bugfree"
browser = webdriver.Firefox()
browser.get(base_url)
browser.find_element_by_id("LoginForm_username").send_keys("admin")
browser.find_element_by_id("LoginForm_password").send_keys("123456")
browser.find_element_by_id("LoginForm_rememberMe").click()
browser.find_element_by_id("SubmitLoginBTN").click()
time.sleep(3)
assert "list" in browser.current_url
assert "退出" in browser.page_source
time.sleep(3)
browser.quit()