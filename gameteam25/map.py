from items import *
from enemies import *
from npcs import *
from surroundings import *

room_village = {
    # The name of the room that the player will see
    "name": "The Village",
    # The description of the room that the player will see
    "description":
        """You find yourself in the heart of a village.
The villagers go about their day, giving you curious glances as they walk past.""",
    # A Dictionary with Directions and Room ID as it's keys and values
    "exits": {"north": "Dragon", "west": "Woods", "east": "Lake", "south": "Mines"},
    # A list with items in the room
    "items": [item_handbook, item_map],
    # A list with Npcs in the room
    "npcs": [npc_village_mayor],
    # A list with the Enemies in the room
    "surroundings": [mayor],

    "display_name": """▄▄▄█████▓ ██░ ██ ▓█████     ██▒   █▓ ██▓ ██▓     ██▓    ▄▄▄        ▄████ ▓█████ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓██░   █▒▓██▒▓██▒    ▓██▒   ▒████▄     ██▒ ▀█▒▓█   ▀ 
▒ ▓██░ ▒░▒██▀▀██░▒███       ▓██  █▒░▒██▒▒██░    ▒██░   ▒██  ▀█▄  ▒██░▄▄▄░▒███   
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄      ▒██ █░░░██░▒██░    ▒██░   ░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄ 
  ▒██▒ ░ ░▓█▒░██▓░▒████▒      ▒▀█░  ░██░░██████▒░██████▒▓█   ▓██▒░▒▓███▀▒░▒████▒
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░      ░ ▐░  ░▓  ░ ▒░▓  ░░ ▒░▓  ░▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░
    ░     ▒ ░▒░ ░ ░ ░  ░      ░ ░░   ▒ ░░ ░ ▒  ░░ ░ ▒  ░ ▒   ▒▒ ░  ░   ░  ░ ░  ░
  ░       ░  ░░ ░   ░           ░░   ▒ ░  ░ ░     ░ ░    ░   ▒   ░ ░   ░    ░   
          ░  ░  ░   ░  ░         ░   ░      ░  ░    ░  ░     ░  ░      ░    ░  ░
                                ░                                               """,
    "enemy": []

}

room_dragon = {
    "name": "Dragon's Lair",

    "description":
        """You stand before a massive dragon.
It observes you with a mix of curiosity and disdain.""",

    "exits": {"south": "Village"},

    "items": [],

    "npcs": [],

    "surroundings": [],

    "display_name": """▓█████▄  ██▀███   ▄▄▄        ▄████  ▒█████   ███▄    █   ██████     ██▓    ▄▄▄       ██▓ ██▀███  
▒██▀ ██▌▓██ ▒ ██▒▒████▄     ██▒ ▀█▒▒██▒  ██▒ ██ ▀█   █ ▒██    ▒    ▓██▒   ▒████▄    ▓██▒▓██ ▒ ██▒
░██   █▌▓██ ░▄█ ▒▒██  ▀█▄  ▒██░▄▄▄░▒██░  ██▒▓██  ▀█ ██▒░ ▓██▄      ▒██░   ▒██  ▀█▄  ▒██▒▓██ ░▄█ ▒
░▓█▄   ▌▒██▀▀█▄  ░██▄▄▄▄██ ░▓█  ██▓▒██   ██░▓██▒  ▐▌██▒  ▒   ██▒   ▒██░   ░██▄▄▄▄██ ░██░▒██▀▀█▄  
░▒████▓ ░██▓ ▒██▒ ▓█   ▓██▒░▒▓███▀▒░ ████▓▒░▒██░   ▓██░▒██████▒▒   ░██████▒▓█   ▓██▒░██░░██▓ ▒██▒
 ▒▒▓  ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ░▒   ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░   ░ ▒░▓  ░▒▒   ▓▒█░░▓  ░ ▒▓ ░▒▓░
 ░ ▒  ▒   ░▒ ░ ▒░  ▒   ▒▒ ░  ░   ░   ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░▒  ░ ░   ░ ░ ▒  ░ ▒   ▒▒ ░ ▒ ░  ░▒ ░ ▒░
 ░ ░  ░   ░░   ░   ░   ▒   ░ ░   ░ ░ ░ ░ ▒     ░   ░ ░ ░  ░  ░       ░ ░    ░   ▒    ▒ ░  ░░   ░ 
   ░       ░           ░  ░      ░     ░ ░           ░       ░         ░  ░     ░  ░ ░     ░     
 ░   

    """,
    "enemy": enemy_dragon
}

