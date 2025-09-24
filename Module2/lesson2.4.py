from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

# Функция из условия
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открываем страницу
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    # Считываем x и считаем выражение
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Находим поле для ответа
    answer = browser.find_element(By.ID, "answer")

    # Скроллим страницу вниз, чтобы элементы были видимыми
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)

    # Вводим ответ
    answer.send_keys(y)

    # Выбираем checkbox и radiobutton
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

    # Кликаем Submit
    browser.find_element(By.TAG_NAME, "button").click()

    # Ждем немного, чтобы увидеть alert с ответом
    time.sleep(5)

finally:
    browser.quit()