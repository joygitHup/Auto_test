import time
import os.path
from config import config
class SccreShortMethod(object):
    def __init__(self, driver):
        self.driver = driver
    # 保存截图
    def get_windows_img(self):
        # os.path.abspath('.')
        # file_path = os.path.dirname(os.path.abspath('.'))+ '\\SccreShrot\\'#设置截图保存路径
        file_path=config.SccreShort_SAVE_PATH
        rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))	#获取当前系统时间
        img_name = file_path + rq + '.png'	#设置截图名称格式
        try:
            self.driver.get_screenshot_as_file(img_name)  	#指定截图存放路径和名称
            print("已将截图保存到文件夹")
        except NameError as e:
            print("截图保存失败! %s" % e)
            self.get_windows_img()
