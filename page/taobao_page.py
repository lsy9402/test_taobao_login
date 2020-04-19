import os, sys
from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())
from base.base_action import Base_action


class Taobao_page(Base_action):
    def __init__(self,driver):
        Base_action.__init__(self, driver)
        self.get_('http://www.taobao.com')
        self.click_partial_link_text("亲，请登录")

    username = "@name='fm-login-id'"
    password = By.ID, "fm-login-password"

    def input_username(self, username):
        self.input_txt(self.username, username)
    # 输入密码
    def input_password(self, password):
        self.input_txt(self.password, password)
    # 点击登陆
    def click_login(self):
        self.click("class='fm-button fm-submit password-login'")