room_woods = {
    "name": "The Woods: Centre",

    "description":
        """The woods are thick, with tall trees forming a canopy overhead.
Birds chirp and the occasional rustle suggests you're not alone here.
""",

    "exits": {"east": "Village", "north": "Marsh", "west": "Clearing", "south": "Outlook"},

    "items": [],

    "npcs": [npc_woods_thornshadow],

    "surroundings": [],

    "display_name": """▄▄▄█████▓ ██░ ██ ▓█████     █     █░ ▒█████   ▒█████  ▓█████▄   ██████ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓█░ █ ░█░▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌▒██    ▒ 
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒█░ █ ░█ ▒██░  ██▒▒██░  ██▒░██   █▌░ ▓██▄   
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ░█░ █ ░█ ▒██   ██░▒██   ██░░▓█▄   ▌  ▒   ██▒
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░░██▒██▓ ░ ████▓▒░░ ████▓▒░░▒████▓ ▒██████▒▒
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░
    ░     ▒ ░▒░ ░ ░ ░  ░     ▒ ░ ░    ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒ ░ ░▒  ░ ░
  ░       ░  ░░ ░   ░        ░   ░  ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░ ░  ░  ░  
          ░  ░  ░   ░  ░       ░        ░ ░      ░ ░     ░          ░  
                                                       ░               """,
    "enemy": []

}

room_woods_marsh = {
    "name": "The Woods: Marsh",

    "description": """As you enter the marshy woodland, you see the idyllic scenery turn into a harsh land.
Bubbling mud pits, mist and tall moss-covered trees surround yourself as you trod through the wetland.
However, in front seems to be a shack untouched by the area.""",

    "exits": {"south": "Woods", "north": "Cabin Outside"},

    "items": [],

    "npcs": [],

    "surroundings": [marsh_trees, marsh_cabin, marsh_mudboils],

    "display_name": """▄▄▄█████▓ ██░ ██ ▓█████     ███▄ ▄███▓ ▄▄▄       ██▀███    ██████  ██░ ██ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓██▒▀█▀ ██▒▒████▄    ▓██ ▒ ██▒▒██    ▒ ▓██░ ██▒
▒ ▓██░ ▒░▒██▀▀██░▒███      ▓██    ▓██░▒██  ▀█▄  ▓██ ░▄█ ▒░ ▓██▄   ▒██▀▀██░
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒██    ▒██ ░██▄▄▄▄██ ▒██▀▀█▄    ▒   ██▒░▓█ ░██ 
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ▒██▒   ░██▒ ▓█   ▓██▒░██▓ ▒██▒▒██████▒▒░▓█▒░██▓
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒
    ░     ▒ ░▒░ ░ ░ ░  ░   ░  ░      ░  ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒  ░ ░ ▒ ░▒░ ░
  ░       ░  ░░ ░   ░      ░      ░     ░   ▒     ░░   ░ ░  ░  ░   ░  ░░ ░
          ░  ░  ░   ░  ░          ░         ░  ░   ░           ░   ░  ░  ░
                                                                          """,
    "enemy": []

}

room_woods_marsh_outside_cabin = {

    "name": "The Woods: Cabin's Garden",

    "description": "The cabin is untouched by the marsh, the welcoming warmth invites you inside.",

    "exits": {"south": "Marsh"},

    "items": [],

    "npcs": [],

    "surroundings": [cabin_door],

    "display_name": """▄▄▄█████▓ ██░ ██ ▓█████     ▄████▄   ▄▄▄       ▄▄▄▄    ██▓ ███▄    █      ▄████  ▄▄▄       ██▀███  ▓█████▄ ▓█████  ███▄    █ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▒██▀ ▀█  ▒████▄    ▓█████▄ ▓██▒ ██ ▀█   █     ██▒ ▀█▒▒████▄    ▓██ ▒ ██▒▒██▀ ██▌▓█   ▀  ██ ▀█   █ 
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒▓█    ▄ ▒██  ▀█▄  ▒██▒ ▄██▒██▒▓██  ▀█ ██▒   ▒██░▄▄▄░▒██  ▀█▄  ▓██ ░▄█ ▒░██   █▌▒███   ▓██  ▀█ ██▒
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░█▀  ░██░▓██▒  ▐▌██▒   ░▓█  ██▓░██▄▄▄▄██ ▒██▀▀█▄  ░▓█▄   ▌▒▓█  ▄ ▓██▒  ▐▌██▒
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ▒ ▓███▀ ░ ▓█   ▓██▒░▓█  ▀█▓░██░▒██░   ▓██░   ░▒▓███▀▒ ▓█   ▓██▒░██▓ ▒██▒░▒████▓ ░▒████▒▒██░   ▓██░
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░ ░▒ ▒  ░ ▒▒   ▓▒█░░▒▓███▀▒░▓  ░ ▒░   ▒ ▒     ░▒   ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒▓  ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
    ░     ▒ ░▒░ ░ ░ ░  ░     ░  ▒     ▒   ▒▒ ░▒░▒   ░  ▒ ░░ ░░   ░ ▒░     ░   ░   ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ▒  ▒  ░ ░  ░░ ░░   ░ ▒░
  ░       ░  ░░ ░   ░      ░          ░   ▒    ░    ░  ▒ ░   ░   ░ ░    ░ ░   ░   ░   ▒     ░░   ░  ░ ░  ░    ░      ░   ░ ░ 
          ░  ░  ░   ░  ░   ░ ░            ░  ░ ░       ░           ░          ░       ░  ░   ░        ░       ░  ░         ░ 

""",
    "enemy": []

}

