from test_data.test_data_menu import ProductFavoritesData
import allure
import pytest


# pytest --alluredir="test/results" -v --maxfail=0 -m regression tests/test_prom.py --cmdoptbrowser="chrome"


@allure.title('Check_add_product_and_delete')
@pytest.mark.regression
@pytest.mark.check_add_product_and_delete
def test_check_add_product_and_delete(browser):
    pfd = ProductFavoritesData()
    login_page = browser
    product_page = login_page.login()
    product_page.click_favorite(pfd.favorites_selector)
    product_page.check_data(pfd.favorites_count)
    product_page.click_favorite_button(pfd.favorites_button)
    product_page.check_data_text(pfd.product_name)
    product_page.click_favorite(pfd.delete_product)
    product_page.delete_check(pfd.locator_delete)


@allure.title('Check_count_favorites')
@pytest.mark.regression
@pytest.mark.check_count_favorites
def test_check_count_favorites(browser):
    pfd = ProductFavoritesData()
    login_page = browser
    product_page = login_page.login()
    product_page.click_favorite(pfd.favorites_selector)
    product_page.check_data(pfd.favorites_count)
    product_page.click_favorite_button(pfd.favorites_button)
    product_page.check_data(pfd.favorites_list_count)
