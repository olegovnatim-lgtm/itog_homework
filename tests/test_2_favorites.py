from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.favorites_page import FavoritesPage
from pages.login_page import LoginPage
from pages.item_card import ItemCard


def test_favorites(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--guest")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print('Начала проверка добавления товара в избранное')

    login = LoginPage(driver)

    """Авторизация"""
    login.authorization()



    cp = CatalogPage(driver)

    """Переход в Каталог"""
    cp.go_to_catalog()

    """Сохранение значения наименования товара для последующего сравнения с наименованием товара в корзине"""
    item_title_value_in_catalog = cp.get_item_title_value()

    """ Открытие карточки товара"""
    cp.open_item_card()




    ic = ItemCard(driver)

    """Добавление товара в избранное"""
    ic.click_favorites_button()

    """Закрытие карточки товара"""
    ic.click_close_card()



    fp = FavoritesPage(driver)

    """Переход в Избранное"""
    fp.go_to_favorites()

    """Сравнение наименования товара из карточки товара с наименованием товара в избранном"""
    assert item_title_value_in_catalog == fp.get_item_title_value()
    print('ASSERT IS TRUE Товар успешно добавлен в избранное')
