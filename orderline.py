from product import Product

class OrderLine():
    def __init__(self, product: Product, stock_quantity: int):
        self.product: Product = product
        self.quantity: int = stock_quantity
        
    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity