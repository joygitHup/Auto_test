import unittest

import time
from appium import webdriver
from config import config
from common import htmlTestRunner
from common import iniHelper
from config import config
from  common.getScreenShot import SccreShortMethod
des = {}
des['platformName'] = config.DEVICE_INFOR_PLATFORMNAME
des['platformVersion'] = config.DEVICE_INFOR_platformVersion
des['deviceName'] = config.DEVICE_INFOR_deviceName
des['appPackage']=config.DEVICE_INFOR_appPackage
des['autoGrantPermissions']=config.DEVICE_INFOR_autoGrantPermissions
des['app']=config.DEVICE_INFOR_app
des['appActivity']=config.DEVICE_INFOR_appActivity

class login_test_case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('多条用例放在一起')
    # @classmethod
    def setUp(self):
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub', des)
    def login_test(self,user=config.ADMIN_NUMBER,password=config.ADMIN_PASSWORD):
      """登录测试"""
      SccreShortMethod.get_windows_img(self)
      self.driver.find_element_by_id(iniHelper.inihelper('login','userinput')).send_keys(user)
      self.driver.find_element_by_id(iniHelper.inihelper('login','userpwdinput')).send_keys(password)
      self.driver.find_element_by_id(iniHelper.inihelper('login','userloginbutom')).click()
    def tearDown(self):
        self.driver.quit()
    @classmethod
    def tearDownClass(cls):
        print('多条用例放在一起执行完毕')
# def suite():
#     suiteTest = unittest.TestSuite()
#     suiteTest.addTest(login_test_case("login_test"))
    # suiteTest.addTest(login_test_case("login_test"))
    # suiteTest.addTest(login_test_case("login_test"))
    # 可以放多条用例进入测试集
    # return suiteTest
if __name__=="__main__":
    logincase=login_test_case()
    logincase.login_test(user='lxm1',password='123456')
    # suite=unittest.TestSuite()
    # suite.addTest(login_test_case('login_test'))
    # 生成测试报告
    # 选择指定时间格式
    # timestr = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))  # 本地日期时间作为测试报告的名字
    # filename = 'E:\\DevWorkSpace\\pythonWorkSpace\\yj_autoTest_UI\\report\\' + timestr + '.html'  # 这个路径改成自己的目录路径
    # fp = open(filename, 'wb')
    # runner = htmlTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title='result',
    #     description='report'
    # )
    # runner.run(suite())
    # fp.close()