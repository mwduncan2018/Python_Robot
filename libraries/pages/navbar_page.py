from .base_page import BasePage

class NavbarPage(BasePage):
    # Selectors
    _PRODUCT_LIST_LINK = "css=[data-cy='ProductListNav']"
    _WATCH_LIST_LINK = "css=[data-cy='WatchListNav']"
    _CONTACT_LINK = "css=[data-cy='ContactNav']"

    def go_to_product_list(self):
        self.browser.click(self._PRODUCT_LIST_LINK)

    def go_to_watch_list(self):
        self.browser.click(self._WATCH_LIST_LINK)

    def go_to_contact(self):
        self.browser.click(self._CONTACT_LINK)