import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium.webdriver.common.action_chains import ActionChains

"""Избранное"""
class FavoritesPage(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)


    # Locators

    favorites = '//a[@title="Избранное"]'
    favorites_title = '//a[@class="personal-filter-link active"]'
    item_title = '//div[@class="item-group-header"]'


    # Getters

    def get_favorites(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.favorites)))

    def get_favorites_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.favorites_title)))

    def get_item_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_title)))


    # Actions

    def click_favorites(self):
        self.get_favorites().click()
        print('Произошел переход на страницу избранных товаров')

    def get_item_title_value(self):
        return self.get_item_title().text




    # Methods

    """Переход в раздел избранных товаров"""

    def go_to_favorites(self):
        self.click_favorites()
        self.assert_word(self.get_favorites_title(), 'Избранное')
        print('Произошел переход в избранное')



