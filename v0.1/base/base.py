#!/bin/bash
from selenium import webdriver


class Base(object):

    def get(self,driver,url):
        driver.get(url)

    def click(self,element):
        element.click()

    def input(self,element,text):
        element.clear()
        element.send_keys(text)


