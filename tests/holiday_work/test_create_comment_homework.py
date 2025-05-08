import re
from playwright.sync_api import expect

from pages.commonHomework import CommonHomeworkPage

def test_goto_comment_homework_page(admin_login_page):
    mainPage = CommonHomeworkPage(admin_login_page)
    mainPage.navigate()
    mainPage.search_by_homework_name("hd-test-假期作业")
    expect(mainPage.table._table).to_contain_text("hd-test-假期作业")
    mainPage.table.to_menu(0)
    expect(mainPage.page).to_have_url("https://xuece-stagingtest1.unisolution.cn/home/homework/homework/topic/120?gradeDcode=S02&homeworkName=hd-test-%E5%81%87%E6%9C%9F%E4%BD%9C%E4%B8%9A&isManager=false")
    

def test_create_scheduling(admin_login_page):
    mainPage = CommonHomeworkPage(admin_login_page)
    mainPage.navigate()
    mainPage.search_by_homework_name("hd-test-假期作业")
    expect(mainPage.table._table).to_contain_text("hd-test-假期作业")
    mainPage.table.to_menu(0)
    mainPage.page.settimeout(500)
    mainPage.page.get_by_placeholder("请输入专题名称").fill("自由出题")
    mainPage.page.settimeout(500)
    mainPage.page.get_by_role("button",name="返回")