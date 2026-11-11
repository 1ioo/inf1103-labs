# product.py contains all relevant information about the Product class and its subclasses
from abc import ABC, abstractmethod
from supplier import Supplier

# Stores Product Information and Manages Product Object
class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier):
        # Private Attributes
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__supplier = supplier
    
    # Getter Methods
    @property
    def product_id(self) -> str:
        return self.__product_id
    
    @property
    def product_name(self) -> str:
        return self.__name
    
    @property
    def stock_quantity(self) -> int:
        return self.__stock
    
    @property
    def price(self) -> float:
        return self.__price
    
    # Updates Product's Stock Quantity
    def update_stock(self, quantity: int) -> None:
        if isinstance(quantity, int):
            self.__stock = quantity
            print("Stock Quantity Updated.\n")
        else:
            raise ValueError("Error: Enter a Positive Integer.\n")
    
    # Displays Product Summary
    def display_information(self) -> None:
        self.__supplier.display_information()
        print(f"Product ID: {self.__product_id}")
        print(f"Product Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock Quantity: {self.__stock}")
        
    @abstractmethod
    def get_fulfillment_info(self):
        pass