from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    # Ссылка на задачу (поменяй на selects2.html для проверки второй версии)
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим два числа
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    result = num1 + num2

    # Работа с выпадающим списком
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(result))   # важно передать строку!

    # Отправляем форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Немного ждём, чтобы увидеть результат
    time.sleep(5)

finally:
    browser.quit()
