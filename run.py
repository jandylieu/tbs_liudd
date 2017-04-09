#coding=utf-8
from appium import webdriver
import unittest
import os
import time
import HTMLTestRunner
import Test_001,Test_002,Test_003,Test_004,Test_005,Test_006,Test_007,Test_008
# Returns abs path relative to this file and not cwd
# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__), p)
# )
def creatSuit():
    suit = unittest.TestSuite()
    #使用discover方法，自动路径下的test文件
    discover = unittest.defaultTestLoader.discover(r'F:\ui_automation', pattern='Test*.py', top_level_dir=None)
    # 将测试用例加至容器中
    for test_suit in discover:
        for casename in test_suit:
            suit.addTest(casename)
        print suit
    return suit
test_case=creatSuit()
Htmlfile = "D:\\result.html"
fp = file(Htmlfile, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description=u'Test Result:')
runner.run(test_case)
fp.close()
if __name__ == '__main__':
    unittest.main(verbosity=2)


# if __name__ == '__main__':
#     suit = unittest.TestSuite()
    # suit.addTest(Test_006.Case("test_01_EstateHouse_Pub1"))
    # suit.addTest(Test_006.Case("test_02_EstateHouse_Pub0"))
    # suit.addTest(Test_006.Case("test_03_EstateVillas_Pub1"))
    # suit.addTest(Test_006.Case("test_04_EstateVillas_Pub0"))
    # suit.addTest(Test_006.Case("test_05_EstateShare_Weixin"))
    # suit.addTest(Test_006.Case("test_06_EstateShare_Friend"))
    # suit.addTest(Test_006.Case("test_07_EstateShare_QQ"))
    # suit.addTest(Test_006.Case("test_08_EstateDelete"))
    # suit.addTest(Test_006.Case("test_09_EstateRefresh"))
    # suit.addTest(Test_006.Case("test_10_SamePlateEstateList"))
    # suit.addTest(Test_006.Case("test_11_PotentialEstateList"))
    # suit.addTest(Test_007.Case("test_01_Updeal"))
    # suit.addTest(Test_007.Case("test_02_Scan"))
    # suit.addTest(Test_007.Case("test_03_Recommend"))
    # suit.addTest(Test_007.Case("test_04_EstateClicked"))
    # Htmlfile = "D:\\result.html"
    # fp = file(Htmlfile, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description=u'Test Result:')
    # runner.run(suit)
    # fp.close()




