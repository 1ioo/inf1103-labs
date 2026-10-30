import json
from abc import ABC, abstractmethod

# Stores Product Information and Manages Product Object
class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        # Private Attributes
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
    
    # Getter Methods
    @property
    def product_id(self):
        return self.__product_id
    
    @property
    def product_name(self):
        return self.__name
    
    @property
    def stock_quantity(self):
        return self.__stock
    
    # Updates Product's Stock Quantity
    def update_stock(self, quantity: int):
        if isinstance(quantity, int):
            self.__stock = quantity
            print("Stock Quantity Updated.\n")
        else:
            print("Error: Enter a Positive Integer.")
    
    # Displays Product Summary
    def display_information(self):
        print(f"Product ID: {self.__product_id}")
        print(f"Product Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock Quantity: {self.__stock}")
        
    @abstractmethod
    def get_fulfillment_info(self):
        pass

# Interface for Physical Products that can be shipped
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass

# Child Class of Product to represent Physical Products
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight
        
    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight:.2f}KG")
        self.get_fulfillment_info()
        print(f"Shipping Fee for Each Product Costs ${self.calculate_shipping_cost():.2f}")
        
    def get_fulfillment_info(self):
        print("The product requires physical shipping.")
        
    def calculate_shipping_cost(self):
        if self.__weight < 5:
            return 2.0
        else:
            return 4.0

# Child Class of Product to represent Digital Products        
class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size
        
    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size:.2f} MB")
        self.get_fulfillment_info()
        
    def get_fulfillment_info(self):
        print("The product is delivered digitally.")

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
            return True
        else:
            return False

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
    def display_all(self):
        print("\nCurrent Inventory")
        print("-" * 70)
        if self.__product_list:
            for product_object in self.__product_list:
                product_object.display_information()
                print()
        else:
            print("No Products in Inventory.")
        
# File Class handles Loading and Saving of JSON Database
class File():
    # Loads Inventory in JSON to Inventory Object
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
                    if product["type"] == "physical":
                        del product["type"]
                        product_object = PhysicalProduct(**product) # Convert to PhysicalProduct Objects via **kwargs unpacking
                    else:
                        del product["type"]
                        product_object = DigitalProduct(**product) # Convert to DigitalProduct Objects via **kwargs unpacking
                    inventory.add_product(product_object)
                    
                print("Inventory loaded successfully.\n")
        except json.decoder.JSONDecodeError:
            print("File was not found or File is empty.")
            print("Empty inventory loaded.\n")
        except Exception as e:
            print(f"Error loading inventory: {e}")
            print("Empty inventory loaded.\n")
        return inventory
    
    # Saves Inventory Object into JSON Database
    def save_inventory(inventory: Inventory):
        try:
            inventory_dict = []
            # Convert Inventory Object to Dictionary
            for product in inventory.product_list:
                product_dict = vars(product)
                if isinstance(product, PhysicalProduct):
                    clean_product = {key.replace("_PhysicalProduct__",""): value for key, value in product_dict.items()} # Replace Subclass Name Mangling
                    clean_product = {key.replace("_Product__",""): value for key, value in clean_product.items()} # Replace Super class Name Mangling
                    clean_product["type"] = "physical" # Add in Physical Type
                    inventory_dict.append(clean_product)
                else: # DigitalProduct
                    clean_product = {key.replace("_DigitalProduct__",""): value for key, value in product_dict.items()} # Replace Subclass Name Mangling
                    clean_product = {key.replace("_Product__",""): value for key, value in clean_product.items()} # Replace Super class Name Mangling
                    clean_product["type"] = "digital" # Add in Digital Type
                    inventory_dict.append(clean_product)
                
            # Writing into JSON Database
            with open("inventory.json", mode="w") as file:
                json.dump(inventory_dict, file, indent=4)
                print("\nSaving inventory...")
                print("Inventory saved successfully to inventory.json.\n")
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
            user_input = input(prompt)
            # Input Validation
            if not user_input.strip():
                raise ValueError("Input cannot be Empty.\n")
            
            try:
                # Convert int and float
                if convert_type in (int, float):
                    user_input = convert_type(user_input)
                    if user_input <= 0: # Make sure number is not negative and not 0
                        raise ValueError
                # Convert string
                else:
                    user_input = convert_type(user_input) # Type Conversion
            except ValueError as e:
                if convert_type == int:
                    raise ValueError("Enter a Non-Negative Integer\n")
                elif convert_type == float:
                    raise ValueError("Input a Non-Negative Number\n")
            
            return user_input
        except ValueError as e:
            raise ValueError(e)
            
    # Main Program Flow
    def main():
        inventory = File.load_inventory()
        Main.display_menu()
        while True:
            try:
                option = Main.get_user_input(int, "Enter Option: ")
                if 1 <= option <= 6:
                    # Display All Products
                    if option == 1:
                        inventory.display_all()
                        
                    # Add Product
                    elif option == 2:
                        print("\nAdd New Product")
                        print("-" * 70)
                        
                        # Getting User Input for Initialisation
                        product_id = Main.get_user_input(str, "Enter Product ID: ")
                        product_name = Main.get_user_input(str, "Enter Product Name: ")
                        price = Main.get_user_input(float, "Enter Price: ")
                        stock_quantity = Main.get_user_input(int, "Enter Stock Quantity: ")
                        product_type = Main.get_user_input(str, "Enter Product Type (physical/digital): ").lower()

                        # Inititalising Object based off Physical or Digital Products
                        if product_type == "physical":
                            weight = Main.get_user_input(float, "Enter Weight (kg): ")
                            product_object = PhysicalProduct(product_id, product_name, price, stock_quantity, weight)
                        elif product_type == "digital":
                            download_size = Main.get_user_input(float, "Enter Download Size (MB): ")
                            product_object = DigitalProduct(product_id, product_name, price, stock_quantity, download_size)
                        else:
                            raise TypeError("Enter the correct product type.\n")
                        
                        # Add Product to Inventory's Product List
                        if inventory.add_product(product_object):
                            print(f"{product_object.product_name} added Successfully.\n")
                        else:
                            print(f"Failed to add {product_object.product_name}\n")
                            
                    # Update Stock Quantity
                    elif option == 3:
                        print("\nUpdate Stock Quantity")
                        print("-" * 70)
                        product_id = Main.get_user_input(str, "Enter Product ID: ")
                        for product in inventory.product_list:
                            if product.product_id == product_id:
                                print("\nProduct Found:")
                                product.display_information()
                                stock_quantity = Main.get_user_input(int, "\nEnter New Stock Quantity: ")
                                product.update_stock(stock_quantity)
                                
                    # Search for Product
                    elif option == 4:
                        print("\nSearch Product")
                        print("-" * 70)
                        product_id = Main.get_user_input(str, "Enter Product ID: ")
                        for product in inventory.product_list:
                            if product.product_id == product_id:
                                print("\nProduct Found:")
                                product.display_information()
                                print()
                                break
                            
                    # Save Inventory into JSON Database
                    elif option == 5:
                        File.save_inventory(inventory)
                        
                    # Save Inventory into JSON Database and QUIT
                    elif option == 6:
                        if File.save_inventory(inventory):
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
            except ValueError as e: # User Input Validation Failed
                print(f"Error: {e}")
            except TypeError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error: {e}")
            
        
if __name__ == "__main__":
    Main.main() # Main Program Flow