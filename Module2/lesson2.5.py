from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    # Заполняем текстовые поля
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("ivan.petrov@example.com")

    # Создаём файл file.txt в той же папке, где лежит скрипт
    current_dir = os.path.abspath(os.path.dirname(__file__))   # абсолютный путь к папке скрипта
    file_path = os.path.join(current_dir, 'file.txt')
    with open(file_path, "w") as f:
        f.write("test file")   # можно оставить пустым, но я добавил текст для примера

    # Загружаем файл в форму
    browser.find_element(By.ID, "file").send_keys(file_path)

    # Нажимаем кнопку Submit
    browser.find_element(By.TAG_NAME, "button").click()

    # Ждём немного, чтобы увидеть alert с числом
    time.sleep(5)

finally:
    browser.quit()
