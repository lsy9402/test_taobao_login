from selenium import webdriver

def init_driver_Firefox():
    driver = webdriver.Firefox()        # 创建Firefox_driver
    driver.implicitly_wait(10)      # 设置等待时间10s
    return driver
