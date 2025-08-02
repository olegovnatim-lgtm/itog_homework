from base.base_class import Base


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""ЛИЧНЫЙ КАБИНЕТ"""
class LkPage(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # Locators

    lk_menu = '//span[@title="Личный кабинет"]'


    # Getters

    def get_lk_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.lk_menu)))