room_woods_marsh_inside_cabin = {

    "name": "The Woods: Cabin",

    "description": """Although the exterior is well-protected and seems perfectly peaceful; the cabin is
in a terrible state. The interior walls have scratch marks and the decor is torn-up.
Whatever happened here, it was not meant to harm anyone or thing since there is no signs of blood.""",

    "exits": {"south": "Cabin Outside"},

    "npcs": [],

    "items": [item_broken_key_part_1],

    "surroundings": [cabin_curtains],

    "display_name": """▄▄▄█████▓ ██░ ██ ▓█████     ▄████▄   ▄▄▄       ▄▄▄▄    ██▓ ███▄    █ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▒██▀ ▀█  ▒████▄    ▓█████▄ ▓██▒ ██ ▀█   █ 
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒▓█    ▄ ▒██  ▀█▄  ▒██▒ ▄██▒██▒▓██  ▀█ ██▒
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░█▀  ░██░▓██▒  ▐▌██▒
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ▒ ▓███▀ ░ ▓█   ▓██▒░▓█  ▀█▓░██░▒██░   ▓██░
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░ ░▒ ▒  ░ ▒▒   ▓▒█░░▒▓███▀▒░▓  ░ ▒░   ▒ ▒ 
    ░     ▒ ░▒░ ░ ░ ░  ░     ░  ▒     ▒   ▒▒ ░▒░▒   ░  ▒ ░░ ░░   ░ ▒░
  ░       ░  ░░ ░   ░      ░          ░   ▒    ░    ░  ▒ ░   ░   ░ ░ 
          ░  ░  ░   ░  ░   ░ ░            ░  ░ ░       ░           ░ 
                           ░                        ░                """,
    "enemy": []

}

room_woods_outlook = {
    "name": "The Woods: Outlook",

    "description": """The path becomes indiscernible from grass and dirt as you venture further. The forest opens up
ahead of you and a view encompassing the landscape lays in front. A steep cliff is found before you and rocks huddle
around you like a shield - you can not take another step.""",

    "exits": {"north": "Woods"},

    "items": [],

    "npcs": [],

    "surroundings": [outlook_cliff, outlook_rocks],

    "display_name": """▄▄▄█████▓ ██░ ██ ▓█████     ▒█████   █    ██ ▄▄▄█████▓ ██▓     ▒█████   ▒█████   ██ ▄█▀
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▒██▒  ██▒ ██  ▓██▒▓  ██▒ ▓▒▓██▒    ▒██▒  ██▒▒██▒  ██▒ ██▄█▒ 
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒██░  ██▒▓██  ▒██░▒ ▓██░ ▒░▒██░    ▒██░  ██▒▒██░  ██▒▓███▄░ 
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒██   ██░▓▓█  ░██░░ ▓██▓ ░ ▒██░    ▒██   ██░▒██   ██░▓██ █▄ 
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░ ████▓▒░▒▒█████▓   ▒██▒ ░ ░██████▒░ ████▓▒░░ ████▓▒░▒██▒ █▄
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒
    ░     ▒ ░▒░ ░ ░ ░  ░     ░ ▒ ▒░ ░░▒░ ░ ░     ░    ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░
  ░       ░  ░░ ░   ░      ░ ░ ░ ▒   ░░░ ░ ░   ░        ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░ 
          ░  ░  ░   ░  ░       ░ ░     ░                  ░  ░    ░ ░      ░ ░  ░  ░   
                                                                                       """,
    "enemy": []

}

