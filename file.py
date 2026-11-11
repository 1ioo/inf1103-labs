# file.py contains all relevant information about the File class
import json
from inventory import Inventory
from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct
from supplier import Supplier
        
# File Class handles Loading and Saving of JSON Database
class File():
    # Loads Inventory in JSON to Inventory Object
    def load_inventory() -> Inventory:
        print("=" * 30)
        print("INVENTORY MANAGEMENT SYSTEM")
        print("=" * 30 + "\n")
        inventory = Inventory()
        try:
            with open("inventory.json", mode="a+") as file: # a+ opens the file for appending and reading but creates it if it doesn't exist
                file.seek(0) # put file pointer to start of file for reading
                print("Finding inventory.json...")
                
                # Load Inventory Object with Product Objects
                inventory_dict = json.load(file) # Loads Inventory Dictionary with Product Dictionaries
                for product in inventory_dict:
                    # Create Supplier Object and delete Supplier Parameters
                    supplier = Supplier(product["supplier_id"], product["supplier_name"], product["contact_email"])
                    del product["supplier_id"]
                    del product["supplier_name"]
                    del product["contact_email"]
                        
                    if product["type"] == "physical":
                        del product["type"]
                        product_object = PhysicalProduct(product["product_id"], product["name"], product["price"], product["stock"], supplier, product["weight"]) # Convert to PhysicalProduct Objects
                    else:
                        del product["type"]
                        product_object = DigitalProduct(product["product_id"], product["name"], product["price"], product["stock"], supplier, product["download_size"]) # Convert to DigitalProduct Objects
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
    def save_inventory(inventory: Inventory) -> bool:
        try:
            inventory_dict = []
            # Convert Inventory Object to Dictionary
            for product in inventory.product_list:
                product_dict = vars(product)
                if isinstance(product, PhysicalProduct):
                    clean_product = {key.replace("_PhysicalProduct__",""): value for key, value in product_dict.items()} # Replace Subclass Name Mangling
                    clean_product = {key.replace("_Product__",""): value for key, value in clean_product.items()} # Replace Super class Name Mangling
                    
                    # Handle Supplier Object and add as Key Value Pair
                    supplier = clean_product.pop("supplier")
                    clean_product.update({key.replace("_Supplier__", ""): value for key, value in vars(supplier).items()})
                    
                    clean_product["type"] = "physical" # Add in Physical Type
                    inventory_dict.append(clean_product)
                else: # DigitalProduct
                    clean_product = {key.replace("_DigitalProduct__",""): value for key, value in product_dict.items()} # Replace Subclass Name Mangling
                    clean_product = {key.replace("_Product__",""): value for key, value in clean_product.items()} # Replace Super class Name Mangling
                    
                    # Handle Supplier Object and add as Key Value Pair
                    supplier = clean_product.pop("supplier")
                    clean_product.update({key.replace("_Supplier__", ""): value for key, value in vars(supplier).items()})
                    
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