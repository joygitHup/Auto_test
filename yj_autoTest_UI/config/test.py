# from  selenium import  webdriver
# import time
# driver=webdriver.Chrome()
# driver.get('https://www.baidu.com')
#
# time.sleep(3)
# driver.quit()
import os

from appium import webdriver

from common import iniHelper
import  unittest
import time
from common import htmlTestRunner

des = {}
des['platformName'] = 'Android'
des['platformVersion'] = '9.0'
des['deviceName'] = 'S4Y4C19308001754'
des['appPackage']='com.yunjihk.install.mobile'
des['autoGrantPermissions']=True
des['app']="E:\\Yunjiapk\\smartstepsmobile.apk"
des['appActivity']='com.yunjihk.install.mobile.ui.activity.SplashByPhoneAct'
# com.yunjihk.helmet.ui.SplashByGlassAct
print(des)
driver=webdriver.Remote('http://localhost:4723/wd/hub', des)
time.sleep(3)
class login_test_case(unittest.TestCase):
 def login_test(self):
   driver.find_element_by_id(iniHelper.inihelper('login','userinput')).send_keys('lxm1')
   driver.find_element_by_id(iniHelper.inihelper('login','userpwdinput')).send_keys('123456')
   driver.find_element_by_id(iniHelper.inihelper('login','userloginbutom')).click()
def Add_new_workList():
  time.sleep(2)
  driver.find_element_by_id(iniHelper.inihelper('addworklist','add_entrance')).click()
# def worklist_content():
#   time.sleep(2)
#   driver.find_element_by_id(iniHelper.inihelper('worklist_content', 'work_day')).click()
#   driver.find_element_by_id(iniHelper.inihelper('worklist_content','time_tool'))
#   driver.find_element_by_xpath(iniHelper.inihelper('worklist_content', 'work_day_value')).click()

if __name__=="__main__":

    suite=unittest.TestSuite()
    suite.addTest(login_test_case())
    # 生成测试报告
    # 选择指定时间格式
    timestr = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))  # 本地日期时间作为测试报告的名字
    filename = 'E:\\DevWorkSpace\\pythonWorkSpace\\yj_autoTest_UI\\report\\' + timestr + '.html'  # 这个路径改成自己的目录路径
    fp = open(filename, 'wb')
    runner = htmlTestRunner.HTMLTestRunner(
        stream=fp,
        title='result',
        description='report'
    )
    runner.run(suite)
    fp.close()

    #
    # login_test()
    # Add_new_workList()
    # worklist_content()



