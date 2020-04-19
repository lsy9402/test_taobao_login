import os, sys
sys.path.append(os.getcwd())

from time import sleep
import allure
import pytest
from base.base_data import get_yml_data_with_filename_key
from base.base_driver import init_driver
from page.taobao_page import Taobao_page

def data_with_key(key):
    return get_yml_data_with_filename_key('data', key)

class Test_taobao :
    def setup(self):
        self.driver = init_driver()     # 创建driver
        self.taobao_page = Taobao_page(self.driver)     # 加载page

    def teardown(self):
        self.taobao_page.quit(5)    # 关闭driver

    @allure.feature("登陆模块")
    @allure.story("用户名密码错误 登陆失败")
    @allure.step("用户名密码错误 登陆失败")
    @allure.severity('critical')
    @pytest.mark.parametrize("args", data_with_key('test_login'))
    def test_login(self, args):
        username = str(args["username"])
        password = str(args["password"])
        with allure.step("1.输入账号:" + username ):
            self.taobao_page.input_username(username)
        with allure.step("2.输入密码:" + password):
            self.taobao_page.input_password(password)
        with allure.step("3.点击登陆"):
            self.taobao_page.click_login()
        self.taobao_page.allure_screen("登陆失败页面")        # 截图