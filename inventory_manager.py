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

def display_all(inventory):
    print("\nCurrent Inventory")
    print("-" * 70)
    if inventory:
        for product in inventory:
            print(f"ID: {product['product_id']} | Name: {product['product_name']} | Price: ${product['product_price']:.2f} | Stock: {product['current_stock']}")
    else:
        print("No Products in Inventory.")
    print("-" * 70)
    
def add_product(inventory):
    print("\nAdd New Product")
    try:
        product_id = str(input("Product ID: "))
        product_name = str(input("Product Name: "))
        product_price = float(input("Price: "))
        current_stock = int(input("Stock Quantity: "))
        
        new_product = {"product_id" : product_id,
                        "product_name" : product_name,
                        "product_price" : product_price,
                        "current_stock" : current_stock
                       }

        inventory.append(new_product)
        print("\nProduct added successfully!\n")
    except Exception as e:
        print(f"Error Adding Product: {e}")
    
def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = str(input("Enter Product ID: "))
    for product in inventory:
        if product["product_id"] == product_id:
            print("\nProduct Found:")
            print("Name:", product["product_name"])
            print("Current Stock:", product["current_stock"], "\n")
            try:
                new_stock_quantity = int(input("New Stock Quantity: "))
                if new_stock_quantity >= 0:
                    product["current_stock"] = new_stock_quantity
                    print("\nStock updated successfully!\n")
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a Positive Integer.\n")
            break
            
    else: # for...else will execute if for loop doesn't meet break
        print("Product Not Found.\n")
        
def search_product(inventory):
    print("\nSearch Product")
    product_id = str(input("Enter Product ID: "))
    for product in inventory:
        if product["product_id"] == product_id:
            print("\nProduct Found")
            print("-" * 70)
            print("ID:", product["product_id"])
            print("Name:", product["product_name"])
            print(f"Price: ${product['product_price']:.2f}")
            print("Stock:", product["current_stock"])
            print("-" * 70 + "\n")
            break
    else:
        print("\nProduct not found.\n")
        
def save_inventory(inventory):
    try:
        with open("inventory.json", mode="w") as file:
            json.dump(inventory, file, indent=4)
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False

inventory = load_inventory()
print_menu()

while True:
    option = input("Enter Option: ")
    if option.isdigit() and 1 <= int(option) <= 6:
        option = int(option)
        if option == 1:
            display_all(inventory)
        elif option == 2:
            add_product(inventory)
        elif option == 3:
            update_stock(inventory)
        elif option == 4:
            search_product(inventory)
        elif option == 5:
            if save_inventory(inventory):
                print("\nSaving inventory...")
                print("Inventory saved successfully to inventory.json.\n")
            else:
                print("Error Saving Inventory. Please Try Again")
        elif option == 6:
            if save_inventory(inventory):
                print("\nSaving inventory before exit...")
                print("Inventory saved successfully.\n")
                print("Thank you for using Inventory Management System.")
                print("Program terminated.")
                break
            else:
                print("Error Saving Inventory.")
                exit_without_save = input("Exit Without Saving? (Yes/No): ")
                if exit_without_save.lower() == "yes":
                    break
                
    else:
        print("Invalid option. Enter a number from 1 to 6.\n")
        