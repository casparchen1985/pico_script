# -*- coding: UTF-8 -*-
import time
import sys
import os
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

long_waiting = 5
short_waiting = 1
parent_path = os.getcwd()
file_lst = [
    '01.jpg', '02.jpeg', '03.png', '04.bmp', '05.gif', '06.mp3', '07.aac', '08.m4a', '09.wmv', '10.mp4',
    '11.mov', '12.doc', '13.docx', '14.xls', '15.xlsx', '16.ppt', '17.pptx', '19.pdf', '20.zip',
    '21.txt', '22.txt', '23.txt', '24', '25.pages', '26.rar',
    '27.檔名超級長939歲，鬼怪。身披血光、手撕敵軍的他是名副其實的戰神，但他卻死在自己所守護的主君刀下，只為了堅守對先王的承諾。從那開始的939年間一直作為鬼怪活著，就像在心.png']
video_ext = ['mov', 'mp4', 'wmv']
pic_ext = ['jpg','jpeg','png','bmp','gif']
audio_ext = ['mp3','aac','m4a']
office_ext = ['doc','docx','xls','xlsx','ppt','pptx']
compressed_ext = ['zip','rar']
nonsupport_ext = ['pages']
pdf_ext = ['pdf']

class Personal_Desktop(object):
    def __init__(self, browser):
        self.browser = browser

    def get_date(self):
        DATE = time.strftime("%H:%M:%S %d-%m-%Y", time.localtime())
        return DATE

    def mouse_over(self, point):
        Action = ActionChains(self.browser)
        Action.move_to_element(point).perform()

    def setting_menu(self):
        setting_btn = self.browser.find_element_by_xpath("/html/body/ui-view/ui-view/div[2]/div/div[4]/div[5]/div/div[2]/ul[1]/li/div/div/div[1]/article[1]/i")
        time.sleep(short_waiting)
        self.mouse_over(setting_btn)
        time.sleep(short_waiting)
        setting_btn.click()

    def logout(self):
        logout_btn = self.browser.find_element_by_xpath("/html/body/ui-view/ui-view/div[2]/div/div[4]/div[5]/div/div[2]/ul[1]/li/div/div/div[2]/div[1]/div/ul/li[4]")
        logout_btn.click()
        
    def logout_yes(self):
        yes_btn = self.browser.find_element_by_xpath("/html/body/div[5]/div/div[3]/button[2]")
        yes_btn.click()
        try:
            self.browser.find_element_by_css_selector("body > ui-view > ui-view > div > div > div.main-wrap > div.operation-pane > ng-include > div > section:nth-child(1) > ng-include > form > div.login-logo > img").is_displayed()
            print "Logout successfully"
        except:
            print "Logout unsuccessfully"
            sys.exit()

    def logout_cancel(self):
        cancel_btn = self.browser.find_element_by_xpath("/html/body/div[5]/div/div[3]/button[1]")
        cancel_btn.click()

    def create_cospace(self):
        create_cospace_btn = self.browser.find_element_by_css_selector("body > ui-view > ui-view > div.main-space.ng-scope > div > div.home-garden.ng-scope > div > ul.tools.top > li:nth-child(4) > a > i")
        create_cospace_btn.click()

    def upload_cover(self):
        cover_lst = ['Argon18.jpg','Bianchi.jpg','FACTOR.jpg','LaPierre.jpeg','Pinarello.jpeg']
        cover = random.choice(cover_lst)
        cover_btn = self.browser.find_element_by_css_selector("body > div.blockUI.blockMsg.blockPage > div > ng-include > form > div.center > div.cover-picture > input")
        cover_btn.send_keys(parent_path + '/cover/' + cover)
        print ("This cover is " + cover)

    def cospace_name(self):
        name = 'AutoTest ' + self.get_date()
        name_colum = self.browser.find_element_by_css_selector("body > div.blockUI.blockMsg.blockPage > div > ng-include > form > div.center > div:nth-child(3) > input").send_keys(name)

    def cospace_discription(self):
        discription = 'AutoTest Discription: ' + self.get_date()
        discription_colum = self.browser.find_element_by_css_selector("body > div.blockUI.blockMsg.blockPage > div > ng-include > form > div.center > div:nth-child(4) > textarea").send_keys(discription)

    def click_privacy(self):
        privacy = self.browser.find_element_by_css_selector("body > div.blockUI.blockMsg.blockPage > div > ng-include > form > div.center > div:nth-child(5) > u3d-dropdown-list > div > div > button > i")
        self.mouse_over(privacy)
        privacy.click()

    def sele_pri(self):
        pri = self.browser.find_element_by_css_selector("body > div.blockUI.blockMsg.blockPage > div > ng-include > form > div.center > div:nth-child(5) > u3d-dropdown-list > div > div > div > ul > li:nth-child(1)")
        self.mouse_over(pri)
        pri.click()

    def sele_pub(self):
        pub = self.browser.find_element_by_css_selector("body > div.blockUI.blockMsg.blockPage > div > ng-include > form > div.center > div:nth-child(5) > u3d-dropdown-list > div > div > div > ul > li:nth-child(2)")
        self.mouse_over(pub)
        pub.click()
        yes_btn = self.browser.find_element_by_css_selector("body > div.blockUI.blockMsg.blockPage > div > div.blockUI.blockMsg.blockElement > div > div.footer > button.action-enter")
        yes_btn.click()

    def create_cospace_yes(self):
        yes_btn = self.browser.find_element_by_css_selector("body > div.blockUI.blockMsg.blockPage > div > ng-include > form > div.south > input.u3d-btn-01.confirm")
        yes_btn.click()
        time.sleep(long_waiting)
        close = self.browser.find_element_by_xpath("//u3d-work-viewer/ul/li[3]/a/i")
        close.click()
        
    def create_cospace_cancel(self):
        cancel_btn = self.browser.find_element_by_css_selector("body > div.blockUI.blockMsg.blockPage > div > ng-include > form > div.south > input.u3d-btn-01.cancel")
        cancel_btn.click()

    def sel_matter(self):
        matter = self.browser.find_element_by_xpath("/html/body/ui-view/ui-view/div[2]/div/div[4]/div[3]/div/div/div/article[1]/h3")
        matter_name = matter.text
        self.mouse_over(matter)
        check_box = self.browser.find_element_by_css_selector("body > ui-view > ui-view > div.main-space.ng-scope > div > div.desktop.ng-scope.history-open > div.pt-main.pt-perspective.ng-scope.ng-isolate-scope > div > div > div > article:nth-child(1) > input").click()
        print (matter_name + " has been selected")
        return (check_box, matter_name)

    def open_context_menu(self):
        target , matter_name = self.sel_matter()
        Action = ActionChains(self.browser)
        Action.context_click(target).perform()
        context_menu = self.browser.find_element_by_xpath("//ul[@class='context-menu-list context-menu-root']")
        return (context_menu, matter_name)

    def drop_off(self):
        context_menu , matter_name = self.open_context_menu()
        self.mouse_over(context_menu)
        time.sleep(short_waiting)
        self.browser.find_element_by_xpath("/html/body/ul[2]/li[1]").click()
        try:
            self.browser.find_element_by_css_selector("body > div.ui-pnotify.normal-center > div > div.ui-pnotify-content > div.ui-pnotify-icon") == True
            print (matter_name + " has been deleted")
        except:
            print ("Delete matter/file is failed")
            sys.exit()

    def rename(self):
        context_menu = self.open_context_menu()
        self.browser.find_element_by_xpath("/html/body/ul[2]/li[2]/span").click()
        DATE = 'Changed ' + self.get_date()
        colum = self.browser.find_element_by_xpath("//form/input[@type='text'][@name='matter[title]']")
        colum.clear()
        colum.send_keys(DATE + Keys.HOME)
        time.sleep(2)
        colum.send_keys(Keys.ENTER)

    def desktop_search_friend(self,nickname):
        try:
            search_colum = self.browser.find_element_by_css_selector("body > ui-view > ui-view > div.main-space.ng-scope > div > div.home-drawer.ng-scope > div > div.drawer-menu.ng-scope > div.block.contacts-block > div > div.search-region.show > input")
        except:
            self.browser.find_element_by_css_selector("body > ui-view > ui-view > div.main-space.ng-scope > div > div.home-drawer.ng-scope > div > div.drawer-menu.ng-scope > div.block.contacts-block > header > ul > li:nth-child(3) > i").click()

        search_colum = self.browser.find_element_by_css_selector("body > ui-view > ui-view > div.main-space.ng-scope > div > div.home-drawer.ng-scope > div > div.drawer-menu.ng-scope > div.block.contacts-block > div > div.search-region.show > input")
        search_colum.clear()
        search_colum.send_keys(nickname)
        time.sleep(short_waiting)

    def desktop_info_of_friend(self,nickname):
        self.desktop_search_friend(nickname)
        friend_lst = self.browser.find_element_by_xpath("//h5[@class='friend-name ng-binding']")
        self.mouse_over(friend_lst)
        time.sleep(short_waiting)

    def desktop_call_friend(self,nickname):
        self.desktop_info_of_friend(nickname)
        phone_btn = self.browser.find_element_by_xpath("//ul/li/div/i[@class='icon-call022']").click()
        time.sleep(short_waiting)

    def check_call_out_view(self,nickname):
        self.browser.find_element_by_css_selector("#outgoing-call > div.video-call-title-bar.ng-scope > span").is_displayed()
        self.browser.find_element_by_css_selector("#outgoing-call-toolbar > a > i").is_displayed()
        assert self.browser.find_element_by_css_selector("#outgoing-call > div.video-call-title-bar.ng-scope > span").text == nickname
        print ("Call to " + nickname + " successfully")

    def check_call_in_view(self,nickname):
        self.browser.find_element_by_css_selector("#incoming-call > div.video-call-title-bar.ng-scope").is_displayed()
        self.browser.find_element_by_css_selector(
            "#incoming-call-toolbar > a:nth-child(2)").is_displayed()
        assert self.browser.find_element_by_css_selector("#incoming-call > div.video-call-title-bar.ng-scope > span").text == nickname
        print ("Call from " + nickname + " confirmed")

    def pick_up_call(self):
        wrong = 0
        self.browser.find_element_by_css_selector("#incoming-call-toolbar-accept > i").is_displayed()
        self.browser.find_element_by_css_selector("#incoming-call-toolbar-accept > i").click()
        time.sleep(long_waiting)
        if self.browser.find_element_by_css_selector("#video-call-toolbar > a:nth-child(1) > i").is_displayed():
            print "Mute button is exist"
        else:
            print "Mute button is not exist"
            sys.exit()

    def hang_up_call(self):
        self.browser.find_element_by_css_selector("#video-call-toolbar > a:nth-child(2) > i").is_displayed()
        time.sleep(short_waiting)
        self.browser.find_element_by_css_selector("#video-call-toolbar > a:nth-child(2) > i").click()
        time.sleep(short_waiting)
        try:
            self.browser.find_element_by_css_selector("#incoming-call").is_displayed()
            print "Fail to hang up the phone"
            sys.exit()
        except:
            print "Hang up the phone call successfully"

    def cancel_call(self):
        self.browser.find_element_by_css_selector("#outgoing-call-toolbar > a > i").is_displayed()
        self.browser.find_element_by_css_selector("#outgoing-call-toolbar > a > i").click()
        time.sleep(short_waiting)
        try:
            self.browser.find_element_by_css_selector("#outgoing-call > div.video-call-title-bar.ng-scope > span") == True
            wrong = 1
        except:
            print "Canceled the phone call"
            wrong = 0
        if wrong is not 0:
            print "Cancel phone call is failed"
            wrong = 0

    def upload_file(self):
        file_fullname = random.choice(file_lst)
        name_split = file_fullname.split('.')
        print ("Chose file randomly: " + file_fullname)
        print ("Extension is " + name_split[-1])
        self.browser.find_element_by_css_selector("body > ui-view > ui-view > div.main-space.ng-scope > div > div.home-garden.ng-scope > div > ul.tools.top > li:nth-child(1) > a > i").click()
        time.sleep(short_waiting)
        select_btn = self.browser.find_element_by_xpath("//*[@id='file-upload']/div/div/div/div[1]/input")
        select_btn.send_keys(parent_path + '/file/' + file_fullname)
        if name_split[-1] in video_ext:
            time.sleep(long_waiting)
        else: time.sleep(short_waiting)
        dt_area = self.browser.find_element_by_xpath("//*[@id='file-upload']")
        self.mouse_over(dt_area)
        dt_area.click()
        time.sleep(short_waiting)
        matter_name = self.browser.find_element_by_xpath("/html/body/ui-view/ui-view/div[2]/div/div[4]/div[3]/div/div/div/article[1]/h3").text
        try:
            assert matter_name == file_fullname
            print ("File " + file_fullname + " has been uploaded successfully")
        except:
            print ("Matter name is " + matter_name + ", but the file name is " + file_fullname)
            sys.exit()
        return (file_fullname)

    def open_matter(self):
        file_fullname = self.upload_file()
        matter_name = self.browser.find_element_by_css_selector("body > ui-view > ui-view > div.main-space.ng-scope > div > div.desktop.ng-scope.history-open > div.pt-main.pt-perspective.ng-scope.ng-isolate-scope > div > div > div > article:nth-child(1) > h3").text
        try:
            matter_name == file_fullname
            print ("Upload file : " + matter_name + ", confirmed")
        name_split = file_fullname.split('.')
        if len(name_split[]) == 1:
            #處理無副檔名
        elif name_split[-1] in pic_ext:
            #picture
        elif name_split[-1] in audio_ext:
            #audio
        elif name_split[-1] in video_ext:
            #video
        elif name_split[-1] in office_ext:
            #office
        elif name_split[-1] in compressed_ext:
            #壓縮檔
        elif name_split[-1] == 'pdf':
            #pdf
        elif name_split[-1] == 'txt':
            # txt
        else:       #nonsupport_ext
