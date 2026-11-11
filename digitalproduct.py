# Child Class of Product to represent Digital Products        
from product import Product
from supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, download_size: float):
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size = download_size
        
    def display_information(self) -> None:
        super().display_information()
        print(f"Download Size: {self.__download_size:.2f} MB")
        self.get_fulfillment_info()
        
    def get_fulfillment_info(self) -> None:
        print("The product is delivered digitally.")