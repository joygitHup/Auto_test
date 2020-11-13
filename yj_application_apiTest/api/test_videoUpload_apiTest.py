import unittest
import requests
from yj_application_apiTest.config import httpConfig
from yj_application_apiTest.otherFile.test import test_loginApicase1

class test_workvideo_list(unittest.TestCase):
    '''
    通过数据线连接到电脑端，初始化获取设备中的视频文件
    '''
    def setUp(self):
        pass
    def test_worvideolist(self):
        url=httpConfig.host1+httpConfig.videouploadurl_host
        headers=httpConfig.headers
        headers['Authorization']='JWT'+test_loginApicase1()
        response=requests.get(url=url,headers=headers)
        print(response.status_code)
    def tearDown(self):
        pass

class test_workvideos_apiTest(unittest.TestCase):
    '''
    连接设备后，通过数据上传设备中采集的信息
    '''
    def setUp(self):
        pass
    def  test_workvideos(self):
          pass
    def tearDown(self):
       pass
if __name__=="__main__":
    unittest.main()
