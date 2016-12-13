#!/bin/bash

from base.get_conf import GetConf
from selenium import webdriver
from selenium.webdriver.common.by import By


class BaiduPO(GetConf):

    conf = GetConf()

    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(conf.get_value('default', 'default', 'wait_time'))

    url = conf.get_value('default', 'default', 'base_url')
    print url
    driver.get(url)

    def clickNomi(self):
        conf = self.conf
        class_name = conf.get_value('baidu', 'class_name', 'nuomi')
        self.driver.find_element(By.CLASS_NAME, class_name).click()

    def quit(self):
        self.driver.quit()

# a = BaiduPO()
# a.clickNomi()



