from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_block = browser.find_element(By.CSS_SELECTOR, "div.first_block")
    first_name_input11 = first_block.find_element(By.CSS_SELECTOR, "input.first")
    first_email_input2 = first_block.find_element(By.CSS_SELECTOR, "input.third")
    first_last_input3 = first_block.find_element(By.CSS_SELECTOR, "input.second")

    first_name_input11.send_keys("Ivan")
    first_last_input3.send_keys("Ivanov")
    first_email_input2.send_keys("ivan.ivanov@example.com")
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()