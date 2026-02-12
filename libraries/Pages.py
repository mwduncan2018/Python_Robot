from libraries.pages.navbar_page import NavbarPage
from libraries.pages.product_page import ProductPage
from libraries.pages.product_add_page import ProductAddPage
from libraries.pages.product_delete_page import ProductDeletePage
from libraries.pages.product_details_page import ProductDetailsPage
from libraries.pages.product_edit_page import ProductEditPage
from libraries.pages.watch_list_page import WatchListPage
from libraries.pages.watch_list_add_page import WatchListAddPage
from libraries.pages.watch_list_delete_page import WatchListDeletePage
from libraries.pages.watch_list_details_page import WatchListDetailsPage
from libraries.pages.watch_list_edit_page import WatchListEditPage
from libraries.pages.contact_page import ContactPage

class Pages:
    """
    Importing this one class in Robot gives access to all page objects.
    """
    ROBOT_LIBRARY_SCOPE = 'SUITE'

    def __init__(self):
        self.NavbarPage = NavbarPage()
        self.ProductPage = ProductPage()
        self.ProductAddPage = ProductAddPage()
        self.ProductDeletePage = ProductDeletePage()
        self.ProductDetailsPage = ProductDetailsPage()
        self.ProductEditPage = ProductEditPage()
        self.WatchListPage = WatchListPage()
        self.WatchListAddPage = WatchListAddPage()
        self.WatchListDeletePage = WatchListDeletePage()
        self.WatchListDetailsPage = WatchListDetailsPage()
        self.WatchListEditPage = WatchListEditPage()
        self.ContactPage = ContactPage()

    def get_keyword_names(self):
        """
        Find all public methods in the page objects.
        """
        attributes = [
            "NavbarPage", "ProductPage", "ProductAddPage", "ProductDeletePage",
            "ProductDetailsPage", "ProductEditPage", "WatchListPage", 
            "WatchListAddPage", "WatchListDeletePage", "WatchListDetailsPage", 
            "WatchListEditPage", "ContactPage"
        ]
        
        keywords = []
        for attr_name in attributes:
            obj = getattr(self, attr_name)
            methods = [m for m in dir(obj) if callable(getattr(obj, m)) and not m.startswith('_')]
            for method in methods:
                keywords.append(f"{attr_name}.{method}")
        return keywords

    def __getattr__(self, name):
        """
        When Robot calls 'Pages.ContactPage.Get All Skills',
        this method routes the call to the actual Python object.
        """
        if "." in name:
            attr_name, method_name = name.split(".", 1)
            if hasattr(self, attr_name):
                obj = getattr(self, attr_name)
                return getattr(obj, method_name)
        raise AttributeError(f"'Pages' object has no attribute '{name}'")