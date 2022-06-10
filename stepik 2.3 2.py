import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    browser.find_element(By.CSS_SELECTOR, value="button.trollface").click()

    new_window = browser.window_handles[1] # путь к новой вкладке (второй открытой вкладке в браузере)
    browser.switch_to.window(new_window)  # переключение на новую вкладку

    x = browser.find_element(By.ID, value="input_value").text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)

    browser.find_element(By.CLASS_NAME, value="form-control").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, value="button.btn").click()

    print(browser.switch_to.alert.text)


finally:
    browser.quit()

#
# Задание: переход на новую вкладку
# В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver
# на новую вкладку и решить в ней задачу.
#
# Сценарий для реализации выглядит так:
#
# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
# вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.