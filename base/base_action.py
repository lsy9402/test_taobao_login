import sys
from time import sleep
import allure

class Base_action:
    def __init__(self, driver):     # 获取对象
        self.driver = driver
    def get_(self, url = ""):
        self.driver.get(url)
    def click(self, loc):       # 点击
        self.find_element(loc).click()
    def click_partial_link_text(self, txt):
        self.driver.find_element_by_partial_link_text(txt).click()
    def clear(self, loc):
        self.find_element(loc).clear()
    def quit(self, time = 0):
        sleep(time)
        self.driver.quit()  # 关闭driver
    def refresh(self):
        self.driver.refresh()
    def input_txt(self,loc,txt):        # 输入txt
        self.find_element(loc).send_keys(txt)
    def get_txt(self,loc):      # 获取txt
        return self.find_element(loc).get_attribute('textContent')
    def quit(self):
        self.driver.quit()
    def assertin(self, expected, actual, screen = "AssertionError"):
        try:
            assert expected in actual
        except AssertionError:
            now_time = time.strftime('%Y-%m-%d_%H:%M:%S')       # 设置时间
            self.screenshot(screen + now_time)  # 上传图片到报告
            allure.attach(open("./screen/" + screen + now_time + ".png", "rb").read(), "失败截图", allure.attachment_type.PNG)      # 上传图片到报告
            raise AssertionError
    def find_element(self, loc):       # 处理参数
        if type(loc) == str:
            value = self.make_xpath_with_feature(loc)
            return self.driver.find_element_by_xpath(value)
        else:
            by = loc[0]
            value = loc[1]
        return self.driver.find_element(by=by, value=value)
    def make_xpath_with_feature(self, loc):
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
    def screenshot(self, file_name):
        self.driver.get_screenshot_as_file("./reports/screen/" + file_name + ".png")
    def allure_screen(self,file_name):
        now_time = time.strftime('%Y-%m-%d_%H:%M:%S')  # 设置时间
        self.screenshot(file_name + now_time)  # 截图
        allure.attach(open("./reports/screen/" + file_name + now_time + ".png", "rb").read(), file_name,allure.attachment_type.PNG)  # 上传图片到报告