# -*- coding: UTF-8 -*-
import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

long_waiting = 5
short_waiting = 2

class Login_Page(object):
    def __init__(self, browser):
        self.browser = browser

    def sel_email(self):
        time.sleep(3)
        self.browser.find_element_by_xpath("/html/body/ui-view/ui-view/div/div/div[1]/div[2]/ng-include/div/section[1]/ng-include/form/div[2]/ul/li[2]").click()

    def input_email(self, email):
        email_element = WebDriverWait(self.browser,long_waiting).until(EC.visibility_of_element_located((By.NAME,"user[email]")))
        email_element.clear()
        email_element.send_keys(email)

    def input_pwd(self, pwd):
        pwd_element = WebDriverWait(self.browser,long_waiting).until(EC.visibility_of_element_located((By.NAME,"user[password]")))
        pwd_element.clear()
        pwd_element.send_keys(pwd)

    def click_login(self):
        login_btn = self.browser.find_element_by_css_selector("body > ui-view > ui-view > div > div > div.main-wrap > div.operation-pane > ng-include > div > section:nth-child(1) > ng-include > form > div:nth-child(5) > button")
        time.sleep(short_waiting)
        login_btn.click()

    def check_success(self):
        self.browser.find_element_by_css_selector("body > ui-view > ui-view > div.main-space.ng-scope > ng-include > header > ng-include > div.roof-container.right.ng-scope > div:nth-child(5) > span > i").is_displayed()
        self.browser.find_element_by_css_selector("body > ui-view > ui-view > div.main-space.ng-scope > div > div.home-drawer.ng-scope > div > div.drawer-menu.ng-scope > div.pico-tag").is_displayed()

    def check_fail(self, msg):
        assert msg == self.browser.find_element_by_css_selector("body > div.alert-container-wrap.alert-wrap-right > div").text

    def click_fg_pwd(self):
        self.browser.find_element_by_css_selector("body > ui-view > ui-view > div > div > div.main-wrap > div.operation-pane > ng-include > div > section:nth-child(1) > ng-include > form > div.options.uk-form-row > div > span > a")
        self.browser.element_clickable("body > ui-view > ui-view > div > div > div.main-wrap > div.operation-pane > ng-include > div > section:nth-child(1) > ng-include > form > div.options.uk-form-row > div > span > a")
