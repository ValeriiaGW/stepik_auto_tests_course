from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


link = "http://suninjuly.github.io/find_link_text"
text = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    clicked_link = browser.find_element(by=By.LINK_TEXT, value=text)
    clicked_link.click()
    input1 = browser.find_element(by=By.TAG_NAME, value="input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(by=By.NAME, value="last_name")
    input2.send_keys("Ivanov")
    input3 = browser.find_element(by=By.CLASS_NAME, value="form-control.city")
    input3.send_keys("Dnipro")
    input4 = browser.find_element(by=By.ID, value="country")
    input4.send_keys("Ukraine")
    button = browser.find_element(by = By.CSS_SELECTOR, value="button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()



# На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней:
#
# Добавьте в самый верх своего кода import math
# Добавьте в код команду, которая откроет страницу: http://suninjuly.github.io/find_link_text
# Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой:
# str(math.ceil(math.pow(math.pi, math.e)*10000))
# (можно вставить данное выражение в свой код, а можно выполнить в интерпретаторе, скопировать оттуда результат и уже его использовать в вашем коде)
#
# Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации
#
# Заполните скриптом форму так же как вы делали в предыдущем шаге урока
#
# После успешного заполнения вы получите код - отправьте его в качестве ответа на это задание