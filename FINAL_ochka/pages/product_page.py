from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        """Добавление товара в корзину"""
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        
    def should_be_add_to_basket_button(self):
        """Проверка наличия кнопки добавления в корзину"""
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Add to basket button is not presented"
            
    def get_product_name(self):
        """Получение названия товара"""
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        
    def get_product_price(self):
        """Получение цены товара"""
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        
    def should_be_product_added_message(self):
        """Проверка сообщения о добавлении товара в корзину"""
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), \
            "Product added message is not presented"
            
    def should_be_basket_price_message(self):
        """Проверка сообщения о цене корзины"""
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE_MESSAGE), \
            "Basket price message is not presented"
            
    def should_product_name_match_added_message(self):
        """Проверка соответствия названия товара в сообщении о добавлении"""
        product_name = self.get_product_name()
        message_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_MESSAGE).text
        assert product_name == message_product_name, \
            f"Product name in message ({message_product_name}) does not match actual product name ({product_name})"
            
    def should_basket_price_match_product_price(self):
        """Проверка соответствия цены корзины цене товара"""
        product_price = self.get_product_price()
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MESSAGE).text
        assert product_price == basket_price, \
            f"Basket price ({basket_price}) does not match product price ({product_price})"
            
    def should_not_be_success_message(self):
        """Проверка отсутствия сообщения об успехе"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
            
    def should_success_message_disappear(self):
        """Проверка исчезновения сообщения об успехе"""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear, but should have" 