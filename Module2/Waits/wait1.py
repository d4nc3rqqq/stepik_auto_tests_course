from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# Ждём, когда цена станет $100 (до 12 секунд)
WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)

# Жмём на кнопку Book
browser.find_element(By.ID, "book").click()

# Решаем задачу
x = browser.find_element(By.ID, "input_value").text
y = calc(x)
browser.find_element(By.ID, "answer").send_keys(y)

# Жмём на Solve
browser.find_element(By.ID, "solve").click()

# Явное ожидание появления алерта
alert = WebDriverWait(browser, 5).until(EC.alert_is_present())

# Читаем текст из алерта
print(alert.text)

# Дадим время, чтобы увидеть число глазами
time.sleep(5)

# Закрываем алерт
alert.accept()
