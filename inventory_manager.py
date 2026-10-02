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
    user_input = ("Enter ID number: ")


def main():
    """Run the order tracking program."""
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
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()