from player import player


def game_ending(ending_type):
    
    if ending_type == "Early Demise":

        print("""
▓█████ ▄▄▄       ██▀███   ██▓   ▓██   ██▓   ▓█████▄ ▓█████  ███▄ ▄███▓ ██▓  ██████ ▓█████ 
▓█   ▀▒████▄    ▓██ ▒ ██▒▓██▒    ▒██  ██▒   ▒██▀ ██▌▓█   ▀ ▓██▒▀█▀ ██▒▓██▒▒██    ▒ ▓█   ▀ 
▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒▒██░     ▒██ ██░   ░██   █▌▒███   ▓██    ▓██░▒██▒░ ▓██▄   ▒███   
▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄  ▒██░     ░ ▐██▓░   ░▓█▄   ▌▒▓█  ▄ ▒██    ▒██ ░██░  ▒   ██▒▒▓█  ▄ 
░▒████▒▓█   ▓██▒░██▓ ▒██▒░██████▒ ░ ██▒▓░   ░▒████▓ ░▒████▒▒██▒   ░██▒░██░▒██████▒▒░▒████▒
░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░▓  ░  ██▒▒▒     ▒▒▓  ▒ ░░ ▒░ ░░ ▒░   ░  ░░▓  ▒ ▒▓▒ ▒ ░░░ ▒░ ░
 ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░░ ░ ▒  ░▓██ ░▒░     ░ ▒  ▒  ░ ░  ░░  ░      ░ ▒ ░░ ░▒  ░ ░ ░ ░  ░
   ░    ░   ▒     ░░   ░   ░ ░   ▒ ▒ ░░      ░ ░  ░    ░   ░      ░    ▒ ░░  ░  ░     ░   
   ░  ░     ░  ░   ░         ░  ░░ ░           ░       ░  ░       ░    ░        ░     ░  ░
                                 ░ ░         ░                                            
""")

        print("As the dragon roars and engulfs the surroundings in flames. The last thing the townsfolk see is the glint of its malevolent eyes. Your journey has come to an untimely end.")
        print("Your brave effort will be remembered, but the story of your heroism ends here.")
        print("Do you wish to try again? (Yes/No)")
        print()
        print("Thank you for playing!")
        exit()
    
    elif ending_type == "Triumph":
        print("""
▄▄▄█████▓ ██▀███   ██▓ █    ██  ███▄ ▄███▓ ██▓███   ██░ ██ 
▓  ██▒ ▓▒▓██ ▒ ██▒▓██▒ ██  ▓██▒▓██▒▀█▀ ██▒▓██░  ██▒▓██░ ██▒
▒ ▓██░ ▒░▓██ ░▄█ ▒▒██▒▓██  ▒██░▓██    ▓██░▓██░ ██▓▒▒██▀▀██░
░ ▓██▓ ░ ▒██▀▀█▄  ░██░▓▓█  ░██░▒██    ▒██ ▒██▄█▓▒ ▒░▓█ ░██ 
  ▒██▒ ░ ░██▓ ▒██▒░██░▒▒█████▓ ▒██▒   ░██▒▒██▒ ░  ░░▓█▒░██▓
  ▒ ░░   ░ ▒▓ ░▒▓░░▓  ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░▒▓▒░ ░  ░ ▒ ░░▒░▒
    ░      ░▒ ░ ▒░ ▒ ░░░▒░ ░ ░ ░  ░      ░░▒ ░      ▒ ░▒░ ░
  ░        ░░   ░  ▒ ░ ░░░ ░ ░ ░      ░   ░░        ░  ░░ ░
            ░      ░     ░            ░             ░  ░  ░
                                                           
""")
        print("With one final swing of your sword, the mighty Dragon  lets out a deafening roar before crashing to the ground. The entire village rejoices as you stand triumphant over the defeated beast." )
        print(f"The villagers celebrate your victory, chanting your name - {player['name']}! The hero who saved the village!")
        print("You'll forever be remembered in tales and songs as the legendary hero who defeated the Dragon.")
        print()
        print("Thank you for playing!")
        exit()
    
    elif ending_type == "Eye-opener":
        print("""
▓█████▓██   ██▓▓█████     ▒█████   ██▓███  ▓█████  ███▄    █ ▓█████  ██▀███  
▓█   ▀ ▒██  ██▒▓█   ▀    ▒██▒  ██▒▓██░  ██▒▓█   ▀  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▒███    ▒██ ██░▒███      ▒██░  ██▒▓██░ ██▓▒▒███   ▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
▒▓█  ▄  ░ ▐██▓░▒▓█  ▄    ▒██   ██░▒██▄█▓▒ ▒▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
░▒████▒ ░ ██▒▓░░▒████▒   ░ ████▓▒░▒██▒ ░  ░░▒████▒▒██░   ▓██░░▒████▒░██▓ ▒██▒
░░ ▒░ ░  ██▒▒▒ ░░ ▒░ ░   ░ ▒░▒░▒░ ▒▓▒░ ░  ░░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
 ░ ░  ░▓██ ░▒░  ░ ░  ░     ░ ▒ ▒░ ░▒ ░      ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
   ░   ▒ ▒ ░░     ░      ░ ░ ░ ▒  ░░          ░      ░   ░ ░    ░     ░░   ░ 
   ░  ░░ ░        ░  ░       ░ ░              ░  ░         ░    ░  ░   ░     
       ░ ░                                                                   
""")
        print("You lower your weapon, realizing that the dragon isn't the true enemy. The dragon, sensing your change of heart, communicates with you telepathically.")
        print("'Thank you, brave human. The real chaos was caused by the very villagers you sought to protect. They've been exploiting my kind for ages, stealing our wealth'")
        print("With the dragon's help, you expose the villagers' dark secrets. The Village is shaken by the revelations, but now has a chance for true peace and coexistence between dragon and humans.")
        print(f"{player['name']}, you have not just saved the Village but also opened the eyes of its people. Your legacy will be of a wise hero, who chose understanding over violence.")
        print()
        print("Thank you for playing!")
        exit()
    
    else:
        print("Unknown ending type. Something went wrong!")
        print()
        print("Thank you for playing!")
        exit()

    # Here you can add a code to restart the game or exit.

# To trigger an ending, you can call:
# game_ending("Triumph")
