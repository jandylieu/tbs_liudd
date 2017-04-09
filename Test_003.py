#coding=utf-8
from appium import webdriver
import unittest
import os
import time
import HTMLTestRunner
import Common,BaseDriver


class Case(BaseDriver.Test):
    #编辑用户信息：上传头像、名片等：
    def test_01_ModifyUser_gallery(self):
        el=Common.element(self.driver)
        el.waitByNameClick('我的')
        #单击头像进入个人资料画面
        ImageViews=el.getElementsByClassName('android.widget.ImageView')
        ImageViews[0].click()
        #设置头像
        ImageViews = el.getElementsByClassName('android.widget.ImageView')
        ImageViews[0].click()
        el.clickByName('相册照片')
        el.clickByName('相机')
        el.waitByName('选择图片')
        el.tapSearch(0.13,0.2)
        for i in range(2):
            el.waitByIdClick('com.android.gallery3d:id/head_select_right')
        el.waitById('tv_title_bar_title')
        #修改所属公司门店
        TextViews=el.getElementsByClassName('android.widget.TextView')
        TextViews[10].click()
        el.sendKeysById('etSearch',u"链家")
        time.sleep(2)
        el.tapSearch(0.2,0.14)
        TextViews[12].click()
        el.sendKeysById('etSearch', u"张江店")
        time.sleep(2)
        el.tapSearch(0.2,0.14)
        #修改主营小区
        TextViews[14].click()
        housenames=el.getElementsByClassName('android.widget.EditText')
        lables=el.getElementsByClassName('android.widget.ImageView')
        for i in range(len(housenames)):
            arrays=[u"民风小区",u"益丰新村",u"上海康城"]
            housenames[i].click()
            el.sendKeysById('etSearch', arrays[i])
            time.sleep(2)
            el.tapSearch(0.2,0.14)
            time.sleep(2)
            if i==1:
                lables[5].click()
                el.swipeUp(0.5,0.9,0.5,0.8,500)
            elif i==2:
                lables[8].click()
                el.swipeUp(0.5,0.9,0.5,0.7,500)
            else:
                lables[2].click()
                pass
            el.clickById('tv_ok')
        el.clickById('btnFinish')
        el.waitById('tv_title_bar_title')
        # 校验是否设置成功
        self.assertEqual(TextViews[15].text, u'3个')
        #设置名片
        ImageViews[1].click()
        el.clickByName('相册照片')
        el.clickByName('相机')
        el.waitByName('选择图片')
        el.tapSearch(0.37,0.34)
        for i in range(2):
            el.waitByIdClick('com.android.gallery3d:id/head_select_right')
        el.waitById('tv_title_bar_title')
        el.swipeUp(0.5,0.6,0.5,0.3,500)
        el.clickById('btnFinish')
        el.waitById('user_image')
        # 校验是否设置成功
        textViews=el.getElementsById('tab_indicator_name')
        self.assertEqual(textViews[3].text, u'我的')
    def test_02_ModifyUser_camera(self):
        el=Common.element(self.driver)
        #单击头像进入个人资料画面
        ImageViews=el.getElementsByClassName('android.widget.ImageView')
        ImageViews[0].click()
        #设置头像
        ImageViews = el.getElementsByClassName('android.widget.ImageView')
        ImageViews[0].click()
        el.clickByName('拍摄照片')
        el.waitByIdClick('com.huawei.camera:id/shutter_button')
        el.waitByIdClick('com.huawei.camera:id/btn_done')
        el.waitByIdClick('com.android.gallery3d:id/head_select_right')
        el.waitById('tv_title_bar_title')
        #修改所属公司门店
        TextViews=el.getElementsByClassName('android.widget.TextView')
        TextViews[10].click()
        el.sendKeysById('etSearch',u"链家")
        time.sleep(2)
        el.tapSearch(0.2,0.14)
        TextViews[12].click()
        el.sendKeysById('etSearch', u"张江店")
        time.sleep(2)
        el.tapSearch(0.2,0.14)
        #修改主营小区
        TextViews[14].click()
        housenames=el.getElementsByClassName('android.widget.EditText')
        lables=el.getElementsByClassName('android.widget.ImageView')
        for i in range(len(housenames)):
            arrays=[u"民风小区",u"益丰新村",u"上海康城"]
            housenames[i].click()
            el.sendKeysById('etSearch', arrays[i])
            time.sleep(2)
            el.tapSearch(0.2,0.14)
            time.sleep(2)
            if i==1:
                lables[5].click()
                el.swipeUp(0.5,0.9,0.5,0.8,500)
            elif i==2:
                lables[8].click()
                el.swipeUp(0.5,0.9,0.5,0.7,500)
            else:
                lables[2].click()
                pass
            el.clickById('tv_ok')
        el.clickById('btnFinish')
        el.waitById('tv_title_bar_title')
        # 校验是否设置成功
        self.assertEqual(TextViews[15].text, u'3个')
        #设置名片
        ImageViews[1].click()
        el.clickByName('拍摄照片')
        el.waitByIdClick('com.huawei.camera:id/shutter_button')
        el.waitByIdClick('com.huawei.camera:id/btn_done')
        el.waitByIdClick('com.android.gallery3d:id/head_select_right')
        el.waitById('tv_title_bar_title')
        #滑动页面
        el.swipeUp(0.5,0.6,0.5,0.3,500)
        el.clickById('btnFinish')
        el.waitById('user_image')
        # 校验是否设置成功
        textViews=el.getElementsById('tab_indicator_name')
        self.assertEqual(textViews[3].text, u'我的')






