def load_inventory():
    try:
        with open("inventory.txt", mode="r") as file:
            orders = []
            for line in file.readlines():
                line = line.strip("\n")
                orders.append(line.split(","))
            return orders
    except FileNotFoundError:
        with open("inventory.txt", mode="w") as file:
            return []
    except Exception as e:
        return e
    
def display_inventory(inventory):
    msg = "Current Orders:\n"
    if inventory:
        for order in inventory:
            line = ""
            for item in order:
                line += item + ", "
            line = line[:-2] + "\n"
            msg += line
        return msg
    else:
        msg += "\t(no previous orders found)"
        return msg
    
def get_current_total_inventory(inventory):
    total = 0
    for item in inventory:
        total += int(item[-1])
    return total

def get_valid_input():
    product_name = input("Enter Product Name (or 'quit' to exit): ")
    if product_name.strip() and product_name.lower() != "quit":
        stock_quantity = input("Enter Stock Quantity (Type 'quit' to quit): ")
        if stock_quantity.isdigit() and int(stock_quantity) > 0:
            return int(stock_quantity)
    elif product_name.lower() == "quit":
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

inventory = load_inventory()
print(display_inventory())

total_inventory = get_current_total_inventory(inventory)
failed_entries = 0
delivery_total = 0

while total_inventory <= 500:
    user_input = get_valid_input()
    if user_input == "quit":
        generate_report(inventory, failed_entries, delivery_total)
        break
    elif user_input:
        inventory += user_input
        delivery_total += process_delivery(delivery_total, user_input)
        print(user_input, "stock recorded.")
    else:
        print("Error: Please Enter a Positive Integer.")
        failed_entries += 1
else:
    print("Inventory has Exceeded 500 Units!")