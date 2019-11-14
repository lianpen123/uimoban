

#  对展示文本做断言
from time import sleep


def test_text(driver):
    driver.get("http://ui.yansl.com/#/message")
    buttons = driver.find_elements_by_xpath("//label[contains(text(),'自动关闭提示')]/..//span[text()='消息']")
    buttons[0].click()

    message = driver.find_element_by_xpath("//div[@role='alert']/p")
    text = message.text
    print(text)
    assert "这是一条消息" in text
    sleep(10)