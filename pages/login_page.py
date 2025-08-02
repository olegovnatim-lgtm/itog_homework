from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class LoginPage(Base):

    url = 'https://star-tex.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    menu_login = '//div[contains(text(), "Войти")]'
    phone_number = '//input[@id="login_login"]'
    password = '//input[@type="password"]'
    button_login = '//button[@type="submit"]'
    lk_menu = '//span[@class="user-bar-control__link-text"]'

    # Getters

    def get_menu_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_login)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_lk_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.lk_menu)))


    # Actions

    def click_menu_login(self):
        self.get_menu_login().click()
        print('Открылось модальное окно для авторизации')

    def input_phone_number(self, phone_number):
        self.get_phone_number().send_keys(phone_number)
        print('Поле "Номер телефона или email" заполнено')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Поле "Пароль" заполнено')

    def click_button_login(self):
        self.get_button_login().click()
        print('Произошло нажатие на кнопку Войти')



    # Methods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_menu_login()
        self.input_phone_number('79278690515')
        self.input_password('qwerty1997')
        self.click_button_login()
        self.assert_word(self.get_lk_menu(), 'Ирина И.')
