import os, sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from base.base_action import Base_action

class Taobao_page(Base_action):
    def __init__(self,driver):
        Base_action.__init__(self, driver)
        self.get_('http://www.taobao.com')  # 打开淘宝
    username = "@name='fm-login-id'"
    password = By.ID, "fm-login-password"
    def click_login(self):
        self.click_partial_link_text("亲，请登录")  # 转到登陆页面
    def input_username(self, username):     # 输入账号
        self.input_txt(self.username, username)
    def input_password(self, password):     # 输入密码
        self.input_txt(self.password, password)
    def click_login(self):      # 点击登陆
        self.click("class='fm-button fm-submit password-login'")
    def assert_is_login(self):
        self.assert_is_element_present("id='login-error'", "登录名或登录密码不正确")