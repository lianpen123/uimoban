from lib2to3.pgen2 import driver
from telnetlib import EC
from time import sleep


import autoit
from pip._vendor.colorama.win32 import handles
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 输入框
from selenium.webdriver.support.wait import WebDriverWait


def test_input(driver): #  定义一种方法
    driver.get('http://ui.yansl.com/#/input') # 获取到此网址
    sleep(2) # 停留2秒

    input = driver.find_element_by_xpath("//input[@name='t1']") # 通过xpath定位元素：定位到输入框
    input.clear()  # 清空内容
    input.send_keys("我是谁？我在哪？")# 输入框内输入
    sleep(2)
#  单点击
def test_radio(driver):
    driver.get("http://ui.yansl.com/#/radio")
    sleep(2)
    radio = driver.find_element_by_xpath("//input[@name='sex'][2]")
    radio.click() # 点击
    sleep(2)

# 多点击
def test_checkbox(driver):
    driver.get("http://ui.yansl.com/#/checkbox")
    sleep(2)
    checkbox = driver.find_element_by_xpath("//*[@id='form']/form/div[2]/div/div/label[1]/span[1]")
    attribute = checkbox.get_attribute("class") # #获取多选框元素里的“CLASS”
    if not attribute=='el-checkbox__input is-checked': # 如果多选框里不等于el-checkbox__input is-checked
        checkbox.click()  # 则点击
        sleep(10)
    checkbox = driver.find_element_by_xpath("//*[@id='form']/form/div[2]/div/div/label[1]/span[1]")
    attribute = checkbox.get_attribute("class")
    if not attribute=='el-checkbox__input is-checked':
        checkbox.click()
        sleep(2)
# 鼠标悬浮未点击 ,下拉框
def test_select(driver):
    driver.get("http://ui.yansl.com/#/select")
    sleep(2)
    select = driver.find_element_by_xpath("//*[@id='form']/form/div[3]/div/div/div[2]/input")
    select.click()
    sleep(2)
    option = driver.find_element_by_xpath("(//span[text()='双皮奶'])[last()]") # 设置一个变量名。通过xpath定位元素
    actions = ActionChains(driver) # 类的实例化
    actions.move_to_element(option).perform() # 鼠标悬浮在元素上面
    sleep(2)
    option.click() # 点击
#  滑块
def test_slider(driver):
    driver.get("http://ui.yansl.com/#/slider")
    sleep(2)
    slider = driver.find_element_by_xpath("//*[@id='form']/form/div[5]/div/div/div/div[2]/div")
    sleep(2)
    actions = ActionChains(driver)# 类的实例化
    #actions.move_to_element(slider).click_and_hold(slider).move_by_offset(0,-200).release(slider).perform(slider)
    actions.drag_and_drop_by_offset(slider,0,-200).perform() # 鼠标拖拽元素，横坐标，纵坐标
    sleep(3)

#  时间
def test_input(driver):
    driver.get('http://ui.yansl.com/#/dateTime')
    sleep(2)

    t1 = driver.find_element_by_xpath("//*[@id='form']/form/div[1]/div[1]/div/div/input")
    t1.clear() #清空
    t1.send_keys("15:10:20") # 输入时间
    sleep(5)
# 上传图片文件
def test_upload1(driver):
    driver.get("http://ui.yansl.com/#/upload")
    sleep(2)
    file = driver.find_element_by_xpath("//*[@id='form']/form/div[1]/div/input")
    file.clear()
    file.send_keys("D:\\softwareback\\eval.png") # 上传文件
    sleep(5)

def test_upload2(driver):
    driver.get("http://ui.yansl.com/#/upload")
    sleep(2)
    file = driver.find_element_by_xpath('//*[@id="form"]/form/div[2]/div/div/div[1]/button/span')
    file.click()
    sleep(3)
    autoit.win_wait("打开", 10)
    sleep(1)
# autoit.control_send("打开", "Edit1", os.path.abspath(file_path))
    autoit.control_set_text("打开", "Edit1", "D:\\softwareback\\eval.png")
    sleep(5)
    autoit.control_click("打开", "Button1")
    sleep(10)

# 弹窗输入
def test_button(driver):
    driver.get("http://192.168.1.128:8082/xuepl/demo.html")
    sleep(2)
    button = driver.find_element_by_xpath("/html/body/table/tbody/tr[6]/td[2]/input")
    button.click()
    sleep(2)
    alert = driver.switch_to.alert # 弹框切换，切换到弹框里
    alert.send_keys("nihao") # 输入nihao
    alert.accept() #点击确认
    sleep(10)

