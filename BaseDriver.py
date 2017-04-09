#coding=utf-8
from appium import webdriver
import unittest
import os
import time
import HTMLTestRunner

# Returns abs path relative to this file and not cwd
# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__), p)
# )
# class Test(unittest.TestCase):
    # def setUp(self):
    #     desired_caps = {}
    #     # 真机运行
    #     desired_caps['platformName'] = 'Android'
    #     desired_caps['platformVersion'] = '6.0'
    #     desired_caps['deviceName'] = 'G2W0215805009153'
    #     desired_caps['appPackage'] = 'com.docrab.pro'
    #     desired_caps['appActivity'] = 'com.docrab.pro.ui.page.SplashActivity'
    #     # 模拟器运行：
    #     # desired_caps['platformName'] = 'Android'
    #     # desired_caps['platformVersion'] = '4.4.4'
    #     # desired_caps['deviceName'] = '192.168.2.101:5555'
    #     # desired_caps['appPackage'] = 'com.docrab.pro'
    #     # desired_caps['appActivity'] = 'com.docrab.pro.ui.page.SplashActivity'
    #     desired_caps['unicodeKeyboard'] = True
    #     desired_caps['resetKeyboard'] = True
    #     self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app
    #     time.sleep(8)  # 需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
    # def tearDown(self):
    #     self.driver.quit()

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        # 真机运行
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'G2W0215805009153'
        desired_caps['appPackage'] = 'com.docrab.pro'
        desired_caps['appActivity'] = 'com.docrab.pro.ui.page.SplashActivity'
        #模拟器运行：
        # desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '4.4.4'
        # desired_caps['deviceName'] = '192.168.2.101:5555'
        # desired_caps['appPackage'] = 'com.docrab.pro'
        # desired_caps['appActivity'] = 'com.docrab.pro.ui.page.SplashActivity'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app
        # time.sleep(15)  # 需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
