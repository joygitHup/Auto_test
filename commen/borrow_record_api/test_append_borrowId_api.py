# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/18 10:58
@Auth ： 你赖大爷
@File ：test_append_borrowId_api.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import json
import unittest

import requests

from financial_auto_api_test.config import data_config
import pytest ,allure
@allure.feature("调整质押率")
class test_append_borrowId_api(unittest.TestCase):
    """调整质押率"""
    @classmethod
    def setUpClass(self) -> None:
        self.url = data_config.host + data_config.borrow_append_borrowId_url
        print(self.url)
        self.header = data_config.header
        print(self.header)
    @allure.title("正常访问接口")
    @allure.story('接口正常访问')
    def test_borrow_list_api_01(self):
        request = requests.post(url=self.url,headers=self.header,data=json.dumps(data_config.borrow_append_borrowId_data))
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @allure.story('接口正常访问')
    def test_borrow_list_api_02(self):
        request = requests.post(url=self.url, headers=self.header, data=json.dumps(data_config.borrow_append_borrowId_data02))
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')
    @classmethod
    def tearDownClass(self) :
        print('test finnnshi!')

if __name__=="__main__":
    unittest.main()

# 生成allure
# pytest test_append_borrowId_api.py --alluredir D:\pythonDdvWorkspace\pythonVersion310\financial_auto_api_test\allure_report
# allure generate D:\pythonDdvWorkspace\pythonVersion310\financial_auto_api_test\allure_report\taget -o D:\pythonDdvWorkspace\pythonVersion310\financial_auto_api_test\allure_report\html
# -o前面文件路径为生成数据的内径 -o后面的路径为生成web页面所需要的路径
# allure serve D:\pythonDdvWorkspace\pythonVersion310\financial_auto_api_test\allure_report\html