room_woods_boss = {
    "name": "The Woods: Clearing",

    "description": """An expanse of demolished trees lay before you as you hear the grunting of an animal.
Whatever the creature is, it seems to be in a frenzied state. You're yet to see the creature due to the
large fallen trees which block a clear view.""",  # Give the player a prompt if they want to turn back

    "exits": {"east": "Woods"},

    "items": [],

    "npcs": [],

    "surroundings": [],

    "display_name": """▄▄▄█████▓ ██░ ██ ▓█████     ▄████▄   ██▓    ▓█████ ▄▄▄       ██▀███   ██▓ ███▄    █   ▄████ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▒██▀ ▀█  ▓██▒    ▓█   ▀▒████▄    ▓██ ▒ ██▒▓██▒ ██ ▀█   █  ██▒ ▀█▒
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒▓█    ▄ ▒██░    ▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒▓▓▄ ▄██▒▒██░    ▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄  ░██░▓██▒  ▐▌██▒░▓█  ██▓
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ▒ ▓███▀ ░░██████▒░▒████▒▓█   ▓██▒░██▓ ▒██▒░██░▒██░   ▓██░░▒▓███▀▒
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░ ░▒ ▒  ░░ ▒░▓  ░░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
    ░     ▒ ░▒░ ░ ░ ░  ░     ░  ▒   ░ ░ ▒  ░ ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░ ▒ ░░ ░░   ░ ▒░  ░   ░ 
  ░       ░  ░░ ░   ░      ░          ░ ░      ░    ░   ▒     ░░   ░  ▒ ░   ░   ░ ░ ░ ░   ░ 
          ░  ░  ░   ░  ░   ░ ░          ░  ░   ░  ░     ░  ░   ░      ░           ░       ░ 
                           ░                                                                """,
    "enemy": enemy_werebear

}

room_lake = {
    "name": "The Lake",

    "description":
        """The peaceful waters of the lake reflect the sky above.
The soft sounds of the lapping water are calming. A boat is tied
to a small dock.""",

    "exits": {"west": "Village", "south": "Shoreline", "north": "Lily Pads"},

    "items": [],

    "npcs": [npc_lake_seraphina],

    "surroundings": [lake_boat, lake_island, lake_Pattern, lake_npc],

    "display_name": """▄▄▄█████▓ ██░ ██ ▓█████     ██▓    ▄▄▄       ██ ▄█▀▓█████ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓██▒   ▒████▄     ██▄█▒ ▓█   ▀ 
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒██░   ▒██  ▀█▄  ▓███▄░ ▒███   
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒██░   ░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄ 
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░██████▒▓█   ▓██▒▒██▒ █▄░▒████▒
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░ ▒░▓  ░▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░
    ░     ▒ ░▒░ ░ ░ ░  ░   ░ ░ ▒  ░ ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░
  ░       ░  ░░ ░   ░        ░ ░    ░   ▒   ░ ░░ ░    ░   
          ░  ░  ░   ░  ░       ░  ░     ░  ░░  ░      ░  ░
                                                          """,
    "enemy": []

}

room_lake_shoreline = {
    "name": "The Lake: Shoreline",

    "description": """Amidst the tranquil embrace of nature's untouched beauty,
the lake's shoreline unfolds in advance.
The water's edge, framed by a dense thicket of emerald foliage.""",

    "exits": {"north": "Lake"},

    "items": [],

    "npcs": [],

    "surroundings": [shoreline_water, shoreline_foliage, shoreline_docks],

    "display_name": """▄▄▄█████▓ ██░ ██ ▓█████      ██████  ██░ ██  ▒█████   ██▀███  ▓█████  ██▓     ██▓ ███▄    █ ▓█████ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▒██    ▒ ▓██░ ██▒▒██▒  ██▒▓██ ▒ ██▒▓█   ▀ ▓██▒    ▓██▒ ██ ▀█   █ ▓█   ▀ 
▒ ▓██░ ▒░▒██▀▀██░▒███      ░ ▓██▄   ▒██▀▀██░▒██░  ██▒▓██ ░▄█ ▒▒███   ▒██░    ▒██▒▓██  ▀█ ██▒▒███   
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄      ▒   ██▒░▓█ ░██ ▒██   ██░▒██▀▀█▄  ▒▓█  ▄ ▒██░    ░██░▓██▒  ▐▌██▒▒▓█  ▄ 
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ▒██████▒▒░▓█▒░██▓░ ████▓▒░░██▓ ▒██▒░▒████▒░██████▒░██░▒██░   ▓██░░▒████▒
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░░ ▒░ ░░ ▒░▓  ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░
    ░     ▒ ░▒░ ░ ░ ░  ░   ░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░   ░▒ ░ ▒░ ░ ░  ░░ ░ ▒  ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░
  ░       ░  ░░ ░   ░      ░  ░  ░   ░  ░░ ░░ ░ ░ ▒    ░░   ░    ░     ░ ░    ▒ ░   ░   ░ ░    ░   
          ░  ░  ░   ░  ░         ░   ░  ░  ░    ░ ░     ░        ░  ░    ░  ░ ░           ░    ░  ░
                                                                                                   """,
    "enemy": []

}

