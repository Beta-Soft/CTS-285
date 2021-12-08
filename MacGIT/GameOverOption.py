#things to implement in BorkDay Mac <3 :)

# CSC 221
# BorkDay Mac! - Text Adventure
# Rebecca Garcia

# Game loop
# =============================================================================
#     game_over = True
#     running = True
#     while running:
#         if game_over:
#             show_go_screen()
#             
#     # Game loop
#     game_over = True
#     running = True
#     while running:
#         if game_over:
#             show_go_screen()
#             game_over = False#when gameover start everything fresh
#             #keep loop running at the right speed
#             all_sprites = pygame.sprite.Group()
#             mobs = pygame.sprite.Group()
#             bullets = pygame.sprite.Group()
#             powerups = pygame.sprite.Group()
#             player = Player()
#             all_sprites.add(player)
#             for i in range(8):
#                 newmob()
#             score = 0
# =============================================================================
import sys, time 

inventory = []

def game():

    print("You are in game!\n")
    print("You are standing at a locked door and there is a key and box on the ground.")
    in_room = True

    while in_room == True: 
        action = input("What do you do?: ").lower().strip()

        if action == "pick up key":
            print("You picked up the key and added it to your inventory")
            inventory.append("key")

        elif action == "open door" and ("key") not in inventory:
            print("The door is locked")
            GameOver()
            
        elif action == "open door" and ("key") in inventory:
            print("The door opens")
            #inventory.remove("key")
            if ("box") in inventory:
                print("But you can not pass thru it with box")
            else:
                in_room = False

        elif action == "open door" and ("key", "box") in inventory:
            print("The door opens")
            #inventory.remove("key")
            print("But you can not pass thru it with box")
            
        elif action == "open box":
            
            print("You open the box and out comes a troll!!\n")
            time.sleep(1)
            print("He stares at you for a second...\n")
            time.sleep(2)
            print("you stare back...\n")
            time.sleep(2)
            print("suddenly...\n")
            time.sleep(2)
            print("he eats you and youre dead LOL\n")
            time.sleep(2)
            GameOver()         
            
        elif action == "pick up box":
            print("You picked up the box and added it to your inventory")
            inventory.append("box")
            
        elif action == "view inv":
            if len(inventory) == 0:
                print("your inv is empty")
            else:
                print("your inventory: \n",  inventory)
                
        elif action == "view box":
            if ("box" in inventory):
                print("Theres a strange noise coming from the box...could it be a puppy?")
            else:
                print("The box is sitting in the corner")
                
        elif action == "view key":
            if ("key" in inventory):
                print("rusty key with a star shaped base")
            else:
                print("the key is on the floor. Try picking it up!")
            
        elif action == "drop key":
            if len(inventory) == 0:
                print("your inv is empty")
            else:
                inventory.remove("key")
                print("You have dropped the key")
                
        elif action == "drop box":
           if len(inventory) == 0:
               print("your inv is empty")
           else:
               inventory.remove("box")
               print("You have dropped the box")
            
        elif action == "quit":
             print("goodbye")
             playAgain()
             
        elif action == "view door":
            print("The door is locked!")            
            if 'key' in inventory:
                print("You currently have a key to open the door tho! \n" 
                    + "Try that maybe?")
            else:
                print("You must equip key first!")
             
        else:
            print("I do not understand")
    else:
        print("Congrat! you made it out!")
        playAgain()

# =============================================================================       
        
def startRoom():
    print("would you like to play or leave?")
    player = input("> ")
    
    playerInput = player.split() # split on whitespace
    if len(playerInput) < 1:
        print("No input detected")
        return
       
    play = playerInput[0].lower()
        
    if play == "play":        
        game()
    else:
        print("goodbye!")
# =============================================================================         
    
def GameOver(): #gameover FUNCTION
    print("Game Over\n")
    time.sleep(2)
    playAgain() 
# =============================================================================
    
def playAgain(): #playagain FUNCTION   
    print("Would you like to play again?")
    answer = input("> ")
    if answer == "yes":
        print("restarting program...")
        time.sleep(1)
        print("Thank you for your patience! Game load is almost complete")
        time.sleep(2)
        game()
    else:
        print("Thanks for playing")
        sys.exit() #telling program to stop and end program/to use need to import sys
# =============================================================================
        
def print_inventory(dct):
    print("Items held:")
    for item, amount in dct.items():  # dct.iteritems() in Python 2
        print("{} ({})".format(item, amount))

    inventory = {
        "shovels": 3,
         "sticks": 2,
           "dogs": 1, }
    
    lst = [1, 2, 3]
    print('My list:', *lst, sep='\n- ')
    
    print_inventory(inventory + "\n")
# =============================================================================
# Which prints:
# Items held:
# shovels (3)
# sticks (2)
# dogs (1)



















                                                              

# =============================================================================
        
#will allow the program to quit, without generating an error/protecting code
try:    
    startRoom()
except SystemExit:
    pass