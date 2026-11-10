from orderline import OrderLine
from product import Product

class Order():
    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []
        
    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity) # Order is responsible for creating and managing its OrderLine objects.
        self.order_lines.append(order_line)
        
    def calculate_total(self):
        total = 0
        for order_line in self.order_lines:
            total += order_line.calculate_subtotal()
        return total