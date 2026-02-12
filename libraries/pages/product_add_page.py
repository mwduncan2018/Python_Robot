from .base_page import BasePage

class ProductAddPage(BasePage):
    # Selectors
    _INPUT_MANUFACTURER = "[data-cy='manufacturerInput']"
    _INPUT_MODEL = "[data-cy='modelInput']"
    _INPUT_PRICE = "[data-cy='priceInput']"
    _INPUT_STOCK = "[data-cy='numberInStockInput']"
    _BTN_ADD = "[data-cy='submitButton']"

    def add_product(self, product):
        self.browser.type_text(self._INPUT_MANUFACTURER, product.manufacturer)
        self.browser.type_text(self._INPUT_MODEL, product.model)
        self.browser.type_text(self._INPUT_PRICE, str(product.price))
        self.browser.type_text(self._INPUT_STOCK, str(product.number_in_stock))
        self.browser.click(self._BTN_ADD)