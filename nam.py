import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="module")
def page(browser):
    page = browser.new_page()
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    yield page
    page.close()


def test_counter_displayed_and_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.avito.ru/avito-care/eco-impact")

        # Находим div с классом "desktop-wrapper-OutiE"
        target_div = page.locator(".desktop-wrapper-OutiE")

        # Проверяем, что div отображается на странице
        assert target_div.is_visible()

        # Делаем скриншот всего div
        target_div.screenshot(path="./output/counter_div.png")

        browser.close()
