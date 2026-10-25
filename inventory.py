class Product:
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        # Private Attributes
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
    
    # Updates Product's Stock Quantity
    def update_stock(self, quantity: int) -> None:
        if quantity.isdigit(): # isdigit checks for negative numbers as well.
            self.__stock = quantity
        else:
            print("Error: Enter a Positive Integer.")
    
    def display_information(self) -> None:
        pass
    
class Inventory:
    def __init__(self):
        pass
    
    def add_product(self):
        pass
    
    def search_product(self):
        pass
    
    def dispay_all(self):
        pass