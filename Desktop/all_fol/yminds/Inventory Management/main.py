# main.py

from inventory import Inventory
import argparse


def main():
    inventory = Inventory()

    # Load inventory from file automatically
    inventory.load_inventory()

    parser = argparse.ArgumentParser(description="🧾 Inventory Management System")
    parser.add_argument("command", help="Command to run: add, update, view, search, save, load, version")

    parser.add_argument("--name", help="Item name")
    parser.add_argument("--quantity", type=int, help="Quantity of the item")
    parser.add_argument("--price", type=float, help="Price of the item")

    args = parser.parse_args()
    command = args.command.lower()

    if command == "add":
        if args.name and args.quantity is not None and args.price is not None:
            inventory.add_item(args.name, args.quantity, args.price)
            inventory.save_inventory()  # Save immediately
        else:
            print("❗ Error: Please provide --name, --quantity, and --price to add an item.")

    elif command == "update":
        if args.name:
            inventory.update_item(args.name, args.quantity, args.price)
            inventory.save_inventory()  # Save after update
        else:
            print("❗ Error: Please provide at least --name to update.")

    elif command == "view":
       content = inventory.view_inventory()
       print(content)

    elif command == "search":
        if args.name:
            items = inventory.search_item(args.name)
            print(items)
        else:
            print("❗ Error: Please provide --name to search.")

    elif command == "save":
        save = inventory.save_inventory()
        print(f'💾 Inventory saved. {save}')

    elif command == "load":
        load =  inventory.load_inventory()
        print(f'📂 Inventory loaded. {load}')


    else:
        print(f"❗ Unknown command: {command}")


if __name__ == "__main__":
    main()
