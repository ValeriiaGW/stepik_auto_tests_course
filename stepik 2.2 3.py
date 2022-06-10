from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

my_file = open("file.txt", "w")  # создаем файл

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    first_name = browser.find_element(By.CSS_SELECTOR, value="input[name='firstname']")
    first_name.send_keys("test")
    last_name = browser.find_element(By.CSS_SELECTOR, value="input[name='lastname']")
    last_name.send_keys("test")
    email = browser.find_element(By.CSS_SELECTOR, value="input[name='email']")
    email.send_keys("test@test.com")

    current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, "file.txt")  # добавляем к этому пути имя файла
    element = browser.find_element(By.ID, value="file")  # находим на странице кнопку добавления файда
    element.send_keys(file_path)  # добавляем путь к файлу

    button = browser.find_element(By.CSS_SELECTOR, value="button.btn")
    button.click()

    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))

finally:
    time.sleep(5)
    browser.quit()


# Задание: загрузка файла


# В этом задании в форме регистрации требуется загрузить текстовый файл.
#
# Напишите скрипт, который будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"