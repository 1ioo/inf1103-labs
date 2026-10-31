# product.py contains all relevant information about the Product class and its subclasses

from abc import ABC, abstractmethod

# Stores Product Information and Manages Product Object
class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        # Private Attributes
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
    
    # Getter Methods
    @property
    def product_id(self):
        return self.__product_id
    
    @property
    def product_name(self):
        return self.__name
    
    @property
    def stock_quantity(self):
        return self.__stock
    
    # Updates Product's Stock Quantity
    def update_stock(self, quantity: int):
        if isinstance(quantity, int):
            self.__stock = quantity
            print("Stock Quantity Updated.\n")
        else:
            raise ValueError("Error: Enter a Positive Integer.\n")
    
    # Displays Product Summary
    def display_information(self):
        print(f"Product ID: {self.__product_id}")
        print(f"Product Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock Quantity: {self.__stock}")
        
    @abstractmethod
    def get_fulfillment_info(self):
        pass

# Interface for Physical Products that can be shipped
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass

# Child Class of Product to represent Physical Products
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight
        
    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight:.2f}KG")
        self.get_fulfillment_info()
        print(f"Shipping Fee for Each Product Costs ${self.calculate_shipping_cost():.2f}")
        
    def get_fulfillment_info(self):
        print("The product requires physical shipping.")
        
    def calculate_shipping_cost(self):
        if self.__weight < 5:
            return 2.0
        else:
            return 4.0

# Child Class of Product to represent Digital Products        
class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size
        
    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size:.2f} MB")
        self.get_fulfillment_info()
        
    def get_fulfillment_info(self):
        print("The product is delivered digitally.")