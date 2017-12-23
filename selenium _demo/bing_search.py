#!/usr/bin/env python

from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://cn.bing.com/")
print(browser.title)
browser.maximize_window()
browser.find_element_by_id("sb_form_q").send_keys("python")
browser.find_element_by_id("sb_form_go").click()
print(browser.current_window_handle)
browser.quit()

