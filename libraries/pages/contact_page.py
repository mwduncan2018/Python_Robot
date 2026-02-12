from .base_page import BasePage

class ContactPage(BasePage):
    # Selectors
    _SECRET_MESSAGE = "#secretMessage"
    _GITHUB_LINK = "#github a"
    _SKILL_LIST = "#skillList li"

    def get_github_href(self):
        return self.browser.get_attribute(self._GITHUB_LINK, "href")

    def get_footer_text(self):
        return self.browser.get_text(self._SECRET_MESSAGE)

    def get_all_skills(self):
        elements = self.browser.get_elements(self._SKILL_LIST)
        return [self.browser.get_text(el).strip() for el in elements]