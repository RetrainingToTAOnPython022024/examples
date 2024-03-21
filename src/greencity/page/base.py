class RegPopUp:
    def __init__(self, page):
        self.page = page

    def set_email(self, email):
        self.page.get_by_placeholder("example@email.com").type(text=email, delay=0.3)
        return self

    def set_firstName(self, firstName):
        self.page.query_selector("input[id='firstName']").type(text=firstName, delay=0.3)
        return self

    def set_pass(self, password):
        self.page.locator("#password").type(text=password, delay=0.3)

        return self

    def set_re_pass(self, password):
        self.page.locator("#repeatPassword").type(text=password, delay=0.3)
        return self

    def get_reg_btn(self):
        return self.page.get_by_role("link", name="Зареєструватись")

    def click_reg(self):
        self.page.get_by_role("link", name="Зареєструватись").click()


class Home:
    def __init__(self, page):
        self.page = page

    def click_reg(self):
        self.page.locator("app-ubs").get_by_role("link", name="Зареєструватись").click()
        return RegPopUp(self.page)
