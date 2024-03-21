import time
import json
from playwright.sync_api import sync_playwright

from src.greencity.page.base import Home


def run():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("http://192.168.199.129:4205/#/ubs")
        # page.locator("app-ubs").get_by_role("link", name="Зареєструватись").click()
        # page.get_by_placeholder("example@email.com").click()
        # page.get_by_placeholder("example@email.com").type(text="galamagal86@gmail.com", delay=0.3)
        # page.query_selector("input[id='firstName']").type(text="galamagal86@gmail.com", delay=0.3)
        #
        # # ---------------------
        home = Home(page)\
            .click_reg()\
            .set_email("galamagal86@gmail.com")\
            .set_firstName("galamagal")\
            .set_pass("QWErty123!@#")
        print(home.get_reg_btn().is_disabled())
        home.set_re_pass("QWErty123!@#")

        print(home.get_reg_btn().is_disabled())
        home.click_reg()


        time.sleep(5)



if __name__ == "__main__":
    run()
