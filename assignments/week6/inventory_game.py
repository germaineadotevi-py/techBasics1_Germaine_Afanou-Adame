# --- Game State ---

import sys

# Global state
inventory = []
items_in_room = [
    {"name": "bread", "description": "A fresh piece of bread. It looks very nourishing and gives you vital energy."},
    {"name": "key", "description": "A heavy iron key. It looks like it fits the exit door perfectly."},
    {"name":"key", "descreiption": "if u pick up the key. ur also going to use"}
]

has_eaten_bread = False  # Stores whether the player has boosted their health


# --- Functions ---

def show_inventory():
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("--- Your Inventory ---")
        for item in inventory:
            print(f"- {item['name']}")


def show_room_items():
    if not items_in_room:
        print("The room is completely empty.")
    else:
        print("--- Items in the Room ---")
        for item in items_in_room:
            print(f"- {item['name']}")


def pick_up(item_name):
    # Search for the item in the room
    for item in items_in_room:
        if item["name"] == item_name:
            inventory.append(item)
            items_in_room.remove(item)
            print(f"You picked up: {item_name}")

            # Trigger event if the item was the key
            if item_name == "key":
                open_door_and_attack()
            return

    print(f"There is no '{item_name}' here.")


def use(item_name):
    global has_eaten_bread

    # Check if the item is in the inventory
    is_in_inventory = any(item["name"] == item_name for item in inventory)

    if not is_in_inventory:
        print(f"You don't have '{item_name}' in your inventory to use.")
        return

    if item_name == "bread":
        has_eaten_bread = True
        # Remove bread from inventory since it has been eaten
        inventory[:] = [item for item in inventory if item["name"] != "bread"]
        print("\n[HEALTH +100]")
        print("You eat the bread. You feel extremely strong and your health is fully restored!")
    else:
        print(f"You don't know how to use '{item_name}' here.")


def examine(item_name):
    # Search in inventory
    for item in inventory:
        if item["name"] == item_name:
            print(f"[Inventory] {item['name'].upper()}: {item['description']}")
            return
    # Search in room
    for item in items_in_room:
        if item["name"] == item_name:
            print(f"[Room] {item['name'].upper()}: {item['description']}")
            return

    print(f"You don't see any '{item_name}' here.")


def open_door_and_attack():
    print("\n--------------------------------------------------")
    print("You put the key into the lock... THE DOOR OPENS!")
    print("Suddenly, an evil creature jumps out of the shadows and attacks you instantly!")
    print("--------------------------------------------------\n")

    if has_eaten_bread:
        print("BAM! The attack hits you hard!")
        print("But because you ate the nourishing bread beforehand, you have enough health and survive!")
        print("\n🎉 CONGRATULATIONS! You managed to escape and won the game! 🎉")
    else:
        print("OH NO! The attack catches you completely off guard!")
        print("You don't have enough health points to withstand the blow...")
        print("\n💀 GAME OVER! You have been defeated. You should have eaten something first... 💀")

    sys.exit()


# --- Main Game Loop ---

def game_loop():
    print("====================================================")
    print("Welcome to the Escape Room!")
    print("Find a way out.")
    print("You look around and see the following items on a table:")
    print(" - bread")
    print(" - key")
    print("====================================================")
    print("Commands: inventory, look, pickup [item], use [item], examine [item], quit")

    while True:
        command_input = input("\n> ").strip().lower()
        parts = command_input.split(' ', 1)
        command = parts[0]
        argument = parts[1] if len(parts) > 1 else None

        match command:
            case "help":
                print("Commands: inventory, look, pickup [item], use [item], examine [item], quit")
            case "inventory":
                show_inventory()
            case "look":
                show_room_items()
            case "pickup":
                if argument:
                    pick_up(argument)
                else:
                    print("What do you want to pick up? (e.g., pickup bread)")
            case "use":
                if argument:
                    use(argument)
                else:
                    print("What do you want to use? (e.g., use bread)")
            case "examine":
                if argument:
                    examine(argument)
                else:
                    print("What do you want to examine? (e.g., examine key)")
            case "quit":
                print("Thanks for playing!")
                break
            case _:
                print("Unknown command. Type 'help' to see the list of commands.")


if __name__ == "__main__":
    game_loop()