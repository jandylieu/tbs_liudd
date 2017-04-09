#coding=utf-8
from appium import webdriver
import unittest
import os
import time
import HTMLTestRunner
import Common,BaseDriver
class Case(BaseDriver.Test):
    # def test_login(self):
    #     textfields = getListByClassName('android.widget.EditText')
    #     textfields[0].send_keys('13999999999')
    #     textfields[1].send_keys('1688')
    #     el = Common.element(self.driver)
    #     el.clickById('btnLogin')
    #     time.sleep(5)
    #     self.assertEqual(getElementById('tv_name').text, u'UI自动化')
    #确认注册、广告弹框、积分弹框：
    def test_Register(self):
        el=Common.element(self.driver)
        el.waitByIdClick('btnRegister')
        edittexts=el.getElementsByClassName('android.widget.EditText')
        arrays = [u'UI自动化','', '13999999999','1688',u'015s8']
        for i in range(len(edittexts)):
            if i==1:
                edittexts[i].click()
                el.clickById('tv_ok')
            else:
                edittexts[i].send_keys(arrays[i])
        el.clickById('btnNext')
        # 校验是否有更新弹出
        # el.waitById('btn_update')
        # self.assertEqual(el.getElementById('btn_update').text, u'立即更新')
        # el.tapSearch(0.2,0.14)
        #校验是否有积分弹出
        el.waitById('txt_integral')
        self.assertEqual(el.getElementById('txt_integral').text, u'+50')
        el.clickByClassName('android.widget.ImageView')
        #校验是否有广告弹出
        el.waitById('img_bg')
        self.assertIsNotNone(el.getElementById('img_bg'),'没有弹出广告')
        imageviews=el.getElementsByClassName('android.widget.ImageView')
        imageviews[0].click()
        self.assertEqual(el.getElementById('tv_name').text, u'UI自动化')





