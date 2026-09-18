def get_valid_input():
    stock_quantity = input("Enter Stock Quantity (Type 'quit' to quit): ")
    if stock_quantity.isdigit() and int(stock_quantity) > 0:
        return int(stock_quantity)
    elif stock_quantity.lower() == "quit":
        return "quit"
    else:
        return False

def calculate_tax(amount):
    amount *= 0.1
    return amount

def process_delivery(current_total, new_value):
    delivery_fee = 5
    current_total += new_value * delivery_fee + calculate_tax(new_value * delivery_fee)
    return current_total

def generate_report(total_units, failed_attempts, delivery_total):
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)
    print("Total Delivery Fee:", delivery_total)

inventory = 0
failed_entries = 0
delivery_total = 0

while inventory <= 500:
    inventory_input = get_valid_input()
    if inventory_input == "quit":
        generate_report(inventory, failed_entries, delivery_total)
        break
    elif inventory_input:
        inventory += inventory_input
        delivery_total += process_delivery(delivery_total, inventory_input)
        print(inventory_input, "stock recorded.")
    else:
        print("Error: Please Enter a Positive Integer.")
        failed_entries += 1
else:
    print("Inventory has Exceeded 500 Units!")