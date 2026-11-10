from product import Product

# inventory.py contains all relevant information about the Inventory class
# Inventory Class handles Inventory Management System
class Inventory:
    def __init__(self):
        self.__product_list: list[Product] = [] # Stores Product Objects in this List
    
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
    def search_product(self, product_id: str) -> Product | None: # return the matching Product, or None if it cannot be found
        for product_object in self.__product_list:
            if product_object.product_id == product_id:
                return product_object
        else:
            return None
            
    # Remove Product
    def remove_product(self, product_id: str):
        for product_object in self.__product_list:
            if product_object.product_id == product_id:
                self.__product_list.remove(product_object)
                print(f"{product_object.__name} removed.")
        else:
            print(f"{product_id} not found.")
    
    # Display all Products
    def display_all(self):
        print("\nCurrent Inventory")
        print("-" * 70)
        if self.__product_list:
            for product_object in self.__product_list:
                product_object.display_information()
                print()
        else:
            print("No Products in Inventory.\n")