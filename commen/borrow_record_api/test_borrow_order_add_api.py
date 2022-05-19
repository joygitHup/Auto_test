# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/18 18:03
@Auth ： 你赖大爷
@File ：test_borrow_order_add_api.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import unittest

import requests

from financial_auto_api_test.config import data_config


class test_borrow_order_add_api(unittest.TestCase):
    """发起借款"""
    @classmethod
    def setUpClass(self) -> None:
        self.url = data_config.host + data_config.borrow_order_add_url
        self.header = data_config.header

    def test_borrow_order_add_api_01(self):
        request = requests.post(url=self.url,headers=self.header,data=data_config.borrow_order_add_data)
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @classmethod
    def tearDownClass(self) :
        print('test finnnshi!')

if __name__=="__main__":
    unittest.main()

