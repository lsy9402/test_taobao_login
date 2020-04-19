import os, sys
sys.path.append(os.getcwd())
import allure
import pytest
from base.base_data import get_yml_data_with_filename_key
from base.base_driver import init_driver_Firefox
from page.taobao_page import Taobao_page

def data_with_key(key):
    return get_yml_data_with_filename_key('data', key)

class Test_taobao :
    def setup_module(self):
        self.driver = init_driver_Firefox()     # 创建driver
        self.taobao_page = Taobao_page(self.driver)     # 加载page
    def setup_method(self):
        self.taobao_page.get_('http://www.taobao.com')  # 打开淘宝
        self.taobao_page.click_partial_link_text("亲，请登录")  # 转到登陆页面
    def teardown_method(self):
        self.taobao_page.close(1)    # 关闭窗口
    def teardown_module(self):
        self.taobao_page.quit(1)    # 退出

    @allure.feature("登陆模块")
    @allure.story("登陆模块用户名密码错误 登陆失败")
    @allure.description("验证用户名密码错误 登陆失败会出现提示")
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
        self.taobao_page.assert_is_login()     # 断言登陆错误提示