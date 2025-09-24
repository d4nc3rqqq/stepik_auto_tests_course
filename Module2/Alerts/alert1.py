from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    # шаг 1: нажать кнопку
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # шаг 2: переключиться на confirm и принять его
    confirm = browser.switch_to.alert
    confirm.accept()

    # шаг 3: на новой странице взять x и решить задачу
    x = browser.find_element(By.ID, "input_value").text
    answer = calc(x)

    # шаг 4: ввести ответ
    browser.find_element(By.ID, "answer").send_keys(answer)

    # шаг 5: отправить форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # подождём чуть-чуть, чтобы увидеть alert с числом
    time.sleep(5)
    alert = browser.switch_to.alert
    print("Ваш ответ:", alert.text)

finally:
    browser.quit()
