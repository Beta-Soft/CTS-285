# CSC 221
# BorkDay Mac! - Text Adventure
# Rebecca Garcia

from  MAC_Room import Room
from  MAC_Player import Player
from  MAC_Item import Item
#from  MAC_Container import Container

"""
Version history:
    v1 - built using Room references (basically a graph). 
        downside: you have to create all rooms, then link
        them together afterwards.
        
    v2 - used constant room IDs to make it possible to add
        and link rooms in one pass. 
        downside: "this looks like BASIC" (from the peanut gallery)
        
    v3 - realization: if the Room names are unique, that's a
        unique ID. I therefore changed
        the container for all Rooms to be a dictionary --
        now it's easy enough to look up the room by name.


"""
mapM = ("[*APT12B*]-----[Pond]-----[APT9C]            N      \n" +
            "    |            |          |            |      \n" +
            "    |            |          |         W--+--E   \n" +
            " [BBPP]   [Main Office]-----!            |      \n" +
            "                                         S        " )

formatX = "--------------------------------------------------------\n"

class Game:
    """
    The Game class organizes all game data in a central location.
    Usage:
    - Set up game using your choice of room configurations
      (TODO: Read these from a file in future)
    - call loop()
    """

    def __init__(self):
        """ Initialize object (with no rooms) """
        self.rooms = { } # stored in dictionary
        # Player is currently used to hold current location (loc)
        self.player = Player() 
        
        self.isPlaying = True
        self.isVerbose = True # auto-look on move
        

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def output(self, message):
        """ output the message. Just uses print() in base class.
        You might for example subclass to use Flask, etc. """
        print(message)

    def setup(self):
        """ setup(): create a graph of rooms for play. """
        # you MUST subclass Game and write your own setup()
        # see MyGame for an example.
        
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
        loc = APT12B
                
        return rooms
        
        

    def loop(self):
        """ loop(): the main game loop.
        Continues until the user quits. """
        self.isPlaying = True
        while self.isPlaying:
            self.playerAction()
        print("Game over, thanks for playing")
        


    def end(self):
        """ finish game, inform user of score and turns played. """
        pass
    
    def playerAction(self):
        """ Ask user for input, validate it, update the game state. """
        command = input("> ")
        #command = command.lower() # DONT DO IF EXITS HAVE CAPITALS!!!
        words = command.split() # split on whitespace
        if len(words) < 1:
            print("No input detected")
            return
        
        verb = words[0]
        if verb == "go":
            direction = words[1]
            self.commandGo(direction)    
        elif verb == "look":
            self.here.describe()
        elif verb == "quit":
            self.isPlaying = False
            print("quitting")
        elif verb == "get":
            item = words[1]
            self.commandGet(item)
        elif verb == "drop":
            item = words[1]
            self.commandDrop(item)
        
        else: # first word is verb
            print("I don't know how to", words[0])

    def commandGo(self, direction):
        """ 
        input: direction to move.
        output: none
        side effect: player location is updated if possible.
        """
                
        # Can we go in the chosen direction from here?
        if self.here.exits.get(direction) == None:
            print("You can't go that way.")
        else:   
            # this key does exist
            #print (formatX + " - Traveling " + direction + " from *TODO* DISPLAY PREVIOUS ROOM ..." + str(self.here))
            newRoomName = self.here.exits[direction]
            newRoom     = self.rooms[newRoomName]
            self.here   = newRoom
            if self.isVerbose:                
                print (formatX + " - Traveling " + direction + " from *TODO* DISPLAY PREVIOUS ROOM ...")
                print ("- You are now at " + (newRoomName) + "...")
                self.here.describe()
    
    def commandGet(self, itemName):
        """ remove the item from the room (if it's there)
        and place it in player inventory.
        """
        # TODO: actually do this
        # We'll need to remove the item from the current
        # room, and then add it to the player inventory
        # (which means we need a player inventory)
        print("You try to get the", itemName)

        
        if self.here.contains(itemName):
            item = self.here.contents[itemName]
            self.here.moveItemTo(item, self.player)
            print("You pick up the ",itemName,".")
        else:
            print("You can't see any", itemName, "here.")    

        
        
    def commandDrop(self, itemName):
        """ remove the item from player inventory
        (if it's there) and add it to the room. 
        """
        print("You try to drop the", itemName)
        
        if self.player.contains(itemName):
            item = self.player.contents[itemName]
            self.player.moveItemTo(item, self.here)
            print("You drop the", itemName,".")
        else:
            print("You don't have a", itemName, "to drop!")

    # Helper functions -- not necessary, but useful
    @property
    def here(self):
        return self.player.loc
    
    @here.setter
    def here(self, room):
        self.player.loc = room

def main():    
    game = Game()
    game.setup()
    print(formatX + "\t\tMacs Bork-Room Map\n" + formatX)
    print(mapM)  
    print("Starting game -- enter command.")
    game.loop()
    game.end()


if __name__ == "__main__":
    main()