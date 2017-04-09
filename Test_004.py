#coding=utf-8
from appium import webdriver
import unittest
import os
import time
import HTMLTestRunner
import Common,BaseDriver
class Case(BaseDriver.Test):
    def test_01_SharePostal_Weixin(self):
        #分享我的名片
        el = Common.element(self.driver)
        el.waitByIdClick('btn_share')
        # 获取微信、朋友圈、QQ元素
        el.waitById('share_wx_persional')
        imageviews = el.getElementsByClassName('android.widget.ImageView')
        # 单击微信
        imageviews[0].click()
        el.waitByNameClick('简简丹丹')
        el.waitByNameClick('分享')
        el.waitByNameClick('返回兔博士经纪人版')
        el.waitById('btn_share')
    def test_02_SharePostal_Friend(self):
        #分享我的名片
        el = Common.element(self.driver)
        el.waitByIdClick('btn_share')
        # 获取微信、朋友圈、QQ元素
        el.waitById('share_wx_persional')
        imageviews = el.getElementsByClassName('android.widget.ImageView')
        # 单击朋友圈
        imageviews[1].click()
        el.waitByNameClick('发送')
        el.waitById('btn_share')
    def test_03_SharePostal_QQ(self):
        #分享我的名片
        el = Common.element(self.driver)
        el.waitByIdClick('btn_share')
        # 获取微信、朋友圈、QQ元素
        el.waitById('share_wx_persional')
        imageviews = el.getElementsByClassName('android.widget.ImageView')
        #单击QQ
        imageviews[2].click()
        el.waitByNameClick('丹丹')
        el.waitByNameClick('发送')
        el.waitByNameClick('返回兔博士经纪版')
        el.waitById('btn_share')