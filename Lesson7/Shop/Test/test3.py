from Lesson7.Shop.Pages.Mainpage import ShopmainPage
from Lesson7.Shop.Pages.Cartpage import ShopCart


def test_shop(chrome_browser):
    expected_total = "58.29"

    shopmain = ShopmainPage(chrome_browser)
    shopmain.registration_fields()
    shopmain.find_add_to_cart_buttons()
    shopmain.add_to_cart()
    shopmain.make_order()

    container = ShopCart(chrome_browser)
    container.checkout()
    container.customer_data()
    container.get_total_price()

    assert expected_total in container.get_total_price()  
    print(f"Total price is ${container.get_total_price()}")
