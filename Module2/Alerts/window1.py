from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    # шаг 1: нажать кнопку, которая открывает новую вкладку
    browser.find_element(By.CSS_SELECTOR, "button.trollface").click()

    # шаг 2: переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # шаг 3: на новой странице взять x и решить задачу
    x = browser.find_element(By.ID, "input_value").text
    answer = calc(x)

    # шаг 4: ввести ответ и отправить форму
    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # шаг 5: получить число-ответ из alert
    time.sleep(3)
    alert = browser.switch_to.alert
    print("Ваш ответ:", alert.text)

finally:
    browser.quit()
