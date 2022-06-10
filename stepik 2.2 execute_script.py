from selenium import webdriver
import time

browser = webdriver.Chrome()

# Изменим сначала заголовок страницы, а затем вызовем alert:
browser.execute_script("document.title='Script executing';alert('Robots at work');")


time.sleep(10)
browser.quit()