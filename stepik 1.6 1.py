from selenium import webdriver
import time
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(by=By.TAG_NAME, value="input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(by=By.NAME, value="last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(by=By.CLASS_NAME, value="form-control.city")
    input3.send_keys("Dnepr")
    input4 = browser.find_element(by=By.ID, value="country")
    input4.send_keys("Ukraine")
    button = browser.find_element(by=By.CSS_SELECTOR, value="button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()


# Вам нужно открыть страницу по ссылке и заполнить форму на этой странице с помощью Selenium.
# Если всё сделано правильно, то вы увидите окно с проверочным кодом. Это число вам нужно ввести в качестве
# ответа в этой задаче.