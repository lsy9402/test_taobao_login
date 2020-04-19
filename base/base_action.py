import sys
import time
from time import sleep
import allure

class Base_action:
    def __init__(self, driver):     # 获取对象
        self.driver = driver
    def forword(self):      # 控制浏览器前进
        self.driver.forword()
    def back(self):     # 控制浏览器后退
        self.driver.back()
    def refresh(self):      # 控制浏览器刷新
        self.driver.refresh()
    def close(self):        # 控制浏览器关闭
        self.driver.close()
    def set_page_load_time(self):
        self.driver.set_page_load_time()
    def set_window_size(self, width, height):       # 通过像素设置浏览器的大小
        self.driver.set_window_size(width, height)
    def maximize_window(self):      # 设置窗口最大化
        self.driver.maximize_window()
    def minimize_window(self):      #   设置窗口最小化
        self.driver.minimize_window()
    def get_(self, url = ""):       # 打开网页
        self.driver.get(url)
    def click(self, loc):       # 单击
        self.find_element(loc).click()
    def click_partial_link_text(self, txt):
        self.driver.find_element_by_partial_link_text(txt).click()
    def clear(self, loc):       # 清除文本
        self.find_element(loc).clear()
    def quit(self, time = 0):   # 控制浏览器退出
        sleep(time)
        self.driver.quit()  # 关闭driver
    def input_txt(self,loc,txt):        # 输入文本
        self.find_element(loc).send_keys(txt)
    def get_txt(self,loc):      # 获取文本
        return self.find_element(loc).get_attribute('textContent')
    def find_element(self, loc):       # 查找元素（str自动转xpath处理）
        if type(loc) == str:
            value = self.make_xpath_with_feature(loc)
            return self.driver.find_element_by_xpath(value)
        else:
            by = loc[0]
            value = loc[1]
        return self.driver.find_element(by=by, value=value)
    def make_xpath_with_feature(self, loc):     # xpath处理
        feature_start = "//*["
        feature_end = "]"
        if isinstance(loc, str):
            if loc.startswith("//"):
                return loc
            elif loc.startswith("/"):
                return loc
            elif loc.startswith("@"):
                feature = loc
                return feature_start + feature + feature_end
            else:
                feature = "@" + loc
                return feature_start + feature + feature_end
    def error_screenshot(self):
        now_time = time.strftime('%Y-%m-%d_%H:%M:%S')        # 设置时间
        self.driver.get_screenshot_as_file("../Image/%s_%s.png" % (now_time, str(sys.exc_info()[1])))        # 断言失败截图
    def screenshot(self, file_name):        # 截图保存
        self.driver.get_screenshot_as_file("./reports/screen/" + file_name + ".png")
    def allure_screen(self,file_name):      #上传截图到报告
        now_time = time.strftime('%Y-%m-%d_%H:%M:%S')  # 设置时间
        self.screenshot(file_name + now_time)  # 截图
        allure.attach(open("./reports/screen/" + file_name + now_time + ".png", "rb").read(), file_name,allure.attachment_type.PNG)  # 上传图片到报告
    def assertin(self, expected, actual):       # 断言结果（失败上传截图到报告）
        try:
            assert expected in actual
        except AssertionError:
            self.allure_screen('失败截图')    # 上传图片到报告
            raise AssertionError
    def assert_is_element_present(self, loc, txt):      # 断言文本存在
        try:
            assert txt in self.find_element(loc).text
        except AssertionError as e:
            print(e)        # 打印异常信息
            raise AssertionError
    def is_displayed(self, loc):        # 返回元素的结果是否可见， 返回结果为 True 或 False
        return self.find_element(loc).is_displayed()