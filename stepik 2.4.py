from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")  # ждет 15с когда цена будет 100
    )
    browser.find_element(By.CSS_SELECTOR, value="button.btn").click()
    x = browser.find_element(By.ID, value="input_value").text

    def calc(x):
        return math.log((abs(12*math.sin(int(x)))))

    y = calc(x)

    browser.find_element(By.ID, value="answer").send_keys(y)
    browser.find_element(By.ID, value="solve").click()

    print(browser.switch_to.alert.text)

finally:

    browser.quit()


# Задание: ждем нужный текст на странице
# Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене.
# Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.
#
# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
# Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.