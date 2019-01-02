import unittest
import time
import selenium.webdriver.support.ui as ui
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import sys
import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Login_Page_lib import Login_Page
from Personal_Desktop_lib import Personal_Desktop
from selenium.webdriver.chrome.options import Options

url = "http://alpha.picowork.com"
account = "selenium01@mailinator.com"
password = "qa123456"
long_waiting = 5
short_waiting = 1
friend = "Selenium01"

opt = Options()
opt_lst = [
    '-allow-running-insecure-content',  # unsafe content
    'use-fake-device-for-media-stream',  # for mic
    'use-fake-ui-for-media-stream',  # for video streaming
    '--disable-infobars',
    'start-maximized',
    '--disable-extensions']
for opts in opt_lst:
	opt.add_argument("opts")
opt.add_experimental_option("prefs",
	{ \
		"profile.default_content_setting_values.media_stream_mic": 1,
		"profile.default_content_setting_values.media_stream_camera": 1,
		"profile.default_content_setting_values.geolocation": 1,
		"profile.default_content_setting_values.notifications": 1}
)

class create_cospace(unittest.TestCase):
	def test_1(self):
	#setup
		self.browser = webdriver.Chrome(chrome_options=opt)
		self.browser.set_window_position(100,0)
		self.browser.set_window_size(1366, 1000)
	#login
		time.sleep(short_waiting)
		self.browser.get(url)
		self.login_Page = Login_Page(self.browser)
		self.Personal_Desktop = Personal_Desktop(self.browser)
		self.login_Page.sel_email()
		self.login_Page.input_email(account)
		self.login_Page.input_pwd(password)
		self.login_Page.click_login()
		time.sleep(long_waiting)
		self.login_Page.check_success()
	# create_CoSpace
		self.Personal_Desktop.create_cospace()
		time.sleep(short_waiting)
		self.Personal_Desktop.upload_cover()
		self.Personal_Desktop.cospace_name()
		time.sleep(short_waiting)
		self.Personal_Desktop.cospace_discription()
		self.Personal_Desktop.click_privacy()
		self.Personal_Desktop.sele_pri()
		time.sleep(short_waiting)
		self.Personal_Desktop.click_privacy()
		self.Personal_Desktop.sele_pub()
		time.sleep(short_waiting)
		self.Personal_Desktop.create_cospace_yes()
		time.sleep(3)
		self.Personal_Desktop.rename()	# rename_matter
		self.Personal_Desktop.drop_off()	# del_CoSpace
	#logout -  cancel
		time.sleep(short_waiting)
		self.Personal_Desktop.setting_menu()
		time.sleep(short_waiting)
		self.Personal_Desktop.logout()
		time.sleep(short_waiting)
		self.Personal_Desktop.logout_cancel()
	#logout -  yes
		time.sleep(short_waiting)
		self.Personal_Desktop.setting_menu()
		time.sleep(short_waiting)
		self.Personal_Desktop.logout()
		time.sleep(short_waiting)
		self.Personal_Desktop.logout_yes()

		print (raw_input("Press Enter to continue..."))	#system pending

if __name__ == '__main__':
	unittest.main()
