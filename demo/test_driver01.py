from time import sleep

from selenium import webdriver
#  打开浏览器
def web_chrome(driver_chrome):
    driver = webdriver.Chrome('../chrome_driver-01/chromedriver.exe')
#  调整浏览器窗口大小
    driver.maximize_window()
#  关闭浏览器，但不退出driver
#driver.close()
sleep(1)

#  关闭浏览器，并退出driver
#driver.quit()
#  打开网址
##driver.get("http://www.jd.com")
# 后退
#driver.back()
sleep(1)
# 前进
#driver.forward()
sleep(1)
# 刷新
#driver.refresh()
sleep(1)
#driver.quit()
