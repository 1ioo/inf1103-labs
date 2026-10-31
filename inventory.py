from product import Product

# inventory.py contains all relevant information about the Inventory class
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
                print("\nProduct Found")
                print("-" * 70)
                product_object.display_information()
                print()
                break
        else:
            print("Product Not Found.\n")
    
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