#  超链接，窗口切换
def test_windows(driver):
    driver.get("http://192.168.1.128:8082/xuepl/demo.html")
    sleep(2)
    dang_dang = driver.find_element_by_link_text("当当") # 准确定位到当当
    actions = ActionChains(driver)
    # 鼠标按下不松开，点击当当链接，松开鼠标，运行
    actions.key_down(Keys.CONTROL).click(dang_dang).key_up(Keys.CONTROL).perform()
    sleep(2)
    jd= driver.find_element_by_link_text("京东")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(jd).key_up(Keys.CONTROL).perform()
    sleep(2)
    dn = driver.find_element_by_partial_link_text("度娘")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(dn).key_up(Keys.CONTROL).perform()
    sleep(2)
    # 获取所有窗口的句柄
    handles = driver.window_handles
    for h in handles:
        # 根据窗口句柄，切换窗口
        driver.switch_to.window(h)
        sleep(2)
        if driver.title.__contains__("当当"):# 如果 链接标题为当当
        # 则停止切换窗口
            break

# 一个界面内不同的框架
def test_frame(driver):
    driver.get("http://192.168.1.128:8082/xuepl1/frame/main.html")# 打开网页
    sleep(2)
    frame = driver.find_element_by_xpath("/html/frameset/frameset/frame[1]") # 通过xpath定位元素定位到此框架
    driver.switch_to.frame(frame) # 切换到frame框架里
    sleep(2)
    driver.find_element_by_link_text('京东').click() # 定位到京东此链接
    sleep(2)
    # 退出当前 iframe
    #driver.swich_to.parent_frame()
    # 回到初始页面
    driver.switch_to.default_content()# 退出此框架
    iframe = driver.find_element_by_xpath("/html/frameset/frameset/frame[2]") # 通过xpath定位元素定位到此框架
    sleep(5)
    driver.switch_to.frame(iframe) # 切换到此框架里
    inpu = driver.find_element_by_xpath('//*[@id="key"]') # 通过xpath定位元素定位到此输入框
    inpu.clear() # 清空
    inpu.send_keys("手机") # 输入手机
    sleep(5)
    #  点击搜索
    sousuo = driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
    #actions = ActionChains(driver)
    #actions.move_to_element(sousuo).perform()
    sousuo.click()
    sleep(5)
    sousuo_02 = driver.find_element_by_xpath('//*[@id="brand-14026"]/a/img')
    sousuo_02.click()
    sleep(10)

    # 显示等待，隐士等待
def test_wait(driver):
    driver.get("http://ui.yansl.com/#/loading")
    bt = driver.find_element_by_xpath("//span[contains(text(),'指令方式')]")
    bt.click()
    WebDriverWait(driver,5,0.5).until(
        EC.presence_of_element_located((By.XPATH,'//tbody/tr[1]/td[2]/div'))
    )
    bg = driver.find_element_by_xpath("//tbody/tr[1]/td[2]/div")
    print(bg.text)
    sleep(10)

    #  对展示文本做断言
from time import sleep

def test_text(driver):
    driver.get("http://ui.yansl.com/#/message")
    # 定位到“自动关闭提示”中的“消息”模块。多元素+s，elements
    buttons = driver.find_elements_by_xpath("//label[contains(text(),'自动关闭提示')]/..//span[text()='消息']")
    buttons[0].click()  # 点击消息
    # 定位到点击消息后显示的提示信息模块
    message = driver.find_element_by_xpath("//div[@role='alert']/p")
    text = message.text   # text+ 方法  获取展示文本
    print(text)
    assert "这是一条消息" in text # 断言assert “内容”in next
    sleep(2)

# 对界面源代码做断言
def test_source(driver):
    driver.get("http://ui.yansl.com/")
    source_01 = driver.find_element_by_xpath('//*[@id="app"]/section/section/aside/ul/li[3]/div')
    source_01.click()
    sleep(2)
    source_02 = driver.find_element_by_xpath("//li[contains(text(),'消息提示')]")
    source_02.click()
    sleep(5)
    source = driver.page_source
    print(source)
    assert "手工关闭提示" in source
    sleep(2)




