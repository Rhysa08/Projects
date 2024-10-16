# Import necessary python libs
import time
import sys
from os import system, name

# Import all (*) variables from other .py files
from map import *
from player import *
from items import *
from enemies import *
from npcs import *
from gameparser import *
from combat import *

map_from_file = map_from_file = open('mapa.txt', 'r')
delay = 0.5


# Function to enter cabin
def enter_cabin(enter):
    global player_current_room
    if enter.lower() == "no":
        pass
    elif enter == "-7":
        player_current_room = rooms["Inside Cabin"]
        type_text(player_current_room, delay)
    elif enter != "-7":
        print("You grab the door and it lights and heats up, repelling you away from the seemingly magical cabin.\n")
    return


# Function to enter shack
def enter_shack(enter):
    global player_current_room
    if enter.lower() == "no":
        return
    elif enter == "yes":
        player_current_room = rooms["Inside Shack"]
    else:
        return "That is not a valid input"


# Takes in text and prints it as if typed
def type_text(text, delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()

    print()


# Prompts the user to enter to return from an informatic screen
def finishedreading():
    finished_reading = input('Press ENTER to clear the screen once you have finished reading...')
    while finished_reading != '':
        finished_reading = input('Press ENTER to clear the screen once you have finished reading...')
    return True


# Used to clear the screen inbetween rooms for readability
def clear_screen():
    time.sleep(0.5)
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# Prints the menu of choices to the player
def print_menu():
    type_text("You can:", delay)
    # Prints the directions the player can move

    for exit in player_current_room["exits"]:
        print_string = "GO " + exit.upper() + " to " + exit_leads_to(player_current_room["exits"], exit).upper()
        type_text(print_string, delay)
    # Prints the items the player can look at

    for item in player_current_room["items"]:
        print_string = "LOOK at " + item["id"].upper()
        type_text(print_string, delay)

        # Prints the npcs the player can talk to
    for npc in player_current_room["npcs"]:
        print_string = "TALK to " + npc["id"].upper()
        type_text(print_string, delay)

        # Prints the surroundings the player can examine
    for surroundings in player_current_room["surroundings"]:
        print_string = "EXAMINE " + surroundings["id"].upper()
        type_text(print_string, delay)

    # Prints the options for the players inventory items
    for item in player_inventory:
        print_string = "INSPECT your " + item["id"].upper()
        type_text(print_string, delay)

    if player_current_room == rooms["Cabin Outside"]:
        print("OPEN DOOR?")

    if player_current_room == rooms["Outside Shack"]:
        print("OPEN DOOR?")


# USED BY PRINT_MENU
# Takes in a dictionary of exits and a direction and returns the room it leads to
def exit_leads_to(exits, direction):
    return exits[direction]


# Takes in a list of dictionaries and an identifier and returns the identifiers in the dicts as a string
def get_list_as_string(list, identifier):
    list_string = ""
    for item in list:
        list_string += item[identifier] + ", "
    list_string = list_string.strip(', ')
    return list_string


# Prints the room description and contents of the room
def print_room_info():
    print(player_current_room["display_name"])
    print()
    # Prints the room description
    type_text(player_current_room["description"], delay)
    print()

    # Prints the player's inventory / prints they have nothing
    if (player_inventory):
        print_string = "You are carrying: " + get_list_as_string(player_inventory, "name") + "."
        type_text(print_string, delay)
        print()
    else:
        type_text("There is nothing in your inventory", delay)
        print()

    # Prints the items in the current room
    if (player_current_room["items"]):
        print_string = "There is " + get_list_as_string(player_current_room["items"], "name") + " here."
        type_text(print_string, delay)
        print()

    # Prints the npcs in the current room
    if (player_current_room["npcs"]):
        print_string = "You can see the " + get_list_as_string(player_current_room["npcs"], "id")
        type_text(print_string, delay)
        print()


# Moves the player if the given direction is valid
def move_player(direction):
    global player_current_room
    if (direction in player_current_room["exits"]):
        target_room = exit_leads_to(player_current_room["exits"], direction)
        player_current_room = rooms[target_room]
    else:
        print()
        type_text("That isn't a valid direction!", delay)


# Prints the description of the item if given a valid item and prompts the player to take the item
def look_at_item(item):
    for current_item in player_current_room["items"]:
        if current_item["id"].lower() == item.lower():
            print_look_text("take", current_item)
            user_choice = normalise_input(input("Enter either 'Yes' or 'No': "))
            if (user_choice[0] == "yes"):
                player_inventory.append(current_item)
                player_current_room["items"].remove(current_item)
                print()
                taken_item_text = "You took the " + item + "."
                type_text(taken_item_text, delay)
    clear_screen()


# Prints item description and prompts take/drop question
def print_look_text(command, item):
    see_text = "You see " + item["description"]
    type_text(see_text, delay)
    command_text = "Would you like to " + command + " the " + item["id"] + "?"
    type_text(command_text, delay)


# Prints the description of the item if given a valid item and prompts the player to drop the item
def inspect_item(item):
    for current_item in player_inventory:
        if current_item["id"] == item:
            print_look_text("drop", current_item)
            user_choice = normalise_input(input("Enter either 'Yes' or 'No': "))
            if (user_choice[0] == "yes"):
                player_inventory.remove(current_item)
                player_current_room["items"].append(current_item)
                print()
                taken_item_text = "You dropped the " + item + "."
                type_text(taken_item_text, delay)
    clear_screen()


def examine_area(thing):
    for surroundings in player_current_room["surroundings"]:
        if surroundings["id"].lower() == thing.lower():
            type_text(surroundings["description"], delay)

    clear_screen()


def talk_to_npc(npc):
    for current_npc in player_current_room["npcs"]:
        if current_npc["id"].lower() == npc:
            type_text(current_npc["description"], delay)
            print()
            if current_npc["interacted_with"]:
                type_text(current_npc["repeat_dialogue"], delay)
                if finishedreading():
                    clear_screen()
                    return
            elif npc == npc_mines_dargrim[
                "id"].lower() and item_broken_key_part_2 in player_inventory and item_broken_key_part_1 in player_inventory:
                type_text(
                    "You found a key? What terrible shape it's in. Let me fix it and give it to you in full form!",
                    delay)
                player_inventory.remove(item_broken_key_part_1)
                player_inventory.remove(item_broken_key_part_2)
                player_inventory.append(item_key)
                if finishedreading():
                    clear_screen()
                    return
            elif npc == npc_miner_oldman["id"].lower() and item_gold_nugget in player_inventory:
                type_text("""Gold? Gold! It's a game-changer! Luck? Who needs luck with this?
            (He cackles manically and dances around with the nugget, eyes wide with crazed excitement).
Reward?! Hmm, i do suppose you deserve one. I give you a trinket! (A long-forgotten weapon has been added to your
usable weapons!)""", delay)
                player_inventory.remove(item_gold_nugget)
                player_weapon.append(item_sword)
                player["health"] += 50
                player["milestone"] += 1
                return
            else:
                type_text(current_npc["quest_dialogue"], delay)
                current_npc["interacted_with"] = True
                if finishedreading():
                    clear_screen()
                    return
        return type_text("\033[4m" + "Talk to whom? You must input a valid character!" + "\033[0m \n", delay)


def use_item(user_input):
    for item in player_inventory:
        if user_input.lower() == item["id"].lower():
            if user_input and player_current_room == rooms["Cove"]:
                type_text(
                    "You strike the torch afire and you read on the ceiling: 'S̸̡̘͕̳̤̗͕̍̿͐Ḫ̶͕̱͙̜̏̅Ạ̸̳͓͋͝Ḍ̸̨͖͇̖̦̎̉͘ͅO̵̠͎̱̞̬͑͊͗̈́͒̚͝W̴̛̱̬̥͎̗̿͆̇̄̅͒S̷̢̭̯͘'\n",
                    delay)

            elif user_input.lower() == "torch" and player_current_room == rooms["Dark Corner"]:
                type_text("""You torch alights in flame. Touching your surroundings with a fiery glow, You can see
                through the darkness.""", delay)
                room_mines_shaft_upper_dark["surroundings"] = [upper_mines_rock]
            elif user_input.lower() == "torch" and player_current_room == rooms["Cave"]:
                type_text("""The moist walls glisten in the light produced by your torch. You notice a strange object
                on the ground.""", delay)
                room_mines_miner_cave["items"] = [item_broken_key_part_2]
            elif user_input.lower() == "key" and player_current_room == rooms[
                "Dark Corner"] and item_key in player_inventory:
                type_text("""You plant the key inside of the rock and twist it. The rock cracks in perfect symmetry. A large
                      golden nugget is unveiled as the shell around it falls to the ground.""", delay)
                room_mines_shaft_upper_dark["items"] = [item_gold_nugget]
                player_inventory.remove(item_key)
                room_mines_shaft_upper_dark["surroundings"] = []
            elif user_input.lower() == "ladder" and player_current_room == rooms["Shaft"]:
                type_text("You place the ladder to the bridge above.", delay)
                room_mines_shaft["exits"] = {"west": "Mines", "north": "Upper Mines"}

    return


# Prints map.txt if the user has the map in their inventory
def read_map():
    if not item_map in player_inventory:
        type_text("You do not have a map!", delay)
        print()
        return
    for line in map_from_file:
        print(line)
    if finishedreading():
        clear_screen()
    return


def speak():
    global room_lake_island
    speech = input("What would you like to say?\n")
    if speech.lower() == "whispering shadows beckon" and player_current_room == rooms["Lake"]:
        room_lake["exits"] = {"west": "Village", "south": "Shoreline", "north": "Lily Pads", "east": "Island"}
        print()
        type_text("""At the moment you said those words, a voice enters your mind:
T̸h̶e̸ ̸p̵a̷t̷h̵ ̷h̶a̸s̶ ̷o̵p̴e̶n̷e̴d̴,̵ ̶I̶ ̸a̸w̴a̷i̷t̴ ̸y̸o̷u̴r̸ ̷a̶r̴r̷i̸v̸a̷l̶.
A moss-covered stone bridge rises from the lake, providing a path towards the island. 
Although you do not know what awaits you there.\n""", delay)
        player["health"] += 50
        player["milestone"] += 1


def print_functions():
    type_text("""List of functions:
'GO'
'LOOK'
'TALK'
'INSPECT'
'EXAMINE'
'OPEN'
'USE'
'SPEAK'
'HELP'
'READ'
'TOGGLE'

    
    """, delay)


# Used to take in the user's choice and then calls the correct action function

def get_user_choice():
    global delay
    type_text("What would you like to do?: ", delay)
    user_input = input()
    if user_input == "":
        return type_text("You must put in a command! Use HELP if you want to see a list of commands!", delay)
    user_choice = normalise_input(user_input)
    clear_screen()

    if (user_choice[0] == "go"):
        if (len(user_choice) == 1):
            type_text("Go where? You must input a direction!", delay)
            print()
            return
        move_player(user_choice[1])
        return
    else:
        pass
    if (user_choice[0] == "look"):
        if (len(user_choice) == 1):
            type_text("Look at what? You must input an item!", delay)
            print()
            return
        look_at_item(user_choice[1])
        return

    if (user_choice[0] == "talk"):
        if (len(user_choice) == 1):
            type_text("Talk to whom? You must input a character!", delay)
            print()
            return
        # NPC CODE
        talk_to_npc(user_choice[1])
        return

    if (user_choice[0] == "inspect"):
        if (len(user_choice) == 1):
            type_text("Inspect what? You must input an item!", delay)
            print()
            return
        inspect_item(user_choice[1])

    if (user_choice[0] == "examine"):
        if (len(user_choice) == 1):
            type_text("Examine what? You must input something to do with the area!", delay)
            print()
            return
        examine_area(user_choice[1])
        return

    if (user_choice[0] == "open"):
        if (len(user_choice) == 1):
            type_text("Open what? There must be something to open!", delay)
            print()
            return
        if user_choice[1] == "door" and player_current_room == rooms["Cabin Outside"]:
            enter_cabin(input("Do You want to open the door? Yes or No?"))
            return
        elif user_choice[1] == "door" and player_current_room == rooms["Outside Shack"]:
            enter_shack(input("Are you sure you want to open the door? Yes or No?"))
    if (user_choice[0] == "use"):
        if (len(user_choice) == 1):
            type_text("Use what? You must input an item in your inventory!", delay)
            print()
            return
        use_item(user_choice[1])
        return
    if (user_choice[0] == "speak"):
        speak()
        return

    if (user_choice[0] == "help"):
        print_functions()
        return

    if (user_choice[0] == "read"):
        if (len(user_choice) == 1):
            type_text("\033[4m" + "Read what? Did you mean to READ MAP?" + "\033[0m", delay)
            print()
            return
        if (user_choice[1] == 'map'):
            read_map()
        return

    if (user_choice[0] == "toggle"):
        if delay == 0.05:
            delay = 0
            type_text("Text will no longer scroll.", delay)
            clear_screen()
            return
        if delay == 0:
            delay = 0.05
            type_text("Text will now scroll", delay)
            clear_screen()
            return
    else:
        print()
        type_text("That is not a valid choice!", delay)


# Function for main game loop
def main():
    global player_current_room
    global player_unselected_weapon
    # Clear screen before first room
    clear_screen()

    while True:

        if player_current_room["enemy"] == enemy_dragon:
            print("Do you wish to fight the dragon? Yes or No?")
            yesno = input("")
            print(normalise_input(yesno))
            if yesno.lower() == "yes":
                combat_loop("Aurum", 300, 45, """At the heart of the opulent chamber, a colossal vault bursts with unimaginable riches,
its glittering contents piled so high that it seems wealth might cascade over the edges at any
moment. But before this treasure trove stands a suspiciously large sum of gold,
forming a glistening barrier, tempting the uninvited to reach out and claim their fortune.
As you inch closer to the precious metal, a crystalline eye opens with a piercing gaze, 
the gold suddenly takes on a draconian shape,
its molten form reshaping into a magnificent dragon with scales of resplendent gold and gemstone
eyes that blaze with an otherworldly intelligence.
The guardian of wealth gazes down upon the player character with regal pride, a testament to the
treasure's fierce protector.""")
                continue
            if yesno.lower() == "no":
                player_current_room = rooms["Village"]
            elif yesno.lower() == "refuse":
                game_ending("Eye-opener")


        if player_current_room["enemy"] != []:  # Checks to see if there are any enemies in the room.
            e = player_current_room["enemy"]  # Enemy dictionary
            eh = e["health"]  # Enemy Health
            eh = int(eh)
            en = e["name"]  # Enemy name
            ed = e["damage"]  # Enemy damage
            ed = int(ed)
            edesc = e["description"]
            combat_loop(en, int(eh), ed, edesc)
            print(f"Congratulations! You defeated the {en}!")
            player["health"] += 50
            player["milestone"] += 1
            player_current_room["enemy"] = []
            player_unselected_weapon = True
        else:
            pass

        print_room_info()

        print_menu()

        get_user_choice()


# KEEP AS FOOTER
# Prevents an error when initializing game.py
if __name__ == "__main__":
    main()