room_lake_island = {
    "name": "The Lake: Island",

    "description": """Walking across the awakened bridge. You felt a presence beneath you. Once you fully cross
you realised by no one sane has been here for decades.""",
    # After this description the Aboleth appears and the fight begins

    "exits": {"west": "Lake"},

    "items": [],

    "npcs": [],

    "surroundings": [],

    "display_name": """▄▄▄█████▓ ██░ ██ ▓█████     ██▓  ██████  ██▓    ▄▄▄       ███▄    █ ▓█████▄ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓██▒▒██    ▒ ▓██▒   ▒████▄     ██ ▀█   █ ▒██▀ ██▌
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒██▒░ ▓██▄   ▒██░   ▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ░██░  ▒   ██▒▒██░   ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░██░▒██████▒▒░██████▒▓█   ▓██▒▒██░   ▓██░░▒████▓ 
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░▓  ▒ ▒▓▒ ▒ ░░ ▒░▓  ░▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒ 
    ░     ▒ ░▒░ ░ ░ ░  ░    ▒ ░░ ░▒  ░ ░░ ░ ▒  ░ ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒ 
  ░       ░  ░░ ░   ░       ▒ ░░  ░  ░    ░ ░    ░   ▒      ░   ░ ░  ░ ░  ░ 
          ░  ░  ░   ░  ░    ░        ░      ░  ░     ░  ░         ░    ░    
                                                                     ░      """,
    "enemy": enemy_aboleth

}

room_lake_lily_pads = {
    "name": "The Lake: Lily Pads",

    "description": """thick lily pads blanket a portion of the shoreline.
Their ivy leaves, the size of platters, create a vibrant green bridge,
leading like stepping stones into the heart of this silent space untouched by civilisation.""",

    "exits": {"south": "Lake", "north": "Cove"},

    "items": [],

    "npcs": [],

    "surroundings": [],

    "display_name": """▄▄▄█████▓ ██░ ██ ▓█████     ██▓     ██▓ ██▓   ▓██   ██▓    ██▓███   ▄▄▄      ▓█████▄   ██████ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓██▒    ▓██▒▓██▒    ▒██  ██▒   ▓██░  ██▒▒████▄    ▒██▀ ██▌▒██    ▒ 
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒██░    ▒██▒▒██░     ▒██ ██░   ▓██░ ██▓▒▒██  ▀█▄  ░██   █▌░ ▓██▄   
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒██░    ░██░▒██░     ░ ▐██▓░   ▒██▄█▓▒ ▒░██▄▄▄▄██ ░▓█▄   ▌  ▒   ██▒
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░██████▒░██░░██████▒ ░ ██▒▓░   ▒██▒ ░  ░ ▓█   ▓██▒░▒████▓ ▒██████▒▒
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░ ▒░▓  ░░▓  ░ ▒░▓  ░  ██▒▒▒    ▒▓▒░ ░  ░ ▒▒   ▓▒█░ ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░
    ░     ▒ ░▒░ ░ ░ ░  ░   ░ ░ ▒  ░ ▒ ░░ ░ ▒  ░▓██ ░▒░    ░▒ ░       ▒   ▒▒ ░ ░ ▒  ▒ ░ ░▒  ░ ░
  ░       ░  ░░ ░   ░        ░ ░    ▒ ░  ░ ░   ▒ ▒ ░░     ░░         ░   ▒    ░ ░  ░ ░  ░  ░  
          ░  ░  ░   ░  ░       ░  ░ ░      ░  ░░ ░                       ░  ░   ░          ░  
                                               ░ ░                            ░               """,
    "enemy": []

}

room_lake_lily_pads_cove = {
    "name": "The Lake: Lily Pad Cove",

    "description": """Moving onto the slippery pads, they struggle under your weight: barely keeping you afloat.
As you walk along the pads, you find yourself in a cove. The water shimmers and reflects aquamarine onto the
rocky walls""",

    "exits": {"south": "Lily Pads"},

    "items": [],

    "npcs": [],

    "surroundings": [lily_pads_cove_reflections],

    "display_name": """▄▄▄█████▓ ██░ ██ ▓█████     ▄████▄   ▒█████   ██▒   █▓▓█████ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▒██▀ ▀█  ▒██▒  ██▒▓██░   █▒▓█   ▀ 
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒▓█    ▄ ▒██░  ██▒ ▓██  █▒░▒███   
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒▓▓▄ ▄██▒▒██   ██░  ▒██ █░░▒▓█  ▄ 
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ▒ ▓███▀ ░░ ████▓▒░   ▒▀█░  ░▒████▒
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░ ░▒ ▒  ░░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░
    ░     ▒ ░▒░ ░ ░ ░  ░     ░  ▒     ░ ▒ ▒░    ░ ░░   ░ ░  ░
  ░       ░  ░░ ░   ░      ░        ░ ░ ░ ▒       ░░     ░   
          ░  ░  ░   ░  ░   ░ ░          ░ ░        ░     ░  ░
                           ░                      ░          """,
    "enemy": []

}

