from robot.libraries.BuiltIn import BuiltIn

class BasePage:
    def __init__(self):
        try:
            self.browser = BuiltIn().get_library_instance('Browser')
        except Exception:
            self.browser = None

    def get_page(self):
        return self.browser.playwright.page