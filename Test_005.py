#coding=utf-8
from appium import webdriver
import unittest
import os
import time
import HTMLTestRunner
import Common
import BaseDriver
class Case(BaseDriver.Test):
    def test_01_Owners(self):
        el=Common.element(self.driver)
        el.waitByNameClick('潜在房东')
        el.waitById('label')
        chats=el.getElementsByName('谈话')
        chats[0].click()
        #校验是否弹出扣除300积分对话框
        self.assertIn(u'300',el.getElementById('tv_info').text)
        el.waitByIdClick('ok')
        #单击新功能提示画面
        el.waitByIdClick('rc_plugin_toggle')
        #校验是否发送默认信息
        mesg=self.driver.find_element_by_id('android:id/text1')
        self.assertIn(u'UI',mesg.text)
        #获取返回键然后单击
        imageviews=el.getElementsByClassName('android.widget.ImageView')
        imageviews[0].click()
        el.waitByNameClick('主页')
        #校验跟进数量加1
        els=el.getElementsById('tv_right_top_count')
        self.assertEqual(u'1',els[0].text)
    def test_02_Buyers(self):
        el=Common.element(self.driver)
        el.clickByName('潜在买家')
        el.waitById('label')
        chats=el.getElementsByName('谈话')
        chats[0].click()
        #校验是否弹出扣除300积分对话框
        self.assertIn(u'300',el.getElementById('tv_info').text)
        el.waitByIdClick('ok')
        el.waitById('rc_plugin_toggle')
        #校验是否发送默认信息
        mesg=self.driver.find_element_by_id('android:id/text1')
        self.assertIn(u'UI',mesg.text)
        #获取返回键然后单击
        imageviews=el.getElementsByClassName('android.widget.ImageView')
        imageviews[0].click()
        el.waitByNameClick('主页')
        #校验跟进数量加1
        els=el.getElementsById('tv_right_top_count')
        self.assertEqual(u'2',els[0].text)
    def test_03_GetCustomers(self):
        el=Common.element(self.driver)
        el.waitByNameClick('跟进客户')
        el.waitById('txt_title')
        els=el.getElementsById('name')
        self.assertIsNotNone(els[0])
        self.assertIsNotNone(els[1])
