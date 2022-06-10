from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(by=By.TAG_NAME, value="input")
    for element in elements:
        element.send_keys("test")
    button = browser.find_element(by=By.CSS_SELECTOR, value="button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()

#В этой задаче вам нужно заполнить форму (http://suninjuly.github.io/huge_form.html).
# С помощью неё отдел маркетинга компании N захотел собрать подробную информацию о пользователях своего продукта.
# В награду за заполнение формы становится доступен код на скидку. Но маркетологи явно переусердствовали, добавив
# в форму 100 обязательных полей и ограничив время на ее заполнение. Теперь эта задача под силу только
# роботам ﻿🤖﻿.