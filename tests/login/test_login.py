import re
from playwright.sync_api import expect
from pages.login import LoginPage

# 使用fixture注入login，这里直接返回的就是login page
def test_login_success(page):
    loginPage = LoginPage(page)
    loginPage.navigate()
    loginPage.login("24070201",'jsylx0301')
    expect(loginPage.page).to_have_url(re.compile(r"^https://.*/home/content$"))
