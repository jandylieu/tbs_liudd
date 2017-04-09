#coding=utf-8
from appium import webdriver
import unittest
import os
import time
import HTMLTestRunner
import Common,BaseDriver
class Case(BaseDriver.Test):
    def test_01_SetStore(self):
        # 设置公司和门店：
        el = Common.element(self.driver)
        el.waitByIdClick('tv_community_name')
        # 检测当前页是否为设置公司和门店：
        el.waitById('tv_title_bar_title')
        self.assertEqual(el.getElementById('tv_title_bar_title').text, u'完善资料')
        edittexts = el.getElementsByClassName('android.widget.EditText')
        arrays = [u"链家", u"张江店"]
        for i in range(len(edittexts)):
            edittexts[i].click()
            el.sendKeysById('etSearch', arrays[i])
            time.sleep(2)
            el.tapSearch(0.2, 0.14)
            time.sleep(2)
        el.clickById('btnFinish')
        el.waitById('tv_title_bar_title')
        # 校验是否设置成功
        self.assertIsNotNone(el.getElementById('tv_title_bar_title'))
        self.assertEqual(el.getElementById('tv_title_bar_title').text, u'选择主营小区')
    def test_02_SetHouse(self):
        #设置主营小区：
        el = Common.element(self.driver)
        housenames=el.getElementsByClassName('android.widget.EditText')
        lables=el.getElementsByName('请选择标签')
        for i in range(len(housenames)):
            arrays=[u"民风小区",u"益丰新村",u"上海康城"]
            housenames[i].click()
            el.sendKeysById('etSearch', arrays[i])
            time.sleep(2)
            el.tapSearch(0.2,0.14)
            lables[0].click()
            if i==1:
                el.swipeUp(0.5,0.9,0.5,0.8,500)
            elif i==2:
                el.swipeUp(0.5,0.9,0.5,0.7,500)
            else:
                pass
            el.clickById('tv_ok')
        el.clickById('btnFinish')
        el.waitById('tv_community_count')
        # 校验是否设置成功
        self.assertEqual(el.getElementById('tv_community_count').text, u'3个')
