import pytest
from playwright.sync_api import sync_playwright, expect

from src.greencity.page.base import Home, RegPopUp


@pytest.fixture
def get_page():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("http://192.168.199.129:4205/#/ubs")
        yield page


@pytest.fixture
def page_logined(get_page):
    home = Home(get_page).header.set_language("UA")\
        .click_reg()\
        .set_email("galamagal86@gmail.com")\
        .set_firstName("galamagal")\
        .set_pass("QWErty123!@#")\
        .set_re_pass("QWErty123!@#")\
        .click_reg()
    return get_page

def test_change_language(page_logined):
    expect(RegPopUp(page_logined).get_reg_btn()).to_be_visible()
    expect(RegPopUp(page_logined).get_reg_btn()).to_be_disabled()



