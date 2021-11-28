from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def find_element(self, locator, time=30):
        ignored_exception = StaleElementReferenceException, NoSuchElementException
        try:
            return WebDriverWait(self.driver, time, ignored_exceptions=ignored_exception).until(
                es.element_to_be_clickable(locator), message=f"Can't find element by locator {locator}")
        except TimeoutError:
            print("TimeoutError is occurred")
