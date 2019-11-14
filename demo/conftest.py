from telnetlib import EC
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='session')
def driver():
  # 打开浏览器
    driver = webdriver.Chrome('../chrome_driver-01/chromedriver.exe')
#  调整浏览器窗口大小
    driver.maximize_window()
    driver.implicitly_wait(10)# 隐士等待5秒
    sleep(1)
    yield driver
    driver.quit()





