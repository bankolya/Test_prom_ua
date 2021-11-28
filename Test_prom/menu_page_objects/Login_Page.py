import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from base_page.BaseTool import BasePage
from test_data.test_data_menu import LoginData
from selenium.webdriver.common.by import By
from menu_page_objects.Product_and_Favorites_Page import ProductFavoritesPage


class LoginHelper(BasePage):
    def __init__(self, driver: WebDriver, cmdoptappurl):
        super().__init__(driver)
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get(cmdoptappurl)

    @allure.step("click_sign_in_one_access")
    def click_sign_in_one_access(self, button):
        with allure.step(f'open "{button}"and take screenshot'):
            locator_selector = (By.CSS_SELECTOR, button)
            field = self.find_element(locator_selector).click()
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
            return field

    @allure.step("click_login_button")
    def click_login_button(self, button):
        with allure.step(f'open "{button}"and take screenshot'):
            locator_selector = (By.ID, button)
            self.find_element(locator_selector).click()
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

    @allure.step('enter_user_data')
    def enter_user_data(self, locator, user_data):
        with allure.step(f'enter user data "{user_data}"'):
            login_input = (By.ID, locator)
            field = self.find_element(login_input)
            field.send_keys(user_data)
            field.send_keys(Keys.ENTER)
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

    def login(self):
        ld = LoginData()
        self.click_sign_in_one_access(ld.button_login)
        self.click_sign_in_one_access(ld.mail_aut)
        self.enter_user_data(ld.input_mail, ld.mail_data)
        self.enter_user_data(ld.input_password, ld.password_data)
        return ProductFavoritesPage(self.driver)