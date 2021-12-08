# CSC 221
# BorkDay Mac! - Text Adventure
# Rebecca Garcia

# MyGame - implements game specific functions

#from  MAC_Player import Player
from  MAC_Game import Game
from  MAC_Room import Room
from  MAC_Item import Item
import sys, time


title = (
    "  ____             _    ____              _   __  __                         \n" +            
    " | __ )  ___  _ __| | _|  _ \  __ _ _   _| | |  \/  | __ _  ___    __        \n" + 
    " |  _ \ / _ \| '__| |/ / | | |/ _` | | | | | | |\/| |/ _` |/ __|o-''|\_____/)\n" + 
    " | |_) | (_) | |  |   <| |_| | (_| | |_| |_| | |  | | (_| | (__  \_/|_)     )\n" + 
    " |____/ \___/|_|  |_|\_\____/ \__,_|\__, (_) |_|  |_|\__,_|\___|    \  __  / \n" + 
    "                                     |___/                          (_/ (_/  \n" +
    "============================================================================== " ) 

mapM = ("\t[*APT12B*]-----[Pond]-----[APT9C]        N      \n" +
        "\t    |            |          |            |      \n" +
        "\t    |            |          |         W--+--E   \n" +
        "\t [BBPP]   [Main Office]-----!            |      \n" +
        "\t                                         S      \n" )
    
formatX = "--------------------------------------------------------\n"
    
#----------------------------------------------------------------------------------------------------------------------------        

def startRoom():
    
    print("\n Woof! you like to play?")
    player = input("> ")
    
    playerInput = player.split() # split on whitespace
    if len(playerInput) < 1:
        print("No input detected")
        return
       
    play = playerInput[0].lower()
        
    if play == "yes":
        print(formatX + "loading game...")
        time.sleep(1)
        print(formatX + title   + "\n")  
        time.sleep(1)
        print("\t\t\t\t\t  Map\n" + formatX)
        print(mapM + formatX)
        
        game = MyGame()
    
        game.setup()  
        
        
        game.output("Starting game -- enter command.")
        game.loop()
        game.end()
    if play!= "yes" and play!="no":
        print("You're barking up the wrong tree..")
        startRoom()
    else:
        print("goodbye!")        
#----------------------------------------------------------------------------------------------------------------------------   
    
class MyGame(Game):
    """ the Game class should be subclassed to add
    game specific features, including the world setup. 
    """    
    def setup(self):
        """ Load your own rooms in the method of your choosing.
        Consider a GameLoader class that might read these
        from a file...
        """
        loader = MyGameLoader()
        self.rooms = loader.setup()
        
        # starting location
        self.here = self.rooms["APT12B"]
        # Let's do a turn 1 look , to orient the player
        self.here.describe() 
#----------------------------------------------------------------------------------------------------------------------------    
    
class MyGameLoader:
    """ just used to put all the room setup in a separate class,
    and if needed, a separate file.
    """
    def setup(self):
        
        APT12B      = Room ("APT12B",
                            " Cozy third floor apartment overlooking pond. Floor to ceiling windows decorated with\n" +
                            "string lights. You and Macs safe haven.",
                           {"East"  : "Pond",
                            "South" : "BBPP" })
    
        Pond        = Room ("Pond",
                            " Complex pond full of life! Ducks, geese, squirrels, benches shaded by tall, lush, palm\n" + 
                            "and live oak trees covered in spanish moss.",
                           {"East"  : "APT9C",
                            "South" : "MainOffice",
                            "West"  : "APT12B" })
        
        APT9C       = Room ("APT9C",
                            " Younger brothers second floor apt. Shelves filled with POP!s. 3D printer half way\n" + 
                            "installed sits on desk. Doggie bowls in corner",
                           {"West"  : "Pond",
                            "South" : "MainOffice" })
        
        MainOffice  = Room ("MainOffice",
                            " Next to the gym. Overlooking pool area. Hub to centralized unit of individually locked\n" + 
                            "compartments for the delivery and collection of mail.",
                           {"North" : "Pond",
                            "East"  : "APT9C" })
        
        BBPP        = Room ("BBPP",
                            " Brohard Paw Park and Doggie Beach. Next to Venice Municipal Airport. A marvelous sight of \n" +
                            "happy doggos, clear, calm waters and the occassional plane flying right above.",
                           {"North" : "APT12B" } )
        
        # Place rooms in a dictionary.
        # (Game will handle this in the full version)
        rooms = {   APT12B.name: APT12B, 
                      Pond.name: Pond,
                     APT9C.name: APT9C,
                MainOffice.name: MainOffice,
                      BBPP.name: BBPP}
        
       #  items in APT12B
        MAC      = Item("Mac", "The king of the show, my reason, my love, my sweet doggo!\n" +
              "      fluffy smart loyal cute 9 yr old Aussie with a tail (: ")
        leash    = Item("leash", "Snoppy themed decorated leash you found\n" +
              "      in the woods hiking, possibly a gift left behind by the forest fairies?")
        collar   = Item("collar", "Shiny studded collar with a nicely golden\n" +
              "      engraved nametag which reads MAC")
        keyCard  = Item ("key card", "small plastic card used instead of a door key,\n" +
              "      bearing magnetically encoded data which is read and processed by an electronic device")
        bandana  = Item ("lavender infused bandana", "scientifically proven aromatherapy to reduce stress, anxiety and overexcitement in dogs")
        #  items added
        APT12B.addItem(MAC)
        APT12B.addItem(leash)
        APT12B.addItem(collar)
        APT12B.addItem(keyCard)
        APT12B.addItem(bandana)    
        
        # Pond
        squirrel = Item("squirrel", "slender body, bushy tail & large eyed\n" +
              "      rodents that Mac is sure are EVIL")
        #  items added
        Pond.addItem(squirrel)
        
        # APT9C
        Coqui    = Item("Coqui", "Your SUPER (lol) annoyingly rude sibling who ironically loves \n" +
              "      your dog next to as close as you do, who you can trust to dogsit (in short intervals that is) -_-'")
        #  items added
        APT9C.addItem(Coqui)
        
        #MainOffice (key)
        cardScan = Item("Card Scanner", "data input device that reads data from your keycard which will allow entry to Main Office")
        Armando  = Item("Armando", "Super kind apt complex maintence guy who loves dogs and jokes")
        #  items added
        MainOffice.addItem(cardScan)
        MainOffice.addItem(Armando)    
        
        #BB&PP
        Odette   = Item("Odette", "Thors human, Armando's partner")
        Thor     = Item("Thor", "the kings best doggo Rottie friend, theyre basically brother")
        #  items added
        BBPP.addItem(Odette)
        BBPP.addItem(Thor)
    
    #print(loc.contents) # just dump the list
                
        return rooms 
#----------------------------------------------------------------------------------------------------------------------------      
      
# Startup
def main():
    #will allow the program to quit, without generating an error/protecting code
    try:    
        startRoom()
    except SystemExit:
        pass
    

if __name__ == "__main__":
    main()