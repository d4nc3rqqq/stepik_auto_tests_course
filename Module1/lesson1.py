from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os

# Путь к ChromeDriver
chromedriver_path = r"C:\chromedriver-win64\chromedriver.exe"

# Создаем сервис с указанием пути к драйверу
service = Service(executable_path=chromedriver_path)

browser = None
try:
    # Инициализация браузера
    browser = webdriver.Chrome(service=service)

    browser.get("http://suninjuly.github.io/simple_form_find_task.html")

    # Заполняем форму
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")

    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    # Нажимаем кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Даем время увидеть результат
    time.sleep(10)
    if browser:
        browser.quit()
