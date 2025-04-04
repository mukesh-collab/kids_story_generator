import json
import os
from dotenv import load_dotenv

load_dotenv()
INVENTORY_FILE = os.getenv("INVENTORY_FILE")

# Version info
__version__ = "1.0.0"


def show_version():
    print(f"📦 Inventory Management System Version: {__version__}")


class Inventory:
    def __init__(self):
        self.filename = INVENTORY_FILE
        self.items = {}

    def add_item(self, name, quantity, price):
        name = name.lower()
        if name in self.items:
            raise ValueError(f"Item '{name}' already exists.")
        self.items[name] = {"quantity": quantity, "price": price}

    def update_item(self, name, quantity=None, price=None):
        name = name.lower()
        if name not in self.items:
            raise KeyError(f"Item '{name}' not found.")
        if quantity is not None:
            self.items[name]["quantity"] = quantity
        if price is not None:
            self.items[name]["price"] = price

    def view_inventory(self):
        return self.items

    def search_item(self, name):
        return self.items.get(name.lower(), None)

    def save_inventory(self):
        try:
            with open(self.filename, "w") as f:
                json.dump(self.items, f, indent=4)
            return f"✅ Data saved to '{self.filename}'"
        except Exception as e:
            return f"❌ Failed to save inventory: {str(e)}"

    def load_inventory(self):
        if not os.path.exists(self.filename):
            return f"⚠️ No inventory file found at '{self.filename}'. Starting fresh."
        try:
            with open(self.filename, "r") as f:
                self.items = json.load(f)
            return f"✅ Data loaded from '{self.filename}'"
        except Exception as e:
            return f"❌ Failed to load inventory: {str(e)}"
