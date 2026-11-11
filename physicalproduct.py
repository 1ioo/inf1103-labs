# Child Class of Product to represent Physical Products
from product import Product
from canbeshipped import CanBeShipped
from supplier import Supplier

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, weight: float):
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight = weight
        
    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight:.2f}KG")
        self.get_fulfillment_info()
        print(f"Shipping Fee for Each Product Costs ${self.calculate_shipping_cost():.2f}")
        
    def get_fulfillment_info(self) -> None:
        print("The product requires physical shipping.")
        
    def calculate_shipping_cost(self) -> float:
        if self.__weight < 5:
            return 2.0
        else:
            return 4.0