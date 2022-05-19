# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/18 13:40
@Auth ： 你赖大爷
@File ：test_auto_adjust_api.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import unittest

import requests

from financial_auto_api_test.config import data_config


class test_auto_adjust_api(unittest.TestCase):
   """自动调整质押率"""
   @classmethod
   def setUpClass(self) -> None:
     self.url = data_config.host + data_config.auto_adjust_url
     print(self.url)
     self.header = data_config.header
     self.data=data_config.auto_adjust_data
     print(self.data)


   def test_auto_adjust_api_01(self):
     """正常访问自动调整质押率接口"""
     request = requests.post(url=self.url, headers=self.header, data=self.data.encode("utf-8"))
     print(request.content.decode('utf-8'))
     return request.content.decode('utf-8')

   @classmethod
   def tearDownClass(self):
      print('test finnnshi!')

if __name__=="__main__":
    unittest.main()

