from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")
    # browser.get("http://suninjuly.github.io/selects2.html")

    x = int(browser.find_element(By.ID, value="num1").text)
    y = int(browser.find_element(By.ID, value="num2").text)
    result = str(x + y)

    # browser.find_element(By.ID, value="dropdown").click()
    # browser.find_element(By.CSS_SELECTOR, value="[value=result]").click()
    #
    select = Select(browser.find_element(By.ID, value="dropdown")) # выбор выпадающего списка
    select.select_by_visible_text(result) # выбор из выпадающего списка

    browser.find_element(By.CSS_SELECTOR, value="button.btn").click() # нажатие на кнопку

finally:
    time.sleep(10)
    browser.quit()


#Задание: работа с выпадающим списком
# Для этой задачи мы придумали еще один вариант капчи для роботов.
# Придется немного переобучить нашего робота, чтобы он справился с новым заданием.
#
# Напишите код, который реализует следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Submit"
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
# вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.




