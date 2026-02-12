from .base_page import BasePage

class ProductPage(BasePage):
    # Selectors
    _BTN_ADD_NEW_PRODUCT = "text=Add New Product"
    _BTN_FUZZY_MATCHING = "#fuzzFuzz"
    _TABLE_ROWS = "tbody tr"

    # Column Selectors (relative to a row)
    _COL_MANUFACTURER = "td:nth-child(2)"
    _COL_MODEL = "td:nth-child(3)"
    _COL_PRICE = "td:nth-child(4)"
    _COL_STOCK = "td:nth-child(5)"
    _BTN_EDIT = "td:nth-child(6) a:nth-child(1)"
    _BTN_DETAILS = "td:nth-child(6) a:nth-child(2)"
    _BTN_DELETE = "td:nth-child(6) a:nth-child(3)"
    _CHK_MATCH = "td:nth-child(1)"
    _CHK_FUZZY_MATCH = "td:nth-child(7)"

    def add_new_product(self):
        self.browser.click(self._BTN_ADD_NEW_PRODUCT)

    def enable_standard_matching(self):
        if self.is_fuzzy_matching_enabled():
            self.browser.click(self._BTN_FUZZY_MATCHING)

    def enable_fuzzy_matching(self):
        if not self.is_fuzzy_matching_enabled():
            self.browser.click(self._BTN_FUZZY_MATCHING)

    def edit(self, product):
        row = self.get_product_row(product)
        self.browser.click(f"{row} >> {self._BTN_EDIT}")

    def details(self, product):
        row = self.get_product_row(product)
        self.browser.click(f"{row} >> {self._BTN_DETAILS}")

    def delete(self, product):
        row = self.get_product_row(product)
        self.browser.click(f"{row} >> {self._BTN_DELETE}")

    def is_fuzzy_matching_enabled(self):
        return self.browser.get_text(self._BTN_FUZZY_MATCHING) == "Disable Fuzzy Matching!"

    def get_product_row(self, product):
        m_name = product['manufacturer']
        model = product['model']    
        return (f"tbody tr:has(td:nth-child(2):has-text(\"{m_name}\"))"
                f":has(td:nth-child(3):has-text(\"{model}\"))")

    def is_product_displayed(self, product):
        row = self.get_product_row(product)
        is_visible = self.browser.get_element_states(row, "contains", "visible")
        price_match = self.browser.get_text(f"{row} >> {self._COL_PRICE}") == str(product['price'])
        stock_match = self.browser.get_text(f"{row} >> {self._COL_STOCK}") == str(product['numberInStock'])
        return is_visible and price_match and stock_match

    def is_product_a_match(self, product):
        status = self.browser.get_text(f"{self.get_product_row(product)} >> {self._CHK_MATCH}")
        return status.strip().lower() == "true"

    def is_product_a_fuzzy_match(self, product):
        row = self.get_product_row(product)
        fuzzy_cell = f"{row} >> {self._CHK_FUZZY_MATCH}"
        if self.browser.get_element_count(fuzzy_cell) > 0:
            status = self.browser.get_text(fuzzy_cell)
            return status.strip().lower() == "true"
        return False