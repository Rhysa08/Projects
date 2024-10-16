
# Puzzle for forest
moss_covered_trees = 6  # Number of tall moss-covered trees
mud_pits = 3  # Number of mud pits
print("You notice an inscription beside the door of the shack:")
print("Unlock the secrets of the marsh:")
print(f"Count the number of tall moss-covered trees ({moss_covered_trees}) and multiply it by the number of bubbling mud pits ({mud_pits}).")
player_input = input("Enter your answer: ")
try:
    player_answer = int(player_input)
    
    if player_answer == moss_covered_trees * mud_pits:
        print("The shack door opens. You may enter.")
        
    else:
        print("Your answer is incorrect. The door remains locked.")
        
except ValueError:
    print("Invalid input. Please enter a number.")

print("You walk in through the shack door. You notice there is light and you see that there is writing on the wall.")
print("The writing on the wall says: ")
print("")

# Puzzle for mines
entrance_mines = {
    "name": "Mines entrance",

    "description": """You are standing at the entrance of the mines.
    You are faced with 3 paths leading into the distance.
    Which path do you take? """,

    "path": ""
}