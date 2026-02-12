from .base_page import BasePage

class WatchListPage(BasePage):
    # Selectors
    _BTN_ADD_NEW_ENTRY = "text=Add To Watch List"
    _TABLE_ROWS = "tbody tr"

    # Column Selectors (relative to a row)
    _COL_MANUFACTURER = "td:nth-child(1)"
    _COL_MODEL = "td:nth-child(2)"
    _BTN_EDIT = "td:nth-child(3) a:nth-child(1)"
    _BTN_DETAILS = "td:nth-child(3) a:nth-child(2)"
    _BTN_DELETE = "td:nth-child(3) a:nth-child(3)"

    # Actions
    def add_new_entry(self):
        self.browser.click(self._BTN_ADD_NEW_ENTRY)

    def edit(self, entry):
        row = self.get_entry_row(entry)
        self.browser.click(f"{row} >> {self._BTN_EDIT}")

    def details(self, entry):
        row = self.get_entry_row(entry)
        self.browser.click(f"{row} >> {self._BTN_DETAILS}")

    def delete(self, entry):
        row = self.get_entry_row(entry)
        self.browser.click(f"{row} >> {self._BTN_DELETE}")

    def get_entry_row(self, entry):
        return (f"{self._TABLE_ROWS} >> "
                f"internal:has-text='{entry['manufacturer']}' >> "
                f"internal:has-text='{entry['model']}'")

    def is_entry_displayed(self, entry):
        row = self.get_entry_row(entry)
        return self.browser.get_element_states(row, "contains", "visible")