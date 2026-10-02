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

def find_product(inventory, product_id):
    for product in inventory:
        if product["id"] == product_id:
            return product
    return None

def display_all(inventory):
    if len(inventory) == 0:
        print("Inventory is empty.")
        return
    print("Current Inventory")
    print("-" * 48)
    for p in inventory:
        print(f"ID: {p['id']} | Name: {p['name']} | Price: ${p['price']:.2f} | Stock: {p['stock']}")
    print("-" * 48)

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
