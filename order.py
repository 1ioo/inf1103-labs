from orderline import OrderLine
from product import Product

class Order():
    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []
        
    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity) # Order is responsible for creating and managing its OrderLine objects.
        self.order_lines.append(order_line)
        print(f"Added {order_line.quantity} {order_line.product.product_name} to {self.order_id}.\n")
        
    def calculate_total(self):
        total = 0
        for order_line in self.order_lines:
            total += order_line.calculate_subtotal()
        return total
    
    def display_order_lines(self):
        for order_line in self.order_lines:
            print(f"Product Name: {order_line.product.product_name}")
            print(f"Order Line Subtotal: ${order_line.calculate_subtotal():.2f}\n")
            
    def remove_order_line(self, product_id: str):
        for order_line in self.order_lines:
            if order_line.product.product_id == product_id:
                self.order_lines.remove(order_line)
                print("Order Removed.\n")
                break
        else:
            print("Order Line not found.\n")