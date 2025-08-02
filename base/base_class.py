import datetime

from selenium.webdriver import ActionChains


class Base():

    def __init__(self, driver):
        self.driver = driver


    """Метод для получения текущего URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Текущий URL: {get_url}')

    def assert_url(self, expected_url):
        currenturl = self.driver.current_url
        assert currenturl == expected_url
        print('Фактический URL совпадает с ожидаемым URL')



    """Метод для сверки текста"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('ASSERT IS TRUE')




    """Метод для нажатия на пустое пространство"""

    def click_empty_space(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        print('Нажатие на пустое пространство успешно')




    """Метод для скриншота"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%H.%M.%S-%Y.%m.%d")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot(f"C:\\Users\\olego\\PycharmProjects\\itog_homework\\screen\\" + name_screenshot)


