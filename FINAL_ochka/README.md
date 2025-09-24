# Автоматизация тестирования с помощью Selenium и Pytest

Этот проект содержит фреймворк автоматизации тестирования для интернет-магазина, построенный на основе паттерна Page Object Model (POM) с использованием Selenium WebDriver и pytest.

## Структура проекта

```
final_project/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── basket_page.py
│   ├── locators.py
│   ├── login_page.py
│   ├── main_page.py
│   └── product_page.py
├── __init__.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── test_main_page.py
├── test_product_page.py
└── README.md
```

## Описание файлов

### Страницы (Page Objects)

- **base_page.py**: Базовый класс для всех страниц с общими методами
- **basket_page.py**: Класс для страницы корзины
- **login_page.py**: Класс для страницы авторизации/регистрации
- **main_page.py**: Класс для главной страницы
- **product_page.py**: Класс для страницы товара
- **locators.py**: Локаторы элементов для всех страниц

### Тесты

- **test_main_page.py**: Тесты для главной страницы
- **test_product_page.py**: Тесты для страницы товара

### Конфигурационные файлы

- **conftest.py**: Фикстуры для pytest (браузер, генерация случайных данных)
- **pytest.ini**: Регистрация маркеров для pytest
- **requirements.txt**: Зависимости проекта

## Описание тестов

### Тесты с маркером need_review

1. **test_guest_can_add_product_to_basket** - Проверяет, что гость может добавить товар в корзину со страницы товара
2. **test_guest_can_go_to_login_page_from_product_page** - Проверяет, что гость может перейти на страницу логина со страницы товара
3. **test_guest_cant_see_product_in_basket_opened_from_product_page** - Проверяет, что гость не видит товары в корзине, открытой со страницы товара
4. **test_user_can_add_product_to_basket** - Проверяет, что авторизованный пользователь может добавить товар в корзину

### Тесты для гостя (TestGuestAddToBasketFromProductPage)

1. **test_guest_can_add_product_to_basket** - Проверяет, что гость может добавить товар в корзину
2. **test_guest_can_add_product_to_basket_with_promo** - Проверяет добавление товара в корзину с разными промо-кодами
3. **test_guest_cant_see_success_message_after_adding_product_to_basket** (xfail) - Проверяет отсутствие сообщения об успехе после добавления товара в корзину
4. **test_guest_cant_see_success_message** - Проверяет отсутствие сообщения об успехе при загрузке страницы
5. **test_message_disappeared_after_adding_product_to_basket** (xfail) - Проверяет, что сообщение об успехе исчезает после добавления товара в корзину
6. **test_guest_should_see_add_to_basket_button** - Проверяет наличие кнопки добавления в корзину
7. **test_guest_can_see_product_name** - Проверяет, что название товара отображается на странице
8. **test_guest_can_see_product_price** - Проверяет, что цена товара отображается на странице

### Тесты для логина гостя (TestGuestLoginFromProductPage)

1. **test_guest_should_see_login_link_on_product_page** - Проверяет, что гость видит ссылку на логин на странице товара
2. **test_guest_can_go_to_login_page_from_product_page** - Проверяет, что гость может перейти на страницу логина со страницы товара

### Тесты для корзины гостя (TestGuestBasketFromProductPage)

1. **test_guest_cant_see_product_in_basket_opened_from_product_page** - Проверяет, что гость не видит товары в корзине, открытой со страницы товара
2. **test_guest_can_go_to_basket_page_from_product_page** - Проверяет, что гость может перейти в корзину со страницы товара

### Тесты для авторизованного пользователя (TestUserAddToBasketFromProductPage)

1. **test_user_cant_see_success_message** - Проверяет отсутствие сообщения об успехе при загрузке страницы
2. **test_user_can_add_product_to_basket** - Проверяет, что авторизованный пользователь может добавить товар в корзину
3. **test_user_should_see_add_to_basket_button** - Проверяет наличие кнопки добавления в корзину
4. **test_user_can_see_product_name** - Проверяет, что название товара отображается на странице
5. **test_user_can_see_product_price** - Проверяет, что цена товара отображается на странице

### Тесты для корзины авторизованного пользователя (TestUserBasketFromProductPage)

1. **test_user_can_go_to_basket_page_from_product_page** - Проверяет, что пользователь может перейти в корзину со страницы товара
2. **test_user_cant_see_product_in_basket_opened_from_product_page** - Проверяет, что пользователь не видит товары в пустой корзине

### Тесты главной страницы (TestLoginFromMainPage)

1. **test_guest_can_go_to_login_page** - Проверяет, что гость может перейти на страницу логина с главной страницы
2. **test_guest_should_see_login_link** - Проверяет, что гость видит ссылку на логин на главной странице
3. **test_guest_cant_see_product_in_basket_opened_from_main_page** - Проверяет, что гость не видит товары в корзине, открытой с главной страницы

## Запуск тестов

### Все тесты

```bash
pytest -v --language=en
```

### Тесты, отмеченные для ревью

```bash
pytest -v --tb=line --language=en -m need_review
```

### Запуск отдельного теста

```bash
pytest -v --language=en test_product_page.py::TestGuestLoginFromProductPage::test_guest_can_go_to_login_page_from_product_page
```

### Запуск всех тестов из определенного класса

```bash
pytest -v --language=en test_product_page.py::TestGuestLoginFromProductPage
```

### Запуск всех тестов из определенного файла

```bash
pytest -v --language=en test_product_page.py
```

### Параметры командной строки

- `--browser_name`: Выбор браузера (chrome или firefox, по умолчанию: chrome)
- `--language`: Выбор языка браузера (по умолчанию: en)

## Маркеры тестов

- `need_review`: Тесты, требующие проверки
- `login_guest`: Тесты для гостевого входа
- `xfail`: Тесты, которые ожидаемо падают

## Требования

- Python 3.8+
- pytest==5.1.1
- selenium==3.14.0
- Браузеры: Chrome и/или Firefox с соответствующими WebDriver 