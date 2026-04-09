# You are building a grocery shopping assistant that runs in the terminal.
# The program keeps a shopping list in memory and lets the user interact with it through a simple numbered menu.
# Requirements:
# - Each item has a name and a checked status (bought or not).
# - The user can add a new item by typing its name.
# - The user can remove an item by its name.
# - The view list option displays all items, marking checked ones with [x] and unchecked ones with [ ].
# - The user can toggle an item between checked and unchecked.
# - The clear option removes all items from the list after asking for confirmation (Are you sure? y/n).
# If the user tries to remove or check an item that doesn't exist, print a friendly error message instead of crashing.
# The menu can look like this for exemple :
# === Shopping List Manager ===
# 1.  Add item
# 2.  Remove item
# 3.  View list
# 4.  Check / Uncheck item
# 5.  Clear list
# 6.  Quit

class Item:
    def __init__(self, name):
        self.name = name
        self.checked = False

    def toggle(self):
        self.checked = not self.checked
    
    def __str__(self):
        check_status = "[x]" if self.checked else "[ ]"
        return f"{check_status} {self.name}"
    
class ShoppingList: 
    def __init__(self):
        self.items = []
    
    def add_item(self, name):
        self.items.append(Item(name))
    
    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(self.item)
                print(f"Item {name} successfully removed.")
                return
        print(f"Item {name} not in the shopping list.")

    def view_list(self):
        if bool(self.items):
            print("=== Shopping Llist ===")
            [print(str(item)) for item in self.items]
        else:
            print("The shopping list is empty.")

    def toggle_item(self, name):
        for item in self.items:
            if item.name == name:
                item.toggle()
                print(f'Item {name} successfully toggled.')
                return
        print(f"Item {name} not in the shopping list.")
    
    def clear_list(self):
        confirm = input("Do you want to clear the shopping list? (y/n)")
        if confirm.lower() == 'y':
            self.items.clear()
            print(("Shopping list has been cleared."))
        else:
            print("Clear cancelled.")
    
    # def main():
        