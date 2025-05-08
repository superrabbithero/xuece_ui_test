import pytest
from playwright.sync_api import Browser, BrowserContext, Page,expect
from pages.login import LoginPage
import re

@pytest.fixture(scope="session")
def browser() -> Browser:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # 改为 True 用于无头模式
        yield browser
        browser.close()

@pytest.fixture(scope="module") 
def context(browser: Browser) -> BrowserContext:
    return browser.new_context()

@pytest.fixture(scope="module") 
def page(context: BrowserContext) -> Page:
    return context.new_page()

@pytest.fixture(scope="module") 
def admin_login_page(page: Page) -> Page:
    loginPage = LoginPage(page)
    loginPage.navigate()
    loginPage.login("hd@admin",'jsylx0301')
    expect(loginPage.page).to_have_url(re.compile(r"^https://.*/home(/|$)"))
    return page