room_mines = {
    "name": "The Mines",

    "description":
        """The entrance to the mines is dark and foreboding.
Torches line the walls, flickering and casting odd shadows.
You can hear the distant sound of pickaxes.""",

    "exits": {"north": "Village", "east": "Shaft", "west": "Miner's Shack"},

    "items": [item_coal],

    "npcs": [npc_mines_dargrim],

    "surroundings": [],

    "display_name": """ ███▄ ▄███▓ ██▓ ███▄    █ ▓█████   ██████    ▓█████  ███▄    █ ▄▄▄█████▓ ██▀███   ▄▄▄       ███▄    █  ▄████▄  ▓█████ 
▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▓█   ▀ ▒██    ▒    ▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄     ██ ▀█   █ ▒██▀ ▀█  ▓█   ▀ 
▓██    ▓██░▒██▒▓██  ▀█ ██▒▒███   ░ ▓██▄      ▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▓██  ▀█ ██▒▒▓█    ▄ ▒███   
▒██    ▒██ ░██░▓██▒  ▐▌██▒▒▓█  ▄   ▒   ██▒   ▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒▒▓█  ▄ 
▒██▒   ░██▒░██░▒██░   ▓██░░▒████▒▒██████▒▒   ░▒████▒▒██░   ▓██░  ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒██░   ▓██░▒ ▓███▀ ░░▒████▒
░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░   ░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░░░ ▒░ ░
░  ░      ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░░ ░▒  ░ ░    ░ ░  ░░ ░░   ░ ▒░    ░      ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░  ▒    ░ ░  ░
░      ░    ▒ ░   ░   ░ ░    ░   ░  ░  ░        ░      ░   ░ ░   ░        ░░   ░   ░   ▒      ░   ░ ░ ░           ░   
       ░    ░           ░    ░  ░      ░        ░  ░         ░             ░           ░  ░         ░ ░ ░         ░  ░
                                                                                                      ░               """,
    "enemy": []

}

room_mines_miner = {
    "name": "The Mines: Miner's Shack",

    "description": """Afore is a rundown shack, light piercing through it's shameful architecture.
a wretched smell creeps into your nose as you enter the area.""",

    "exits": {"east": "Mines", "south": "Cave", "west": "Outside Shack"},

    "items": [item_chain, item_ladder],

    "npcs": [],

    "surroundings": [],

    "display_name": """ ███▄ ▄███▓ ██▓ ███▄    █ ▓█████  ██▀███    ██████      ██████  ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀
▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒▒██    ▒    ▒██    ▒ ▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ 
▓██    ▓██░▒██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒░ ▓██▄      ░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
▒██    ▒██ ░██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒     ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
▒██▒   ░██▒░██░▒██░   ▓██░░▒████▒░██▓ ▒██▒▒██████▒▒   ▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░   ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
░  ░      ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░   ░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
░      ░    ▒ ░   ░   ░ ░    ░     ░░   ░ ░  ░  ░     ░  ░  ░   ░  ░░ ░  ░   ▒   ░        ░ ░░ ░ 
       ░    ░           ░    ░  ░   ░           ░           ░   ░  ░  ░      ░  ░░ ░      ░  ░   
                                                                                 ░               """,
    "enemy": []

}

room_mines_miner_shack_outside = {
    "name": "The Mines: Outside Shack",

    "description": "The outside of the shack is desolate of any attention or care. Who knows what creature lives here?",

    "exits": {"east": "Miner's Shack"},

    "items": [],

    "npcs": [],

    "surroundings": [],

    "display_name": """
 ▒█████   █    ██ ▄▄▄█████▓  ██████  ██▓▓█████▄ ▓█████      ██████  ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀
▒██▒  ██▒ ██  ▓██▒▓  ██▒ ▓▒▒██    ▒ ▓██▒▒██▀ ██▌▓█   ▀    ▒██    ▒ ▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ 
▒██░  ██▒▓██  ▒██░▒ ▓██░ ▒░░ ▓██▄   ▒██▒░██   █▌▒███      ░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
▒██   ██░▓▓█  ░██░░ ▓██▓ ░   ▒   ██▒░██░░▓█▄   ▌▒▓█  ▄      ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
░ ████▓▒░▒▒█████▓   ▒██▒ ░ ▒██████▒▒░██░░▒████▓ ░▒████▒   ▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
░ ▒░▒░▒░ ░▒▓▒ ▒ ▒   ▒ ░░   ▒ ▒▓▒ ▒ ░░▓   ▒▒▓  ▒ ░░ ▒░ ░   ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
  ░ ▒ ▒░ ░░▒░ ░ ░     ░    ░ ░▒  ░ ░ ▒ ░ ░ ▒  ▒  ░ ░  ░   ░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
░ ░ ░ ▒   ░░░ ░ ░   ░      ░  ░  ░   ▒ ░ ░ ░  ░    ░      ░  ░  ░   ░  ░░ ░  ░   ▒   ░        ░ ░░ ░ 
    ░ ░     ░                    ░   ░     ░       ░  ░         ░   ░  ░  ░      ░  ░░ ░      ░  ░   
                                         ░                                           ░               
""",
    "enemy": []
}

