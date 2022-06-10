from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://SunInJuly.github.io/execute_script.html")
    x = browser.find_element(By.ID, value="input_value").text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)
    browser.find_element(By.ID, value="answer").send_keys(y)
    browser.find_element(By.ID, value="robotCheckbox").click()

    robots_rule = browser.find_element(By.ID, value="robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robots_rule)
    robots_rule.click()
    button = browser.find_element(By.CSS_SELECTOR, value="button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(5)
    browser.quit()


# #Задание на execute_script
# В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным
# и огромным футером, который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:
#
# Открыть страницу http://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit".
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
# вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.
#
# Для этой задачи вам понадобится использовать метод execute_script, чтобы сделать прокрутку в область
# видимости элементов, перекрытых футером.
