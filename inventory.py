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
    
class Inventory:
    def __init__(self):
        self.__product_list = [] # Stores Product Objects in this List
    
    # Adds Product to Product List
    def add_product(self, product_id: str, product_name: str, price: float, stock_quantity: int):
        product_object = Product(product_id, product_name, price, stock_quantity)
        self.__product_list.append(product_object)
        print(f"{product_name} added to Inventory.")
    # def add_product(self):
    #     try:
    #         print("ADD NEW PRODUCT")
    #         product_id = input("Enter Product ID: ")
    #         product_name = input("Enter Product Name: ")
            
    #         # Check if Product ID or Product Name is Empty
    #         if not product_id.strip():
    #             raise ValueError("Error: Product ID cannot be Empty.")
    #         if not product_name.strip():
    #             raise ValueError("Error: Product Name cannot be Empty.")
            
    #         product_price = float(input("Enter Product Price: "))    
    #         stock_quantity = int(input("Enter Stock Quantity: "))
    #         if product_price < 0 or stock_quantity < 0: raise ValueError # Raise Error if Product Price or Stock Quantity is Negative
    #         product_obj = Product(product_id, product_name, product_price, stock_quantity)
    #         self.__product_list.append(product_obj)
            
    #         print("Product Added Successfully.")
    #     except ValueError as v:
    #         if "Empty" in str(v): # Error caused by Product ID or Product Name
    #             print(v)
    #         else: # Error caused by Product Price and Stock Quantity
    #             print("Error: Please enter a Non-Negative Number for Product Price and Stock Quantity.")
    #     except Exception as e:
    #         print(f"Error: {e}")
    
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
        
    
    
class Menu():
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
            print(f"Error: {e}")
            