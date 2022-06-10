from selenium import webdriver
import time
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/find_xpath_form"

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
    button = browser.find_element(by=By.XPATH, value="//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()


#На этот раз воспользуемся возможностью искать элементы по XPath.

# На странице http://suninjuly.github.io/find_xpath_form вы найдете такую же форму регистрации, как в шаге 3,
# при этом в нее добавилась куча одинаковых кнопок отправки. Но сработает только кнопка с текстом "Submit", и
# наша задача нажать в коде именно на неё.