#设备信息
deviceInfor={
   'device':{
      'platformName':'Android',
      'platformVersion':'9.0',
      'deviceName':'S4Y4C19308001754',
      'appPackage':'com.yunjihk.install.mobile',
      'autoGrantPermissions':True,
      'app':'E:\\Yunjiapk\\smartstepsmobile.apk',
      'appActivity':'com.yunjihk.install.mobile.ui.activity.SplashByPhoneAct'
   }
}
DEVICE_INFOR_PLATFORMNAME=deviceInfor['device']['platformName']
DEVICE_INFOR_platformVersion=deviceInfor['device']['platformVersion']
DEVICE_INFOR_deviceName=deviceInfor['device']['deviceName']
DEVICE_INFOR_appPackage=deviceInfor['device']['appPackage']
DEVICE_INFOR_autoGrantPermissions=deviceInfor['device']['autoGrantPermissions']
DEVICE_INFOR_app=deviceInfor['device']['app']
DEVICE_INFOR_appActivity=deviceInfor['device']['appActivity']

#测试数据信息
settings = {
   'admin': {
      'number': 'lxm1',
      'password': '123456'
   },
   'default_password': '123456'
}
ADMIN_NUMBER = settings['admin']['number']
ADMIN_PASSWORD = settings['admin']['password']

#文件路径信息
FilePath={
   'filePath':{
      'report_path':'E:\\DevWorkSpace\\pythonWorkSpace\\yj_autoTest_UI\\report\\',
      'report_save_path':'E:\\DevWorkSpace\\pythonWorkSpace\\yj_autoTest_UI\\report\\',
      'log_save_path':'E:\\DevWorkSpace\\pythonWorkSpace\\yj_autoTest_UI\\log\\',
      'SccreShort_save_path':'E:\\DevWorkSpace\\pythonWorkSpace\\yj_autoTest_UI\\SccreShrot\\',
   }
}
REPORT_PATH=FilePath['filePath']['report_path']
REPORT_SAVE_PATH=FilePath['filePath']['report_save_path']
LOG_SAVE_PATH=FilePath['filePath']['log_save_path']
SccreShort_SAVE_PATH=FilePath['filePath']['SccreShort_save_path']


