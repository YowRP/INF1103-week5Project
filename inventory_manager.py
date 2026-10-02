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