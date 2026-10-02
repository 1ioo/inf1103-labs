import json

def load_inventory():
    print("=" * 30)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 30 + "\n")
    try:
        with open("inventory.json", mode="a+") as file: # a+ opens the file for appending and reading but creates it if it doesn't exist
            file.seek(0) # put file pointer to start of file for reading
            inventory = json.load(file)
            print("inventory.json found.")
            print("Inventory loaded successfully.\n")
    except json.decoder.JSONDecodeError:
        inventory = []
        print("File was not found or File is empty.")
        print("Empty inventory loaded.\n")
    except Exception as e:
        print(f"Error loading inventory: {e}")
        print("Empty inventory loaded.\n")
        inventory = []
    return inventory

def print_menu():
    print("-" * 10 + " MENU " + "-" * 10)
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("-" * 25 + "\n")
    

def display_inventory(inventory): # inventory = [[id,name,inventory],[id,name,inventory]]
    msg = "Current Orders:\n"
    if inventory:
        for order in inventory:
            line = ""
            for item in order:
                line += item + ", "
            line = line[:-2] + "\n" #:-2 clears out the extra ", " and replaces it with \n
            msg += line
        return msg
    else:
        msg += "\t(no previous orders found)"
        return msg

def get_current_total_inventory(inventory): #inventory = [[id,name,inventory],[id,name,inventory]]
    total = 0
    if inventory: # If inventory is not empty
        for item in inventory:
            total += int(item[-1])
    return total

def get_valid_input():
    product_name = input("Enter Product Name (or 'quit' to exit): ")
    if product_name.strip() and product_name.lower() != "quit": # If product_name is not empty and != quit
        stock_quantity = input("Enter Stock Quantity: ")
        if stock_quantity.isdigit() and int(stock_quantity) > 0:
            return [str(product_name), int(stock_quantity)]
        else:
            return False
    elif product_name.lower() == "quit":
        return "quit"
    else:
        return False

def add_to_inventory(inventory, order):
    # inventory = [[id,name,inventory],[id,name,inventory]]
    # order = [product_name, stock_quantity]
    
    new_id = len(inventory) + 1001
    order.insert(0, int(new_id)) # new order = [id, product_name, stock_quantity]
    inventory.append(order)
    msg = ""
    for fields in order:
        msg += str(fields) + ","
    msg = msg.strip(",") # strip the last ","
    print("New Order Added:")
    print(msg)
    print(f"Tax: ${calculate_tax(order[-1]):,.2f} | Total Inventory: {order[-1]}\n")
    return True

def save_inventory(inventory): # inventory = [[id,name,inventory],[id,name,inventory]]
    msg =""
    for order in inventory:
        for fields in order:
            msg += str(fields) + ","
        msg = msg[:-1]  + "\n" # remove final "," and replace with "\n"
    with open("inventory.txt", mode="w") as file:
        file.write(msg)
    print("Order successfully saved to inventory.txt")
                

def calculate_tax(amount):
    amount *= 0.1
    return amount

def process_delivery(stock_quantity):
    delivery_fee = 5
    total_cost = stock_quantity * delivery_fee + calculate_tax(stock_quantity * delivery_fee)
    return total_cost

def generate_report(transactions_recorded, total_units_processed, failed_attempts, delivery_total):
    print("\n=== Audit Report ===")
    print("Total Transactions Recorded:", transactions_recorded)
    print("Total Units Processed:", total_units_processed)
    print("Number of Failed/Rejected Entries:", failed_attempts)
    print(f"Total Delivery Fee: ${delivery_total:,.2f}")

inventory = load_inventory()
print(display_inventory(inventory))

failed_entries = 0

while get_current_total_inventory(inventory) <= 500:
    user_input = get_valid_input()
    if user_input == "quit":
        save_inventory(inventory)
        current_total_inventory = get_current_total_inventory(inventory)
        generate_report(len(inventory), current_total_inventory, failed_entries, process_delivery(current_total_inventory))
        break
    elif user_input:
        if add_to_inventory(inventory, user_input):
            print("Order successfully saved.\n")
        else:
            print("Error occured saving entry, please re-enter.")
            failed_entries += 1
    else:
        print("Error: Please Enter a Positive Integer.")
        failed_entries += 1
else:
    print("Inventory has Exceeded 500 Units!")