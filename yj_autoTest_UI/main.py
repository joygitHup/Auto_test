import unittest
#相对路径
import time

from TestCase.Test_login import login_test_case
from common import htmlTestRunner
from common.SendNewReport import sendEmai
from common.filePath import fileposition
from config import config

# testcase_path = ".\\testcase"
report_path = config.REPORT_PATH
def creat_suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(login_test_case("login_test"))
    # suiteTest.addTest(login_test_case("login_test"))
    # suiteTest.addTest(login_test_case("login_test"))
    # 可以放多条用例进入测试集
    return suiteTest
suite = creat_suite()
timestr = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))  # 本地日期时间作为测试报告的名字
filename =config.REPORT_SAVE_PATH + timestr + '.html'  # 这个路径改成自己的目录路径
fp = open(filename,"wb")
runner = htmlTestRunner.HTMLTestRunner(stream=fp,title="测试结果",description="测试结果")
runner.run(suite)
fp.close()
newresult =fileposition.new_file(report_path)
# emial = sendEmai
# emial.Sendemail(newresult)


#1.将日志记录引入
#2.引入断言
#3.尝试将扩展其他用例集成
#4.将启动设备号 参数化  ----ok
#5.引入截图功能  -----ok---封装截图--ok
#6.将测试报告内容展示优化   --添加截图
#7.优化driver  一处启动 到处调用




