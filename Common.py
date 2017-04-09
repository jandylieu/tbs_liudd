#coding=utf-8
from appium import webdriver
import unittest
import os
import time
import HTMLTestRunner
from selenium.webdriver.support.ui import WebDriverWait
class element:
    def __init__(self, driver):
        self.driver = driver
    def clickById(self, id):
        self.driver.find_element_by_id('com.docrab.pro:id/'+id).click()
    def getElementById(self, id):
        ele=self.driver.find_element_by_id('com.docrab.pro:id/'+id)
        return ele
    def getElementsById(self,id):
        eles=self.driver.find_elements_by_id('com.docrab.pro:id/'+id)
        return eles
    def sendKeysById(self, id, key):
        self.driver.find_element_by_id('com.docrab.pro:id/'+id).send_keys(key)
    def clickByName(self, name):
        self.driver.find_element_by_name(name).click()
    def getElementByName(self,type):
        ele=self.driver.find_elements_by_name(type)
        return ele
    def getElementsByName(self,type):
        eles=self.driver.find_elements_by_name(type)
        return eles
    def sendKeysByName(self, name, key):
        self.driver.find_element_by_name(name).send_keys(key)
    def clickByClassName(self, type):
        self.driver.find_element_by_class_name(type).click()
    def getElementsByClassName(self,type):
        eles=self.driver.find_elements_by_class_name(type)
        return eles
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)
    def swipeUp(self,a,a1,b,b1,t):
        l=self.getSize()
        x=int(l[0]*a)
        x1=int(l[0]*b)
        y=int(l[1]*a1)
        y1=int(l[1]*b1)
        self.driver.swipe(x,y,x1,y1,t)
    def swipeDown(self, a, a1, b, b1, t):
        l = self.getSize()
        x = int(l[0] * a)
        x1 = int(l[0] * b)
        y = int(l[1] * a1)
        y1 = int(l[1] * b1)
        self.driver.swipe(x, y, x1, y1, t)
    def swipeLeft(self,a,a1,b,b1, t):
        l=self.getSize()
        x=int(l[0]*a)
        x1=int(l[0]*b)
        y=int(l[1]*a1)
        y1=int(l[1]*b1)
        self.driver.swipe(x, y, x1, y1, t)
    def tapSearch(self,a,b):
        l = self.getSize()
        x = int(l[0])
        y = int(l[1])
        self.driver.tap([(a * x, b * y)], )
    def waitByName(self,name):
        Wait = WebDriverWait(self.driver, 15)
        Wait.until(lambda x: self.driver.find_element_by_name(name).is_displayed())
    def waitById(self,id):
        Wait = WebDriverWait(self.driver, 90)
        string="com."
        if string in id:
            Wait.until(lambda x: self.driver.find_element_by_id(id).is_displayed())
        else:
            Wait.until(lambda x: self.driver.find_element_by_id('com.docrab.pro:id/' + id).is_displayed())
    def waitByNameClick(self,name):
        Wait = WebDriverWait(self.driver, 15)
        Wait.until(lambda x: self.driver.find_element_by_name(name).is_displayed())
        el=element(self.driver)
        el.clickByName(name)
    def waitByIdClick(self,id):
        Wait = WebDriverWait(self.driver, 30)
        string="com."
        #如果传的是系统的id
        if string in id:
            Wait.until(lambda x: self.driver.find_element_by_id(id).is_displayed())
            self.driver.find_element_by_id(id).click()
        else:
            Wait.until(lambda x: self.driver.find_element_by_id('com.docrab.pro:id/'+id).is_displayed())
            el = element(self.driver)
            el.clickById(id)

