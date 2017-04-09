#coding=utf-8
from appium import webdriver
import unittest
import os
import time
import HTMLTestRunner
import Common
import BaseDriver,Conversation
# Returns abs path relative to this file and not cwd
# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__), p)
# )
class Case(BaseDriver.Test):
    def test_01_EstateHouse_Pub1(self):
        el=Common.element(self.driver)
        el.waitByNameClick('发布房源')
        #设为隐私房源
        el.waitByIdClick('iv_switcher')
        textviews=el.getElementsByClassName('android.widget.TextView')
        #设置小区名
        textviews[4].click()
        el.sendKeysById('etSearch',u"益丰新村")
        time.sleep(6)
        el.tapSearch(0.2,0.14)
        #设置属性
        textviews[6].click()
        el.waitByIdClick('tv_ok')
        #设置楼层
        edittexts=el.getElementsByClassName('android.widget.EditText')
        edittexts[0].send_keys('2')
        edittexts[1].send_keys('6')
        #设置户型
        textviews[9].click()
        el.swipeUp(0.25,0.9,0.25,0.8,500)
        el.swipeUp(0.75,0.9,0.75,0.7,500)
        el.waitByIdClick('tv_ok')
        #设置面积
        edittexts[2].send_keys('76')
        #设置朝向
        textviews[12].click()
        el.swipeUp(0.5,0.9,0.5,0.3,500)
        el.waitByIdClick('tv_ok')
        #设置持有年限
        textviews[14].click()
        el.swipeUp(0.5,0.9,0.5,0.8,500)
        el.waitByIdClick('tv_ok')
        #滑动界面
        el.swipeUp(0.5,0.9,0.5,0.2,1000)
        #设置房型图
        pics =el.getElementsById('iv_add_pic')
        pics[0].click()
        el.waitById('btnCancel')
        el.swipeLeft(0.5,0.7,0.2,0.7,500)
        el.waitByIdClick('iv_selector')
        el.waitByIdClick('btnOk')
        #设置图片
        pics[1].click()
        imageviews=el.getElementsById('image')
        for i in range(len(imageviews)):
            if i<=4:
                imageviews[i].click()
            else:
                break
        el.waitByIdClick('commit')
        el.sendKeysByName('增加房源可信度,吸引更多买家(选填)',u"周边环境好、朝向好")
        el.swipeUp(0.5, 0.9, 0.5, 0.4, 500)
        el.sendKeysByName('请输入',u"390")
        el.waitByIdClick('tv_confirm_btn')
        #确认返回主页（显示出小区下拉列表）
        el.waitById('txt_select_name')
        els=el.getElementsById('tv_middle_top_count')
        self.assertEqual(u'1',els[1].text)
    def test_02_EstateHouse_Pub0(self):
        el=Common.element(self.driver)
        el.waitByNameClick('发布房源')
        el.waitById('iv_switcher')
        textviews=el.getElementsByClassName('android.widget.TextView')
        #设置小区名
        textviews[4].click()
        el.sendKeysById('etSearch',u"民风小区")
        time.sleep(6)
        el.tapSearch(0.2,0.14)
        #设置属性
        textviews[6].click()
        el.waitByIdClick('tv_ok')
        #设置楼层
        edittexts=el.getElementsByClassName('android.widget.EditText')
        edittexts[0].send_keys('2')
        edittexts[1].send_keys('6')
        #设置户型
        textviews[9].click()
        el.swipeUp(0.25,0.9,0.25,0.8,500)
        el.swipeUp(0.75,0.9,0.75,0.7,500)
        el.waitByIdClick('tv_ok')
        #设置面积
        edittexts[2].send_keys('88')
        #设置朝向
        textviews[12].click()
        el.swipeUp(0.5,0.9,0.5,0.3,500)
        el.waitByIdClick('tv_ok')
        #设置持有年限
        textviews[14].click()
        el.swipeUp(0.5,0.9,0.5,0.8,500)
        el.waitByIdClick('tv_ok')
        #滑动界面
        el.swipeUp(0.5,0.9,0.5,0.2,1000)
        # 设置图片
        pics =el.getElementsById('iv_add_pic')
        pics[1].click()
        imageviews=el.getElementsById('image')
        for i in range(len(imageviews)):
            if i<=4:
                imageviews[i].click()
            else:
                break
        el.waitByIdClick('commit')
        el.sendKeysByName('增加房源可信度,吸引更多买家(选填)',u"周边环境好、朝向好")
        el.swipeUp(0.5, 0.9, 0.5, 0.4, 500)
        el.sendKeysByName('请输入',u"400")
        el.waitByIdClick('tv_confirm_btn')
        # 确认返回主页（显示出小区下拉列表）
        el.waitById('txt_select_name')
        els=el.getElementsById('tv_middle_top_count')
        self.assertEqual(u'2',els[1].text)
    def test_03_EstateVillas_Pub1(self):
        el=Common.element(self.driver)
        el.waitByNameClick('发布房源')
        #设置隐私房源
        el.waitByIdClick('iv_switcher')
        #设置小区名
        textviews=el.getElementsByClassName('android.widget.TextView')
        textviews[4].click()
        el.sendKeysById('etSearch',u"汤臣高尔夫别墅")
        time.sleep(5)
        el.tapSearch(0.2,0.14)
        #设置属性
        textviews[6].click()
        el.swipeUp(0.5,0.9,0.5,0.8,500)
        el.waitByIdClick('tv_ok')
        #设置面积
        edittexts=el.getElementsByClassName('android.widget.EditText')
        edittexts[0].send_keys('120')
        #设置持有年限
        textviews[9].click()
        el.swipeUp(0.5,0.9,0.5,0.8,500)
        el.waitByIdClick('tv_ok')
        #设置图片
        el.waitByIdClick('iv_add_pic')
        imageviews=el.getElementsById('image')
        for i in range(len(imageviews)):
            if i<=4:
                imageviews[i].click()
            else:
                break
        el.waitByIdClick('commit')
        #滑动界面
        el.swipeUp(0.5,0.9,0.5,0.7,500)
        edittexts[1].send_keys(u"周边环境好、朝向好")
        edittexts[2].send_keys(u"990")
        el.waitByIdClick('tv_confirm_btn')
        # 确认返回主页（显示出小区下拉列表）
        el.waitById('txt_select_name')
        els=el.getElementsById('tv_middle_top_count')
        self.assertEqual(u'3',els[1].text)
    def test_04_EstateVillas_Pub0(self):
        el=Common.element(self.driver)
        el.waitByNameClick('发布房源')
        #设置小区名
        el.waitById('iv_switcher')
        textviews=el.getElementsByClassName('android.widget.TextView')
        textviews[4].click()
        el.sendKeysById('etSearch',u"天安别墅")
        time.sleep(5)
        el.tapSearch(0.2,0.14)
        #设置属性
        textviews[6].click()
        el.swipeUp(0.5,0.9,0.5,0.8,500)
        el.waitByIdClick('tv_ok')
        #设置面积
        edittexts=el.getElementsByClassName('android.widget.EditText')
        edittexts[0].send_keys('130')
        #设置持有年限
        textviews[9].click()
        el.swipeUp(0.5,0.9,0.5,0.8,500)
        el.waitByIdClick('tv_ok')
        #设置图片
        el.waitByIdClick('iv_add_pic')
        imageviews=el.getElementsById('image')
        for i in range(len(imageviews)):
            if i<=4:
                imageviews[i].click()
            else:
                break
        el.waitByIdClick('commit')
        #滑动界面
        el.swipeUp(0.5,0.9,0.5,0.7,500)
        edittexts[1].send_keys(u"周边环境好、朝向好")
        edittexts[2].send_keys(u"1120")
        el.waitByIdClick('tv_confirm_btn')
        # 确认返回主页（显示出小区下拉列表）
        el.waitById('txt_select_name')
        els=el.getElementsById('tv_middle_top_count')
        self.assertEqual(u'4',els[1].text)
    def test_05_EstateShare_Weixin(self):
        el=Common.element(self.driver)
        el.waitByNameClick('已发布房源')
        time.sleep(5)
        #获取分享元素
        textviews=el.getElementsByName('分享')
        textviews[0].click()
        el.waitById('share_wx_persional')
        #获取微信、朋友圈、QQ元素
        imageviews=el.getElementsByClassName('android.widget.ImageView')
        #单击微信
        imageviews[0].click()
        el.waitByNameClick('简简丹丹')
        el.waitByNameClick('分享')
        el.waitByNameClick('返回兔博士经纪人版')
        el.waitById('tv_title_bar_title')
        #校验分享次数加1
        els=el.getElementsById('read_count')
        self.assertIn(u'1',els[0].text)
    def test_06_EstateShare_Friend(self):
        el=Common.element(self.driver)
        #获取分享元素
        textviews=el.getElementsByName('分享')
        textviews[0].click()
        el.waitById('share_wx_persional')
        #获取微信、朋友圈、QQ元素
        imageviews=el.getElementsByClassName('android.widget.ImageView')
        #单击朋友圈
        imageviews[1].click()
        el.waitByNameClick('发送')
        el.waitById('tv_title_bar_title')
        #校验分享次数加1
        els=el.getElementsById('read_count')
        self.assertIn(u'2',els[0].text)
    def test_07_EstateShare_QQ(self):
        el=Common.element(self.driver)
        #获取分享元素
        textviews=el.getElementsByName('分享')
        textviews[0].click()
        el.waitById('share_wx_persional')
        #获取微信、朋友圈、QQ元素
        imageviews=el.getElementsByClassName('android.widget.ImageView')
        #单击QQ
        imageviews[2].click()
        el.waitByNameClick('丹丹')
        el.waitByNameClick('发送')
        el.waitByNameClick('返回兔博士经纪版')
        el.waitById('tv_title_bar_title')
        #校验分享次数加1
        els=el.getElementsById('read_count')
        self.assertIn(u'3',els[0].text)
    def test_08_EstateDelete(self):
        el=Common.element(self.driver)
        el.waitById('tv_title_bar_title')
        #获取删除元素
        dels=el.getElementsById('tv_delete_private')
        dels[0].click()
        time.sleep(3)
        #校验删除成功
        housenames=el.getElementsById('house_name')
        self.assertEqual(u'益丰新村',housenames[0].text)
    def test_09_EstateRefresh(self):
        el=Common.element(self.driver)
        #获取刷新元素
        res=el.getElementsById('tv_refresh')
        res[0].click()
        el.waitById('tv_info')
        #对话框中单击确定（扣除100积分）
        self.assertIn(u'100', el.getElementById('tv_info').text)
        el.waitByIdClick('ok')
    def test_10_SamePlateEstateList(self):
        el=Conversation.Case(self.driver)
        el.test_PotentialEstateList(u'潜在房源',u'3')
    def test_11_PotentialEstateList(self):
        el = Conversation.Case(self.driver)
        el.test_PotentialEstateList(u'同板块房源',u'4')


