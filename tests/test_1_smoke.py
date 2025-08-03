from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.login_page import LoginPage
from pages.item_card import ItemCard


def test_smoke(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--guest")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print('Начало дымового тестирования')


    login = LoginPage(driver)

    """Авторизация"""
    login.authorization()



    cp = CatalogPage(driver)

    """Переход в Каталог"""
    cp.go_to_catalog()

    """Применение фильтрации в каталоге"""
    cp.filtr()

    """ Открытие карточки товара"""
    cp.open_item_card()



    ic = ItemCard(driver)

    """Сравнение цены и наименования из карточки товара с ценой и наименованием товара из каталога"""
    ic.assert_card_item_value()

    """Сохранение значения цены/наименования товара для последующего сравнения с ценой,наименование товара в корзине"""
    item_title_value_in_card = ic.get_item_card_title_value()
    item_price_value_int_in_card = ic.get_item_card_price_2_int_value()

    """Добавления товара к корзину"""
    ic.click_item_add_to_cart()

    """Переход в корзину"""
    ic.click_order_button()



    cap = CartPage(driver)

    """Сравнение цены товара из карточки товара с ценой в корзине"""
    print(item_price_value_int_in_card)
    print(cap.get_item_cart_int_price_value())
    assert item_price_value_int_in_card == cap.get_item_cart_int_price_value()
    print('ASSERT IS TRUE Цена товара из карточки товара совпадает с ценой товара в корзине')

    """Сравнение наименование товара из карточки товара с наименованием в корзине 
    (поскольку к наименованию в корзине прибавляются еще значения, то было решено сделать проверку на частичное сравнение)"""
    if item_title_value_in_card in cap.get_item_cart_title_value():
        print('ASSERT IS TRUE Наименование товара из карточки товара совпадает с ценой товара в корзине')


    """Проверка правильности итоговой суммы,
         полученной в результате умножения цены товара на его метраж,
          и сопоставление этой суммы с фактическим результатом + скрин"""
    cap.assert_itog_sum()


    print('Дымовое тестирование проведено успешно')

    driver.quit()