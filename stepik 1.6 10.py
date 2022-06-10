from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(by=By.CSS_SELECTOR, value=".first_block .form-control.first")
    first_name.send_keys("test")
    last_name = browser.find_element(by=By.CSS_SELECTOR, value=".first_block .form-control.second")
    last_name.send_keys("test")
    email_field = browser.find_element(by=By.CSS_SELECTOR, value=".first_block .form-control.third")
    email_field.send_keys("test@test.com")

# Отправляем заполненную форму
    button = browser.find_element(by=By.CSS_SELECTOR, value="button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(by=By.CSS_SELECTOR, value="h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

