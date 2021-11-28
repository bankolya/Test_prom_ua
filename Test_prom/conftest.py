import allure
import pytest
from menu_page_objects.Login_Page import LoginHelper
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption("--cmdoptbrowser", action="store", default="chrome", help="my option: chrome or firefox")
    parser.addoption("--cmdoptwpurl", action="store",
                     default="https://prom.ua/p712545800-pokrishka-schwalbe-marathon.html ",
                     help="url prom")


def chrome_options(cmdoptbrowser):
    options = webdriver.ChromeOptions()
    if cmdoptbrowser == "chrome_headless":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-proxy-server")
        options.add_argument("--no-sandbox")
        options.add_argument('--lang=en-us')
        options.add_argument('--use-fake-ui-for-media-stream')
        options.add_argument("--window-size=1440x860")
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option('w3c', False)
    return options


def firefox_profile():
    profile = webdriver.FirefoxProfile()
    profile.set_preference('network.proxy.type', 0)
    profile.set_preference("security.sandbox.content.level", 5)
    profile.set_preference("intl.accept_languages", "en")
    profile.set_preference("media.navigator.streams.fake", True)
    profile.update_preferences()
    return profile


def set_up_chrome_driver(options):
    chrome_capabilities = webdriver.DesiredCapabilities.CHROME
    chrome_capabilities['loggingPrefs'] = {'browser': 'ALL'}
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                              desired_capabilities=chrome_capabilities,
                              options=options)
    return driver


def set_up_firefox_driver(profile, cmdoptbrowser):
    firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True
    options = None
    if "headless" in cmdoptbrowser:
        options = Options()
        options.headless = True
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                               desired_capabilities=firefox_capabilities,
                               firefox_profile=profile,
                               options=options)
    return driver


@pytest.fixture(scope="function")
def browser(cmdoptbrowser, cmdoptwpurl):
    if cmdoptbrowser == "firefox":
        firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                   desired_capabilities=firefox_capabilities)
        yield LoginHelper(driver, cmdoptwpurl)
        allure.attach(driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        driver.quit()
    elif cmdoptbrowser == "chrome":
        chrome_capabilities = webdriver.DesiredCapabilities.CHROME
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                  desired_capabilities=chrome_capabilities)
        driver.implicitly_wait(10)
        yield LoginHelper(driver, cmdoptwpurl)
        try:
            allure.attach(driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(e)
        driver.quit()


@pytest.fixture(scope='function')
def cmdoptbrowser(request):
    return request.config.getoption("--cmdoptbrowser")


@pytest.fixture(scope='function')
def cmdoptwpurl(request):
    return request.config.getoption("--cmdoptwpurl")
