from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

# Функция для расчета значения
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# 1️⃣ Открываем страницу
browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/math.html")

try:
    # 2️⃣ Считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # 3️⃣ Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # 4️⃣ Отмечаем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    # 5️⃣ Выбираем radiobutton "Robots rule!"
    robots_rule_radio = browser.find_element(By.ID, "robotsRule")
    robots_rule_radio.click()

    # 6️⃣ Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # Ждем чтобы увидеть результат и закрываем браузер
    time.sleep(10)
    browser.quit()
