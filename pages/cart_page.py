from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from pages.catalog_page import CatalogPage
from selenium.webdriver.common.action_chains import ActionChains
from pages.item_card import ItemCard



"""КОРЗИНА"""
class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)


    # Locators

    item_cart_title = '//span[@class="item-group-name"]'
    item_cart_int_price = '(//span[@class="integer"])[1]'
    item_cart_float_price = '(//span[@class="fractional"])[1]'
    item_cart_int_price_total = '(//span[@class="integer"])[2]'
    item_cart_float_price_total = '(//span[@class="fractional"])[2]'


    # Getters

    def get_item_cart_title_value(self):
        get_item_cart_title = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_cart_title)))
        return get_item_cart_title.text

    def get_item_cart_int_price_value(self):
        get_item_cart_int_price = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_cart_int_price)))
        return get_item_cart_int_price.text

    def get_item_cart_float_price_value(self):
        get_item_cart_float_price = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_cart_float_price)))
        return get_item_cart_float_price.text

    def get_item_cart_price_value(self):
        get_item_cart_price_value = self.get_item_cart_int_price_value() + '.' + self.get_item_cart_float_price_value()
        return get_item_cart_price_value

    def get_item_cart_int_price_total(self):
        get_item_cart_int_price_total = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_cart_int_price_total)))
        return get_item_cart_int_price_total.text

    def get_item_cart_float_price_total(self):
        get_item_cart_float_price_total = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_cart_float_price_total)))
        return get_item_cart_float_price_total.text

    def get_item_cart_price_total(self):
        get_item_cart_price_total = self.get_item_cart_int_price_total() + '.' + self.get_item_cart_float_price_total()
        return get_item_cart_price_total




    # Actions



    #Methods
    """Проверка правильности итоговой суммы,
     полученной в результате умножения цены товара на его метраж,
      и сопоставление этой суммы с фактическим результатом + скрин"""
    def assert_itog_sum(self):
        print(f'get_item_cart_price_value(): {self.get_item_cart_price_value()}')
        itog_sum_fact = float(self.get_item_cart_price_value()) * 6
        itog_sum_ecpected = self.get_item_cart_price_total()
        itog_sum_ecpected = itog_sum_ecpected[0] + itog_sum_ecpected[2:] #преобразование суммы с "3 655,50" на "3655,50"
        print(f'itog_sum_fact: {itog_sum_fact}, itog_sum_ecpected: {itog_sum_ecpected}')
        assert itog_sum_fact ==  float(itog_sum_ecpected)
        print('ASSERT IS TRUE. Ожидаемая и фактическая итоговая сумма совпадают')
        self.get_screenshot()









