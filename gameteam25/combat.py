import random
import sys
from os import system, name
from gameparser import normalise_input
import time
from player import *
from game import main
from ending import *

global delay
delay = 0.5
player_unselected_weapon = True
health = int(player["health"])


def combat_loop(e_name, e_health, e_damage, e_desc):
    global delay
    global enemy_alive
    global enemy_health, enemy_damage, enemy_name

    player_name = player["name"]
    enemy_alive = True
    enemy_health = int(e_health)
    enemy_name = e_name
    enemy_damage = int(e_damage)
    enemy_description = e_desc

    # Functions needed for text
    def type_text(text, delay):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()

        print()

    def tips():
        print("Welcome to combat! Here are some functions you can use:")
        print("ATTACK - For example, to do a light or heavy attack type: 'ATTACK LIGHT' or 'ATTACK HEAVY'")
        print("STATUS - For example, to check on your enemy's status type: STATUS (ENEMY NAME)")
        print("PLAYER NAME - For example, to check your own player status, type: (PLAYER NAME)")

    def clear_screen():
        time.sleep(0.5)
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    # Enemy status function
    def enemy_status():
        print(f"Name: {enemy_name.upper()}")
        print(f"Health: {enemy_health}")
        print(f"Damage: {enemy_damage}")

    def player_status():
        print(f"Name: {player['name']}")
        print(f"Health: {health}")
        print(f"Damage: {player_damage}")
        print(f"Milestone: {player['milestone']}")

    # Enemy attack function
    def enemy_attack():
        global health
        hit = random.randrange(1, 100)
        if hit < 75:
            health -= enemy_damage
            print(f"The {enemy_name} hit you for {enemy_damage}!")
            return health
        else:
            print(f"The {enemy_name} misses it's attack!")
            return

    # Attack functions
    def light_attack(damage, enemy_health):
        enemy_health -= damage
        print(f"You dealt {damage} to the {enemy_name}")
        return enemy_health

    def heavy_attack(damage, enemy_h):
        hit = random.randrange(1, 100)
        if hit < 75:
            print("You miss the attack")
            return enemy_h
        elif hit >= 75:
            print(f"You dealt {damage * 2} to the {enemy_name}")
            enemy_h -= damage * 2
        return enemy_h

    type_text(enemy_description, delay)

    while enemy_alive:
        global player_damage
        global player_weapon
        global player_unselected_weapon
        global player_damage

        if health <= 0:
            game_ending("Early Demise")

        if int(enemy_health) <= 0:
            if enemy_name == "Aurum":
                game_ending("Triumph")
            else:
              enemy_alive = False
              return enemy_alive

        if player_unselected_weapon:
            for weapon in player_weapon:
                print(f"{weapon['id'].upper()}: {weapon['description']} dealing {weapon['damage']} damage\n")
            user_weapon = input("What weapon will you use?\n")
            normalise_input(user_weapon)
            if user_weapon == "":
                player_damage = 1
                print("You have selected your fists!")
            for weapon in player_weapon:
                if user_weapon == weapon["id"]:
                    player_damage = int(weapon["damage"])
                    player_unselected_weapon = False

        type_text("What will you do?:\n", delay)
        user_input = input()
        if user_input == "":
            type_text("You must put in a command! Use COMBAT if you want to see a list of  combat commands!", delay)
            continue
        user_choice = normalise_input(user_input)
        clear_screen()

        if (user_choice[0] == "attack"):
            if (len(user_choice) == 1):
                print("How do you want to attack? Light Or Heavy?")
                continue
                pass
            if user_choice[1] == "light":
                enemy_health = light_attack(player_damage, enemy_health)
                enemy_attack()
                continue
            if user_choice[1] == "heavy":
                enemy_health = heavy_attack(player_damage, enemy_health)
                enemy_attack()
                continue
            else:
                print("That is an invalid way of attacking")
        elif user_choice[0] == "status":
            if (len(user_choice) == 1):
                type_text("What are you checking the status of?", delay)
                print()
                pass
            if user_choice[1].lower() == enemy_name.lower():
                enemy_status()
        elif user_choice[0] == "combat":
            tips()
        elif user_choice[0] == player_name.lower():
            player_status()
        else:
            print("That is not a valid input")
