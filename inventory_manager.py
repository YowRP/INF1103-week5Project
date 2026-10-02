import json
import os

INVENTORY_FILE = "inventory.json"


def load_inventory():
    if os.path.exists(INVENTORY_FILE):
        print("inventory.json found.")
        with open(INVENTORY_FILE, "r", encoding="utf-8") as f:
            inventory = json.load(f)
        print("Inventory loaded successfully.")
        return inventory
    print("inventory.json not found. Starting with an empty inventory.")
    return []

def save_inventory(inventory):
    with open(INVENTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(inventory, f, indent=4)


def add_product(inventory):
    print("Add new product")
    product_id = input("Enter product ID: ").strip()
    for i in inventory:
        if i["id"] == product_id:
            print("Product ID already exists.")
            return

    name = input("Enter product name: ").strip()

    try:
        price = float(input("Enter product price: ").strip())
        stock = int(input("Enter stock quantity: ").strip())
    except ValueError:
        print("Invalid input. Product not added.")
        return

    product = {"id": product_id, "name": name, "price": price, "stock": stock}
    inventory.append(product)
    print("Product added successfully.")

def find_inventory(inventory):
    #find product by ID and also update_stock

    find_product_id = input("Enter product ID: ").strip()
    for product in inventory:
        if product["id"] == find_product_id:
            print(f"Product found: ID: {product['id']}, Name: {product['name']}, Quantity: {product['quantity']}, Price: {product['price']}")
            return product

        else: 
            print("Product not found.")
            choice = input("Do you want to add this product? (y/n): ").strip().lower()
            if choice == "y":
                add_product(inventory)

    

def display_all(inventory):
    for i in inventory:
        print(f"ID: {i['id']}, Name: {i['name']}, Quantity: {i['quantity']}, Price: {i['price']}")

        if inventory == []:
            print("Inventory is empty.")
            return choice == "1"

def main():
    """Run the order tracking program."""
    print ("="*40)
    print ("INVENTORY MANAGEMENT SYSTEM")

    inventory = load_inventory()
    display_all(inventory)

    while True:
        print("----------- MENU -----------")
        # print options 1-6
        choice = input("Enter option: ").strip()
        if choice == "1": ...
        elif choice == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print ("THANK YOU FOR USING THE INVENTORY MANAGEMENT SYSTEM!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
