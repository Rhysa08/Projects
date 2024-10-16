from items import *
from map import *
from game import type_text

# List of Items in player's inventory 
player_inventory = [item_torch]
player_weapon = [item_knife]

player = {
    "name": input("What is your adventurer's name?\n"),
    
    "health": 125,
    
    "milestone": 0
}
