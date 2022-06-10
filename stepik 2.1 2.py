from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.TAG_NAME, value="img")
    x = x_element.get_attribute("valuex")


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)

    result = browser.find_element(By.ID, value="answer")
    result.send_keys(y)
    check_box = browser.find_element(By.ID, value="robotCheckbox")
    check_box.click()
    radio_b = browser.find_element(By.ID, value="robotsRule")
    radio_b.click()
    button = browser.find_element(By.CSS_SELECTOR, value="button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()


#Задание: поиск сокровища с помощью get_attribute
# В данной задаче вам нужно с помощью роботов решить ту же математическую задачу,
# как и в прошлом задании. Но теперь значение переменной х спрятано в "сундуке", точнее,
# значение хранится в атрибуте valuex у картинки с изображением сундука.
#
# Ваша программа должна:
#
# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку "Submit".
# Для вычисления значения выражения в п.4 используйте функцию calc(x) из предыдущей задачи.