room_mines_miner_shack_inside = {
    "name": "The Mines: Inside Shack",

    "description": """The door scrapes across the floor as you push the door open, 
producing a violent screech with each movement. Inside you see a hobbled man and what looks to be his home.""",

    "exits": {"east": "Outside Shack"},

    "items": [],

    "npcs": [npc_miner_oldman],

    "surroundings": [],

    "display_name": """
 ██▓ ███▄    █   ██████  ██▓▓█████▄ ▓█████      ██████  ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀
▓██▒ ██ ▀█   █ ▒██    ▒ ▓██▒▒██▀ ██▌▓█   ▀    ▒██    ▒ ▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ 
▒██▒▓██  ▀█ ██▒░ ▓██▄   ▒██▒░██   █▌▒███      ░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
░██░▓██▒  ▐▌██▒  ▒   ██▒░██░░▓█▄   ▌▒▓█  ▄      ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
░██░▒██░   ▓██░▒██████▒▒░██░░▒████▓ ░▒████▒   ▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
░▓  ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░░▓   ▒▒▓  ▒ ░░ ▒░ ░   ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
 ▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░ ▒ ░ ░ ▒  ▒  ░ ░  ░   ░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
 ▒ ░   ░   ░ ░ ░  ░  ░   ▒ ░ ░ ░  ░    ░      ░  ░  ░   ░  ░░ ░  ░   ▒   ░        ░ ░░ ░ 
 ░           ░       ░   ░     ░       ░  ░         ░   ░  ░  ░      ░  ░░ ░      ░  ░   
                             ░                                           ░               
""",
    "enemy": []
}

room_mines_miner_cave = {
    "name": "The Mines: Cave",

    "description": "A short walk from the shack leads to a darkened cave.",

    "exits": {"north": "Miner's Shack"},

    "items": [],

    "npcs": [],

    "surroundings": [],

    "display_name": """
 ▄████▄   ▄▄▄    ██▒   █▓▓█████ 
▒██▀ ▀█  ▒████▄ ▓██░   █▒▓█   ▀ 
▒▓█    ▄ ▒██  ▀█▄▓██  █▒░▒███   
▒▓▓▄ ▄██▒░██▄▄▄▄██▒██ █░░▒▓█  ▄ 
▒ ▓███▀ ░ ▓█   ▓██▒▒▀█░  ░▒████▒
░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▐░  ░░ ▒░ ░
  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ░  ░
░          ░   ▒     ░░     ░   
░ ░            ░  ░   ░     ░  ░
░                    ░          
""",
    "enemy": []
}

room_mines_shaft = {
    "name": "The Mines: Shaft",

    "description": """In the depths of the long-forgotten, abandoned mine lay an ominous secret — a treacherous,
mine shaft, hidden away from the world.""",

    "exits": {"west": "Mines"},

    "items": [item_rope],

    "npcs": [],

    "surroundings": [],

    "display_name": """▄▄▄█████▓ ██░ ██ ▓█████     ███▄ ▄███▓ ██▓ ███▄    █ ▓█████   ██████  ██░ ██  ▄▄▄        █████▒▄▄▄█████▓
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▓█   ▀ ▒██    ▒ ▓██░ ██▒▒████▄    ▓██   ▒ ▓  ██▒ ▓▒
▒ ▓██░ ▒░▒██▀▀██░▒███      ▓██    ▓██░▒██▒▓██  ▀█ ██▒▒███   ░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ▒████ ░ ▒ ▓██░ ▒░
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒██    ▒██ ░██░▓██▒  ▐▌██▒▒▓█  ▄   ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ░▓█▒  ░ ░ ▓██▓ ░ 
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ▒██▒   ░██▒░██░▒██░   ▓██░░▒████▒▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒░▒█░      ▒██▒ ░ 
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒ ░      ▒ ░░   
    ░     ▒ ░▒░ ░ ░ ░  ░   ░  ░      ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░ ░          ░    
  ░       ░  ░░ ░   ░      ░      ░    ▒ ░   ░   ░ ░    ░   ░  ░  ░   ░  ░░ ░  ░   ▒    ░ ░      ░      
          ░  ░  ░   ░  ░          ░    ░           ░    ░  ░      ░   ░  ░  ░      ░  ░                 
                                                                                                        """,
    "enemy": []

}

