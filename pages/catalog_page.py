import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium.webdriver.common.action_chains import ActionChains

"""КАТАЛОГ ТОВАРОВ"""
class CatalogPage(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)


    # Locators

    catalog = '//button[@class="catalog-nav__toggle"]'
    catalog_naturalnye_tkani = '//span[@data-key="натуральные ткани"]'
    naturalnye_tkani_viskoza = '//a[@href="/naturalnye_tkani/viskoza_optom/"]'
    min_price = '(//input[@name="min-value"])[1]'
    max_price = '(//input[@name="max-value"])[1]'
    black_color = "//li[@class='filter-value']//input[@type='checkbox' and @value='черный']"
    black_color_current_filtr = '//li[@class="category-chosen-filters__item"]'
    item = '(//div[@class="item-groups-list-item"])[2]'
    item_title = '(//div[@class="item-group-header"])[2]'
    item_price_int = '(//span[@class="item-group-price"])[2]//span[@class="integer"]'






    # Getters

    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_catalog_naturalnye_tkani(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_naturalnye_tkani)))

    def get_naturalnye_tkani_viskoza(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.naturalnye_tkani_viskoza)))

    def get_min_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.min_price)))

    def get_max_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.max_price)))

    def get_black_color(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.black_color)))

    def get_black_color_current_filtr(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.black_color_current_filtr)))

    def get_item(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item)))

    def get_item_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_title)))

    def get_item_price_int(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_price_int)))




    # Actions


    def click_catalog(self):
        self.get_catalog().click()
        print('Открылось меню каталога')

    def move_to_element_catalog_naturalnye_tkani(self):
        self.actions.move_to_element(self.get_catalog_naturalnye_tkani()).perform()
        print('В каталоге наведен курсор на "Натуральные ткани"')

    def click_naturalnye_tkani_viskoza(self):
        self.get_naturalnye_tkani_viskoza().click()
        print('Прозошел переход на страницу "Натуральная вискоза"')

    def input_min_price(self):
        self.get_min_price().send_keys(Keys.CONTROL + "a")
        self.get_min_price().send_keys(Keys.DELETE)
        self.get_min_price().send_keys('300')
        print('Введена минимальная цена для фильтрации')

    def input_max_price(self):
        self.get_max_price().send_keys(Keys.CONTROL + "a")
        self.get_max_price().send_keys(Keys.DELETE)
        self.get_max_price().send_keys('500')
        time.sleep(2)
        print('Введена максимальная цена для фильтрации')


    def click_black_color(self):
        self.get_black_color().click()
        self.get_black_color().click()
        print('Осуществлено нажатие на фильтр "Черный цвет"')

    def get_item_title_value(self):
        return self.get_item_title().text

    def get_item_price_value_int(self):
        return self.get_item_price_int().text












    # Methods

    """Переход в Каталог"""
    def go_to_catalog(self):
        self.click_catalog()
        self.move_to_element_catalog_naturalnye_tkani()
        self.click_naturalnye_tkani_viskoza()

    """Применение фильтрации и открытие карточки товара"""
    def filtr(self):
        self.input_min_price()
        self.input_max_price()
        self.click_empty_space()
        self.click_black_color()
        self.assert_word(self.get_black_color_current_filtr(), 'цвет: черный')
        self.get_current_url()
        self.assert_url('https://star-tex.ru/naturalnye_tkani/viskoza_optom/?a_tsvet=%D1%87%D0%B5%D1%80%D0%BD%D1%8B%D0%B9&max_price=500&min_price=300')
        time.sleep(2)

    """ Открытие карточки товара"""
    def open_item_card(self):
        self.actions.move_to_element(self.get_item()).perform()
        self.get_item().click()
        print('Произошел переход на страницу карточки товара')
