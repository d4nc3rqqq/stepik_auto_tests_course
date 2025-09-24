from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    # Находим все поля input
    elements = browser.find_elements(By.TAG_NAME, "input")

    # Заполняем каждый элемент
    for element in elements:
        element.send_keys("Мой ответ")

    # Нажимаем кнопку отправки
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Даем время скопировать код
    time.sleep(30)
    # Закрываем браузер
    browser.quit()
