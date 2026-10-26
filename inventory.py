import json

class Product:
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        # Private Attributes
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
    
    # Getter Method for Product ID Field
    @property
    def product_id(self):
        return self.__product_id
    
    @property
    def product_name(self):
        return self.__name
    
    # Updates Product's Stock Quantity
    def update_stock(self, quantity: int):
        if quantity.isdigit(): # isdigit checks for negative numbers as well.
            self.__stock = quantity
            print("Stock Quantity Updated.")
        else:
            print("Error: Enter a Positive Integer.")
    
    # Displays Product Summary
    def display_information(self):
        print(f"Product ID: {self.__product_id}")
        print(f"Product Name: {self.__name}")
        print(f"Price: {self.__price}")
        print(f"Stock Quantity: {self.__stock}")

# Inventory Class handles Inventory Management System
class Inventory:
    def __init__(self):
        self.__product_list = [] # Stores Product Objects in this List
    
    # Getter for Product List
    @property
    def product_list(self):
        return self.__product_list
    
    # Adds Product to Product List
    def add_product(self, product_object: Product):
        if isinstance(product_object, Product):
            self.__product_list.append(product_object)
            print(f"{product_object.product_name} added to Inventory.")

    # Searches for Products
    def search_product(self, product_id: str):
        for product_object in self.__product_list:
            if product_object.product_id == product_id:
                print("Product Found")
                print("-" * 70)
                product_object.display_information()
            else:
                print("Product Not Found.")
    
    # Display all Products
    def dispay_all(self):
        print("Current Inventory")
        print("-" * 70)
        if self.__product_list:
            for product_object in self.__product_list:
                product_object.display_information()
        else:
            print("No Products in Inventory.")
        
# File Class handles Loading and Saving of JSON Database
class File():
    def load_inventory():
        print("=" * 30)
        print("INVENTORY MANAGEMENT SYSTEM")
        print("=" * 30 + "\n")
        inventory = Inventory()
        try:
            with open("inventory.json", mode="a+") as file: # a+ opens the file for appending and reading but creates it if it doesn't exist
                file.seek(0) # put file pointer to start of file for reading
                print("inventory.json found.")
                
                # Load Inventory Object with Product Objects
                inventory_dict = json.load(file) # Loads Inventory Dictionary with Product Dictionaries
                for product in inventory_dict:
                    product_object = Product(**product) # Convert Product Dictionaries to Product Objects via **kwargs unpacking
                    inventory.add_product(product_object)
                print("Inventory loaded successfully.\n")
        except json.decoder.JSONDecodeError:
            print("File was not found or File is empty.")
            print("Empty inventory loaded.\n")
        except Exception as e:
            print(f"Error loading inventory: {e}")
            print("Empty inventory loaded.\n")
        return inventory
    
    def save_inventory(inventory: Inventory):
        try:
            inventory_dict = [vars(product) for product in inventory] # Convert Product Objects to Product Dictionaries
            with open("inventory.json", mode="w") as file:
                json.dump(inventory, file, indent=4)
                return True
        except Exception as e:
            print(f"Error saving file: {e}")
            return False        
        
# Main Class handles Main Program Flow
class Main():
    # Display Main Menu
    def display_menu():
        print("-" * 10 + " MENU " + "-" * 10)
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("-" * 25 + "\n")
        
    # Get User Input
    def get_user_input(convert_type, prompt):
        try:
            user_input = convert_type(input(prompt)) # Type Conversion
            # Input Validation
            if convert_type == str:
                if not user_input.strip():
                    raise ValueError("Field cannot be Empty.")
            elif convert_type in (int, float):
                if user_input < 0:
                    raise ValueError("Enter a Non-Negative Number.")
            
            return user_input
        except ValueError as e:
            raise ValueError(e)
            
    # Main Program Flow
    def main():
        inventory = File.load_inventory()
        Main.display_menu()
        while True:
            option = input("Enter Option: ")
            if option.isdigit() and 1 <= int(option) <= 6:
                option = int(option)
                if option == 1: # Display All Products
                    inventory.display_all()
                elif option == 2: # Add Product
                    try:
                        print("Add New Product")
                        product_id = Main.get_user_input(str, "Enter Product ID: ")
                        product_name = Main.get_user_input(str, "Enter Product Name: ")
                        price = Main.get_user_input(str, "Enter Price: ")
                        stock_quantity = Main.get_user_input(str, "Enter Stock Quantity: ")
                    
                        product_object = Product(product_id, product_name, price, stock_quantity)
                        inventory.add_product(product_object)
                    except ValueError as e:
                        print(f"Error: {e}")
                elif option == 3:
                    # update_stock(inventory)
                    print("Update Stock Quantity")
                    product_id = Main.get_user_input(str, "Enter Product ID: ")
                    for product in inventory:
                        if product.product_id == product_id:
                            print("\nProduct Found:")
                            product.display_information()

                            try:
                                stock_quantity = Main.get_user_input(int, "Enter New Stock Quantity: ")
                                product.update_stock(stock_quantity)
                            except ValueError as e:
                                print(f"Error: {e}")
                elif option == 4:
                    # search_product(inventory)
                    pass
                elif option == 5:
                    # if save_inventory(inventory):
                    #     print("\nSaving inventory...")
                    #     print("Inventory saved successfully to inventory.json.\n")
                    # else:
                    #     print("Error Saving Inventory. Please Try Again")
                    pass
                elif option == 6:
                    # if save_inventory(inventory):
                    #     print("\nSaving inventory before exit...")
                    #     print("Inventory saved successfully.\n")
                    #     print("Thank you for using Inventory Management System.")
                    #     print("Program terminated.")
                    #     break
                    # else:
                    #     print("Error Saving Inventory.")
                    #     exit_without_save = input("Exit Without Saving? (Yes/No): ")
                    #     if exit_without_save.lower() == "yes":
                    #         break
                    pass
                        
            else:
                print("Invalid option. Enter a number from 1 to 6.\n")