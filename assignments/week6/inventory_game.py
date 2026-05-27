# --- Game State ---

inventory = []
items_in_room = [
    {"name": "Torch", "type": "tool", "description": "Lights up dark places."},
    {"name": "Apple", "type": "food", "description": "Restores a small amount of health."},
    {"name": "Key", "type": "tool", "description": "Opens a locked door."}
] # length shall be larger than max inventory size if there is only one room
MAX_INVENTORY_SIZE = 5

# --- Functions ---

def show_inventory():
    # list all names of items in the inventory, consider the case when the list is empty
    pass

def show_room_items():
    # list all items in current room
    pass

def pick_up(item_name):
    # pick up an item from the room if inventory limit is not met yet
    pass

def drop(item_name):
    # drop an item from your inventory, at the same time append it back to the list of items for the room
    pass

def use(item_name):
    # Ex: use the item differently depends on the type
    pass

def examine(item_name):
    # you can only examine an item if it's in your inventory or if it is in the room
    pass

# --- Game Loop ---

def game_loop():
    print("Welcome to the Inventory Game!")
    print("Type 'help' for a list of commands.")

    while True:
        command = input("\n> ").strip().lower()

        # As an example, here I used the match/case syntax to replace long if/else statements
        # This feature is only supported from Python 3.10 and above

        match command.split():
            case ["help"]:
                print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], quit")
            case ["inventory"]:
                show_inventory()
            case ["look"]:
                show_room_items()
            case ["pickup", item_name]:
                pick_up(item_name)
            case ["drop", item_name]:
                drop(item_name)
            case ["use", item_name]:
                use(item_name)
            case ["examine", item_name]:
                examine(item_name)
            case ["quit"]:
                print("Thanks for playing!")
                break
            case _: # else
                print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    game_loop()
