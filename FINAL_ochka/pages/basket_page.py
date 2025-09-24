from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        """Проверка URL страницы корзины"""
        assert "basket" in self.browser.current_url, "URL does not contain 'basket'"
        
    def should_be_empty_basket(self):
        """Проверка, что корзина пуста"""
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is not empty, but should be"
            
    def should_be_empty_basket_message(self):
        """Проверка наличия сообщения о пустой корзине"""
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is not presented, but should be"
            
    def should_not_be_empty_basket_message(self):
        """Проверка отсутствия сообщения о пустой корзине"""
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is presented, but should not be"
            
    def should_be_items_in_basket(self):
        """Проверка наличия товаров в корзине"""
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "No items in basket, but should be" 