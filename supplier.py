class Supplier():
    def __init__(self, supplier_id: str, supplier_name: str, contact_email: str):
        self.__supplier_id = supplier_id
        self.__supplier_name = supplier_name
        self.__contact_email = contact_email
        
    def display_information(self) -> None:
        print(f"Supplier ID: {self.__supplier_id}")
        print(f"Supplier Name: {self.__supplier_name}")
        print(f"Contact Email: {self.__contact_email}")