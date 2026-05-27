### Assignment 6
The goal of this week is to build a small game based with an inventory management system to practice dictionary/list. 
You're a character exploring a (text-based) world, along the way, you can:
- pick up and drop items
- use or examine them
- deal with inventory limits

Core features
1. Inventory System
  - A list holds your items: `inventory = []`
  - Each item is a dictionary: `{"name": "medicine", "type": "healing", "uses": 1}`
  - Inventory Limit: max of 5 items
2. Room System
  - A list of dictionary represents items in the current area: 
```
items_in_room = [
    {"name": "Key", "type": "tool"},
    {"name": "Apple", "type": "food"}
]
```
3. Actions 
  - Use functions to define the following basic actions:
```
def show_room_items(): ...
def pick_up(item_name): ...
def drop(item_name): ...
def use(item_name): ...
def show_inventory(): ...
def examine(item_name): ...
```
4. User Interactions
  - Users shall be able to navigate the game by typing commands in following ways
```
inventory
pickup apple
drop torch
use potion
examine sword
help
```
5. Define a meaningful scenario (goal and ending) for your little game. It could be a classic escape game, survival on an island, buying food in a supermarket...

** You can also integrate the system to what you have already built. Though that probably means more work on your side. If you are adding things on top of very long code, please clearly mark the sections where new changes are introduced for this week
