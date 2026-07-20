'''
Author: Grace Tarihoran
Program name: Inventory Management System
'''

inventory = {}


def add_item():
    '''add item to inventory'''

    print("\nAdding a New Item")
    # validate input id
    while True:
        try:
            id = int(input("Enter item ID (unique integer): "))
            if id in inventory:
                print("Error: Item ID already exists. Try a different ID.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer for the item ID.")

    # validate input name
    while True:
        try:
            name = input("Enter item name: ").strip()
            if not name:
                print("Item name cannot be empty.")
                continue
            break
        except ValueError:
            print("Invalid input")

    # validate input quantity
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # validate input price
    while True:
        try:
            price = float(input("Enter price per unit: "))
            if price <= 0:
                print("Price must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number for the price.")

    # add item to inventory
    inventory[id] = {
        "name": name.strip(),
        "quantity": quantity,
        "price": price
    }

    print(f"Item '{name}' added successfully!\n")


def update_item():
    '''update existing item in inventory'''

    print("\nUpdating Item Details")

    # check if id is exist
    while True:
        try:
            id = int(input("Enter item ID to update: "))

            if id not in inventory:
                print("Error: Item not found.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer for the item ID.")

    # retrive inventory item details
    name = inventory[id]["name"]
    quantity = inventory[id]["quantity"]
    price = inventory[id]["price"]

    print("Enter new values (press Enter to keep existing values):")

    # update name
    new_name = input(f"Current Name: {name} | New Name: ").strip()
    if new_name == "":
        new_name = name

    # update quantity
    while True:
        try:
            new_quantity = input(f"Current Quantity: {quantity} | New Quantity: ")
            if new_quantity == "":
                new_quantity = quantity
                break

            new_quantity = int(new_quantity)
            if new_quantity <= 0:
                print("Quantity cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid input! Enter a valid integer for quantity.")

    # update price
    while True:
        try:
            new_price = input(f"Current Price: {price} | New Price: ")
            if new_price == "":
                new_price = price
                break

            new_price = float(new_price)
            if new_price <= 0:
                print("Price must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number for the price.")

    # update inventory item details
    inventory[id] = {
        "name": new_name.strip(),
        "quantity": new_quantity,
        "price": new_price
    }

    print("Item updated successfully!\n")


def remove_item():
    '''remove item from inventory'''

    # check if id is exist
    print("\nRemoving an Item")
    while True:
        try:
            id = int(input("Enter the ID of the item to remove: "))

            if id not in inventory:
                print("Error: Item not found.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer for the item ID.")

    # delete an item from inventory
    del inventory[id]
    print("Item removed successfully!\n")


def view_inventory():
    '''retrieve all inventory items'''

    total_value = 0
    print("\nCurrent Inventory:")

    if not inventory:
        print("No items in inventory.")
        return

    print("-" * 60)
    print(f"{'ID':<6}{'Name':<15}{'Quantity':>10}{'Price':>10}{'Total Value':>15}")
    print("-" * 60)

    for id, item in inventory.items():
        name = inventory[id]["name"]
        quantity = inventory[id]["quantity"]
        price = inventory[id]["price"]
        total_value = quantity * price

        print(f"{id:<6}{name:<15}{quantity:>10}{price:>10.2f}{total_value:>15.2f}")
    print("-" * 60)


def check_total_value():
    '''display total price in inventory'''

    total_value = 0
    for id, item in inventory.items():
        quantity = inventory[id]["quantity"]
        price = inventory[id]["price"]
        total_value += quantity * price

    print(f"\nTotal inventory value:  {total_value:.2f}")


def find_low_stock():
    '''set quantity threshold and list item under quantity threshold'''

    print("\nChecking for Low Stock Items")

    if not inventory:
        print("No items in inventory.")
        return

    # set threshold
    while True:
        try:
            threshold = int(input("Enter the low stock threshold: "))

            if threshold <= 0:
                print("Threshold must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer")

    found = False
    print("\nItems with Low Stock:")

    # check if quantity items less than determined threshold
    for id, item in inventory.items():
        if inventory[id]["quantity"] <= threshold:
            print(f"- Name: {item["name"]}, ID: {id}, Quantity: {item["quantity"]}")
            found = True

    if not found:
        print("No items with low stock.")


def main():
    'call and execute all functions'

    while True:
        print("\n==== Inventory Management System ====")
        print("1. Add a New Item to Inventory")
        print("2. Update Item Details")
        print("3. Remove an Item")
        print("4. View Inventory")
        print("5. Check Inventory Value")
        print("6. Find Items with Low Stock")
        print("7. Exit Program")

        choice = input("Choose an option(1-7): ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            view_inventory()
        elif choice == "5":
            check_total_value()
        elif choice == "6":
            find_low_stock()
        elif choice == "7":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")


# Run the program
if __name__ == "__main__":
    main()
