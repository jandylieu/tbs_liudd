#coding=utf-8
from appium import webdriver
import unittest
import os
import time
import HTMLTestRunner
import Common
import BaseDriver
# Returns abs path relative to this file and not cwd
# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__), p)
# )
class Case(BaseDriver.Test):
    #活动福利：
    def test_01_Activities(self):
        el=Common.element(self.driver)
        el.waitByNameClick('我的')
        el.waitByNameClick('活动福利')
        # 领取每日福利
        el.waitByName('分享我的名片1次')
        buttons=el.getElementsById('stv_score')
        buttons[3].click()
        time.sleep(2)
        #领取成长福利
        el.clickById('rb_right_button')
        el.waitByNameClick('+800积分')
        time.sleep(2)
        el.clickById('iv_task_box')
        el.waitById(txt_sign_day.text)
        self.assertEqual(txt_sign_day.text, u'1')
        el.tapSearch(0.1, 0.1)
        el.waitByIdClick('iv_back')
    def test_02_Account(self):
        el = Common.element(self.driver)
        el.waitByNameClick('积分及奖励')
        el.waitByNameClick('奖励记录')
        counts=el.getElementsById('tv_integal_count')
        self.assertEqual(counts[0].text, u'+1200')
        self.assertEqual(counts[1].text, u'+300')

