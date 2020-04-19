from selenium import webdriver
from selenium.webdriver.common.by import By


def init_driver():
    # 创建driver
    driver = webdriver.Firefox()
    # 设置等待时间10s
    driver.implicitly_wait(10)
    # driver.find_elements_by_partial_link_text()
    return driver
