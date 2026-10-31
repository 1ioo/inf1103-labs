# inventory_manager.py contains the Main class which executes the main program flow

from file import File
from inventory import Inventory
from product import PhysicalProduct, DigitalProduct
        
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
                                break
                        else:
                            print("Product Not Found.\n")
                                
                    # Search for Product
                    elif option == 4:
                        print("\nSearch Product")
                        print("-" * 70)
                        product_id = Main.get_user_input(str, "Enter Product ID: ")
                        inventory.search_product(product_id)
                            
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