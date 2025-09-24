import time
from selenium.webdriver.common.by import By


def test_add_to_cart_button_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Оставляем паузу для ручной проверки языка кнопки
    time.sleep(30)

    # Проверяем, что кнопка добавления в корзину есть на странице
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button.is_displayed(), "Кнопка добавления в корзину не найдена!"
