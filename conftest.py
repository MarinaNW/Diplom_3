import pytest
from selenium import webdriver

from urls import Urls


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()

    browser.get(Urls.BASE_URL)

    yield browser

    browser.quit()


