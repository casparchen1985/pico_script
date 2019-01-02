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
account02 = "selenium02@mailinator.com"
password = "qa123456"
password02 = "qa123456"
long_waiting = 5
short_waiting = 1
friend = "Selenium01"
friend02 = "Selenium02"

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

class call_test(unittest.TestCase):
	def test_1(self):
	#setup
		self.browser = webdriver.Chrome(chrome_options=opt)
		self.browser.set_window_position(100,0)
		self.browser.set_window_size(1366, 700)

		self.browser02 = webdriver.Chrome(chrome_options=opt)
		self.browser02.set_window_position(100,730)
		self.browser02.set_window_size(1366, 700)

	#login
		time.sleep(short_waiting)
		self.browser.get(url)
		self.browser02.get(url)
		self.login_Page = Login_Page(self.browser)
		self.login_Page02 = Login_Page(self.browser02)
		self.Personal_Desktop = Personal_Desktop(self.browser)
		self.Personal_Desktop02 = Personal_Desktop(self.browser02)
		self.login_Page.sel_email()
		self.login_Page02.sel_email()
		self.login_Page.input_email(account)
		self.login_Page02.input_email(account02)
		self.login_Page.input_pwd(password)
		self.login_Page02.input_pwd(password02)
		self.login_Page.click_login()
		self.login_Page02.click_login()
		time.sleep(long_waiting)
		self.login_Page.check_success()
		self.login_Page02.check_success()

		self.Personal_Desktop.desktop_call_friend(friend02)
		time.sleep(short_waiting)
		self.Personal_Desktop.check_call_out_view(friend02)
		time.sleep(short_waiting)
		self.Personal_Desktop02.check_call_in_view(friend) #check caller
		self.Personal_Desktop02.pick_up_call()	#pick-up
		time.sleep(long_waiting)
		self.Personal_Desktop02.hang_up_call()  # hang-up

		self.Personal_Desktop.desktop_call_friend(friend02)
		time.sleep(short_waiting)
		self.Personal_Desktop.check_call_out_view(friend02)
		time.sleep(short_waiting)
		self.Personal_Desktop02.check_call_in_view(friend) #check caller
		self.Personal_Desktop.cancel_call()		#cancel call


		print raw_input("Press Enter to continue...")	#system pending

if __name__ == '__main__':
	unittest.main()
