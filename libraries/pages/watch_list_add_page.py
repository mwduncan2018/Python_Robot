from .base_page import BasePage

class WatchListAddPage(BasePage):
    # Selectors
    _INPUT_MANUFACTURER = "[data-cy='manufacturerInput']"
    _INPUT_MODEL = "[data-cy='modelInput']"
    _BTN_ADD = "[data-cy='submitButton']"

    def add_entry(self, entry):
        self.browser.fill_text(self._INPUT_MANUFACTURER, entry['manufacturer'])
        self.browser.fill_text(self._INPUT_MODEL, entry['model'])
        self.browser.click(self._BTN_ADD)