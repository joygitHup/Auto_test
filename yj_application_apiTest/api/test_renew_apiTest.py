import json
import logging
import unittest
import requests
from yj_application_apiTest.config import httpConfig
from yj_application_apiTest.otherFile.test import test_loginApicase1
from yj_application_apiTest.tools.logClas import MyLog
class test_budinwordsheet_dutypepole(unittest.TestCase):
    '''新建工作票中下拉框中获取数据接口'''
    def setUp(self):
        pass
    def test_budinwordsheet_duty(self):
         url=httpConfig.host+httpConfig.duty_url
         date=httpConfig.duty_data
         headers = httpConfig.headers
         headers['Authorization'] = 'JWT ' + test_loginApicase1()
         response=requests.post(url,headers,data=date)
         print(response.status_code)
    def tearDown(self):
        pass
class test_renew_apitest(unittest.TestCase):
    '''
    提交新建工作票的接口测试
    '''
    def setUp(self):
        pass
    def test_rebuited_worksheet(self):
        url = httpConfig.host + httpConfig.new_rebuited_data_url
        # data = httpConfig.dataUploa
        headers = httpConfig.headers
        headers['Authorization'] = 'JWT ' + test_loginApicase1()
        re = requests.put(url, headers=headers, verify=False)
        result = re.status_code
        # 添加断言
        print(result)
    def tearDown(self):
        pass

class alternative_new_voice(unittest.TestCase):
    '''切换到新建作业票'''
    def setUp(self):
        pass
    def alter_voice(self):
        '/kw/desktop/inspection_sheets/field_values/recommend/'
        pass
    def tearDown(self) :
        pass
class upload_file_remark(unittest.TestCase):
    def setUp(self) :
        pass
    def uploadfile_remark(self):
        pass
    def tearDown(self) :
        pass
class  worksheet_Manger(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def gain_worksheet_list(self):
        pass
    def tearDown(self) -> None:
        pass
class worksheet_content(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def worksheet_content_infor(self):
        pass
    def tearDown(self) -> None:
        pass
if __name__=="__main__":
  unittest.main()