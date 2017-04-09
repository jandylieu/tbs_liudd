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
    def test_01_Updeal(self):
        el = Common.element(self.driver)
        el.waitByName(u'发布房源')
        el.swipeUp(0.5,0.9,0.5,0.3,500)
        el.waitByNameClick(u'上传成交')
        textviews = el.getElementsByClassName('android.widget.TextView')
        # 设置小区名
        textviews[2].click()
        el.sendKeysById('etSearch', u"益丰新村")
        time.sleep(2)
        el.tapSearch(0.2,0.14)
        time.sleep(2)
        # 设置属性
        textviews[4].click()
        el.waitByIdClick('tv_ok')
        # 设置楼栋、楼层、面积、真实成交价
        edittexts = el.getElementsByClassName('android.widget.EditText')
        keys=['12','502','2','6','76','390']
        for i in range(len(edittexts)):
            edittexts[i].send_keys(keys[i])
        # 设置户型
        textviews[8].click()
        el.swipeUp(0.25, 0.9, 0.25, 0.8, 500)
        el.swipeUp(0.75, 0.9, 0.75, 0.7, 500)
        el.waitByIdClick('tv_ok')
        # 设置朝向
        textviews[11].click()
        el.swipeUp(0.5, 0.9, 0.5, 0.3, 500)
        el.waitByIdClick('tv_ok')
        # 设置成交日期
        textviews[13].click()
        el.waitByIdClick('tv_ok')
        # 上传合同
        el.waitByIdClick('iv_add_pic')
        imageviews = el.getElementsById('image')
        for i in range(len(imageviews)):
            if i <= 2:
                imageviews[i].click()
            else:
                break
        el.waitByIdClick('commit')
        el.swipeUp(0.5,0.6,0.5,0.3,500)
        el.waitByIdClick('tv_confirm_btn')
        el.waitByName(u'推广效果')
        el.swipeDown(0.5,0.3,0.5,0.9,500)
        el.waitById('tv_deal_count')
        self.assertEqual(u'1套', el.getElementById('tv_deal_count').text)
    def test_02_Scan(self):
        el = Common.element(self.driver)
        el.swipeUp(0.5, 0.9, 0.5, 0.3, 500)
        el.waitByNameClick('主营小区浏览')
        el.waitByName('上海康城')
        textviews=el.getElementsById('community_name')
        for i in range(len(textviews)):
            housenames=[u"民风小区",u"益丰新村",u"上海康城"]
            self.assertIn(textviews[i].text, housenames)
    def test_03_Recommend(self):
        el = Common.element(self.driver)
        el.waitByNameClick('您被推荐')
        el.waitByName('上海康城')
        textviews=el.getElementsById('community_name')
        for i in range(len(textviews)):
            housenames=[u"民风小区",u"益丰新村",u"上海康城"]
            self.assertIn(textviews[i].text, housenames)
    def test_04_EstateClicked(self):
        el=Common.element(self.driver)
        el.clickByName('房源点击')
        el.waitByName('天安别墅')
        housenames=el.getElementsById('tv_address')
        self.assertEqual(housenames[0].text,u'天安别墅')
        self.assertEqual(housenames[1].text,u'民风小区')
        self.assertEqual(housenames[2].text,u'益丰新村')





