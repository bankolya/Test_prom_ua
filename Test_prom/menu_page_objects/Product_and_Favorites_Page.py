import allure
from selenium.webdriver.remote.webdriver import WebDriver
from base_page.BaseTool import BasePage
from selenium.webdriver.common.by import By


class ProductFavoritesPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    @allure.step("click_login_button")
    def click_favorite(self, button):
        with allure.step(f'open "{button}"and take screenshot'):
            locator_selector = (By.CSS_SELECTOR, button)
            self.find_element(locator_selector).click()
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
            return self

    @allure.step("click_login_button")
    def click_favorite_button(self, button):
        with allure.step(f'open "{button}"and take screenshot'):
            locator_selector = (By.XPATH, button)
            self.find_element(locator_selector).click()
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

    @allure.step("click_login_button")
    def delete_check(self, button):
        with allure.step(f'open "{button}"and take screenshot'):
            locator_selector = (By.CSS_SELECTOR, button)
            self.find_element(locator_selector)
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

    def check_data(self, queue_tab_table_data):
        for key, value in queue_tab_table_data.items():
            locator_selector = (By.CSS_SELECTOR, f"[class*='{key}']")
            data = self.find_element(locator_selector)
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
            assert data.text == value, f"CURR:'{data.text}' instead of EXP:'{value, self.driver.current_url} '"
        return self

    def check_data_text(self, queue_tab_table_data):
        for key, value in queue_tab_table_data.items():
            locator_selector = (By.CSS_SELECTOR, f"[data-qaid*='{key}']")
            data = self.find_element(locator_selector)
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
            assert data.text == value, f"CURR:'{data.text}' instead of EXP:'{value, self.driver.current_url}'"
