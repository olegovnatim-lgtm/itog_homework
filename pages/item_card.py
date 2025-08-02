import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from pages.catalog_page import CatalogPage
from selenium.webdriver.common.action_chains import ActionChains

"""КАРТОЧКА ТОВАРА"""
class ItemCard(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)


    # Locators

    item_card_title = '(//h1[@class="item-group-data__name"])[2]'
    item_card_price_1_int = '(//span[@class="item-group__price-value"]//span[@class="price"])[2]//span[@class="integer"]'
    item_card_price_2_int = '(//span[@class="pack-type-select-price"]//span[@class="integer"])[6]'
    item_add_to_cart = "(//span[normalize-space(translate(@title, ' ', ' '))='6 м в нарезку'])[2]"
    order_button = '(//a[@title="Перейти в корзину"])[3]'
    favorites_button = '(//span[@class="item-action toggle-to-favorite"])[2]'
    close_card = '(//span[@class="close-button item-groups-slider__closer swiper-no-swiping"])[2]'

    # Getters

    def get_item_card_title_value(self):
        get_item_card_title = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_card_title)))
        return get_item_card_title.text


    def get_item_card_price_1_int_value(self):
        get_item_card_price_int = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_card_price_1_int)))
        return get_item_card_price_int.text


    def get_item_card_price_2_int_value(self):
        get_item_card_price_int = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_card_price_2_int)))
        return get_item_card_price_int.text



    def get_item_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_add_to_cart)))

    def get_order_button(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.order_button)))

    def get_favorites_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.favorites_button)))

    def get_close_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_card)))

    # Actions

    def click_item_add_to_cart(self):
        self.get_item_add_to_cart().click()
        print("Товар добавлен в корзину")

    def click_order_button(self):
        self.get_order_button().click()
        print('Произошел переход в корзину')

    def click_favorites_button(self):
        self.get_favorites_button().click()
        print('Товар добавлен в избранное')

    def click_close_card(self):
        self.get_close_card().click()
        print('Карточка товара закрыта')





    # Methods
    """Сверка цены и наименования выбранного товара"""
    def assert_card_item_value(self):
        assert CatalogPage(self.driver).get_item_price_value_int() == self.get_item_card_price_1_int_value()
        print('ASSERT IS TRUE. Цена выбранного товара из каталога совпадает с ценой товара в карточке товара')

        if CatalogPage(self.driver).get_item_title_value() in self.get_item_card_title_value():
            print('ASSERT IS TRUE. Наименование выбранного товара из каталога совпадает с наименование в карточке товара')






