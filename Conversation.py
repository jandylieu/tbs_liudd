# coding=utf-8
from appium import webdriver
import unittest
import os
import time
import HTMLTestRunner
import Common
import BaseDriver,Test_006
class Case(BaseDriver.Test):
    def __init__(self, driver):
        self.driver = driver
    def test_PotentialEstateList(self,tablename,count):
        el=Common.element(self.driver)
        if tablename == u"潜在房源":
            textviews = el.getElementsByClassName('android.widget.TextView')
            textviews[2].click()
        else:
            el.waitByNameClick(tablename)
        time.sleep(3)
        els = el.getElementsById('conversation')
        els[0].click()
        self.assertIn(u'300', el.getElementById('tv_info').text)
        el.waitByIdClick('ok')
        el.waitByIdClick('rc_plugin_toggle')
        # 校验是否发送默认信息
        mesg = self.driver.find_element_by_id('android:id/text1')
        self.assertIn(u'UI', mesg.text)
        # 获取返回键然后单击
        imageviews = el.getElementsByClassName('android.widget.ImageView')
        imageviews[0].click()
        el.waitById('publish')
        els=el.getElementsById('publish')
        self.assertIn(u'接受并发布',els[0].text)
        el.waitByNameClick('主页')
        # 校验跟进数量加1
        els = el.getElementsById('tv_right_top_count')
        self.assertIn(count, els[0].text)
