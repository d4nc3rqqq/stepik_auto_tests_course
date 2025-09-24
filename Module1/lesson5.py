from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Старая страница (тест должен пройти)
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Уникальные селекторы для обязательных полей
    browser.find_element(By.CSS_SELECTOR, "input.first[required]").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "input.second[required]").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, "input.third[required]").send_keys("ivan.petrov@example.com")

    # Отправка формы
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Проверка успешной регистрации
    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
