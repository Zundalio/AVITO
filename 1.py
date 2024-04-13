import pytest
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope="module")
def page(browser):
    page = browser.new_page()
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    yield page
    page.close()


def test_water_counter_screenshot(page):
    water_counter_div = page.locator(".desktop-impact-item-eeQO3:nth-child(4)")
    water_counter_div.screenshot(path="./output/test-case-1.png")


def test_co2_counter_screenshot(page):
    co2_counter = page.locator(".desktop-impact-item-eeQO3:nth-child(2)")
    co2_counter.screenshot(path="./output/test-case-2.png")


def test_energy_counter_screenshot(page):
    energy_counter = page.locator(".desktop-impact-item-eeQO3:nth-child(6)")
    energy_counter.screenshot(path="./output/test-case-3.png")