room_mines_shaft_upper = {

    "name": "The Mines: Upper Level",

    "description": """Bringing the ladder up to the rail track above leads to a new path. From here you can see the
vast depth of the mines. Echoes of the creaking structures built before abandonment haunt your ears.
You notice a sparkle in the corner of your eye.""",

    "exits": {"south": "Shaft", "west": "Dark Corner"},

    "items": [],

    "npcs": [],

    "surroundings": [],

    "display_name": """
 █    ██  ██▓███   ██▓███  ▓█████  ██▀███      ██▓    ▓█████ ██▒   █▓▓█████  ██▓    
 ██  ▓██▒▓██░  ██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒   ▓██▒    ▓█   ▀▓██░   █▒▓█   ▀ ▓██▒    
▓██  ▒██░▓██░ ██▓▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒   ▒██░    ▒███   ▓██  █▒░▒███   ▒██░    
▓▓█  ░██░▒██▄█▓▒ ▒▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄     ▒██░    ▒▓█  ▄  ▒██ █░░▒▓█  ▄ ▒██░    
▒▒█████▓ ▒██▒ ░  ░▒██▒ ░  ░░▒████▒░██▓ ▒██▒   ░██████▒░▒████▒  ▒▀█░  ░▒████▒░██████▒
░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ▒░▓  ░░░ ▒░ ░  ░ ▐░  ░░ ▒░ ░░ ▒░▓  ░
░░▒░ ░ ░ ░▒ ░     ░▒ ░      ░ ░  ░  ░▒ ░ ▒░   ░ ░ ▒  ░ ░ ░  ░  ░ ░░   ░ ░  ░░ ░ ▒  ░
 ░░░ ░ ░ ░░       ░░          ░     ░░   ░      ░ ░      ░       ░░     ░     ░ ░   
   ░                          ░  ░   ░            ░  ░   ░  ░     ░     ░  ░    ░  ░
                                                                 ░                  
""",
    "enemy": []
}

room_mines_shaft_upper_dark = {
    "name": "Dark Corner",

    "description": """This section of the upper levels is pitch-black. The path seems to be caved in with rubble
and rock.""",

    "exits": {"east": "Upper Mines"},

    "items": [],

    "npcs": [],

    "surroundings": [],

    "display_name": """
▓█████▄  ▄▄▄       ██▀███   ██ ▄█▀    ▄████▄   ▒█████   ██▀███   ███▄    █ ▓█████  ██▀███  
▒██▀ ██▌▒████▄    ▓██ ▒ ██▒ ██▄█▒    ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░    ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄    ▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
░▒████▓  ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄   ▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒▒██░   ▓██░░▒████▒░██▓ ▒██▒
 ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒   ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
 ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░     ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ░ ░  ░   ░   ▒     ░░   ░ ░ ░░ ░    ░        ░ ░ ░ ▒    ░░   ░    ░   ░ ░    ░     ░░   ░ 
   ░          ░  ░   ░     ░  ░      ░ ░          ░ ░     ░              ░    ░  ░   ░     
 ░                                   ░                                                     
""",
    "enemy": []
}

rooms = {
    "Village": room_village,
    "Dragon": room_dragon,
    "Woods": room_woods,
    "Lake": room_lake,
    "Marsh": room_woods_marsh,
    "Outlook": room_woods_outlook,
    "Clearing": room_woods_boss,
    "Mines": room_mines,
    "Shaft": room_mines_shaft,
    "Miner's Shack": room_mines_miner,
    "Upper Mines": room_mines_shaft_upper,
    "Island": room_lake_island,
    "Shoreline": room_lake_shoreline,
    "Lily Pads": room_lake_lily_pads,
    "Cabin Outside": room_woods_marsh_outside_cabin,
    "Inside Cabin": room_woods_marsh_inside_cabin,
    "Cove": room_lake_lily_pads_cove,
    "Dark Corner": room_mines_shaft_upper_dark,
    "Cave": room_mines_miner_cave,
    "Outside Shack": room_mines_miner_shack_outside,
    "Inside Shack": room_mines_miner_shack_inside
}

player_current_room = rooms["Village"]
