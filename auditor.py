inventory = 0
failed_entries = 0

while True:
    if (inventory <= 500):
        stock_quantity = input("Enter Stock Quantity (Type 'quit' to quit): ")
        if stock_quantity.isdigit():
            if int(stock_quantity) < 0:
                print("Error: Please Enter a Positive Integer.")
                failed_entries += 1
            else:
                inventory += int(stock_quantity)
                print(int(stock_quantity), "stock recorded.")
        elif stock_quantity.lower() == "quit":
            print("Total Units Processed:", inventory)
            print("Number of Failed/Rejected Entries:", failed_entries)
            break
        else:
            print("Error: Please Enter a Positive Integer.")
            failed_entries += 1
    else:
        print("Inventory has Exceeded 500 Units!")
        break