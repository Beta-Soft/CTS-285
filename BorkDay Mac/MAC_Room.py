# CSC 221
# BorkDay Mac! - Text Adventure
# Rebecca Garcia

from  MAC_Item import Item
from  MAC_Container import Container

class Room(Container):
    """
    The Room class holds names, descriptions, and exits.
    In future it should also manage objects in rooms, somehow
    """
        
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits
        self.contents = {} # used by container
#----------------------------------------------------------------------------------------------------------------------------

    def __str__(self):
        """ contains the name, description, and exits in a human-readable fashion"""
        text = self.name + "\n"
        text += self.description + "\n"
        # append all exits
        exitList = self.exits.keys() # this gives us a list of all directions ipresent in exits
        for direction in exitList:
            text += " - " + direction                     # North, South, East, West 
            text += ": " + self.exits[direction]  # prints in format "North: Living Room", etc.
            text += "\n"
        # print items in room, if any
        text += "**Here you see** \n"
        text += self.listContents()
        return text
#----------------------------------------------------------------------------------------------------------------------------

    def describe(self):
        """ print full room description. """
        print(self)
#----------------------------------------------------------------------------------------------------------------------------
    
    def exit(self, direction):
        """
        input: an exit direction, as string
        output: a Room object - either the room the player
            has moved to, or the current room if
            movement failed.
        """   
        pass 
        # I need access to the roomDict for this -- so it should 
        # go in Game, not Room.
#----------------------------------------------------------------------------------------------------------------------------             
            
    def addItem(self, item):
        """ used to add an item into a room. """
        self.add(item)
#----------------------------------------------------------------------------------------------------------------------------
    
    def removeItem(self, item):
        """ used to remove items from a room. """
        self.remove(item)
#----------------------------------------------------------------------------------------------------------------------------        
        
def main():
    """
    Currently used for testing.
    TODO: implement doctests. """
    APT12B      = Room ( "APT12B",
                         " Cozy third floor apartment overlooking pond. Floor to ceiling windows decorated with\n" +
                         "string lights. You and Macs safe haven.",
                        {"East"  : "Pond",
                         "South" : "BBPP" })
    
    Pond        = Room ( "Pond",
                         " Complex pond full of life! Ducks, geese, squirrels, benches shaded by tall, lush, palm\n" + 
                         "and live oak trees covered in spanish moss.",
                        {"East"  : "APT9C",
                         "South" : "MainOffice",
                         "West"  : "APT12B" })
    
    APT9C       = Room ( "APT9C",
                         " Younger brothers second floor apt. Shelves filled with POP!s. 3D printer half way\n" + 
                         "installed sits on desk. Doggie bowls in corner",
                        {"West"  : "Pond",
                         "South" : "MainOffice" })
    
    MainOffice  = Room ( "MainOffice",
                         " Next to the gym. Overlooking pool area. Hub to centralized unit of individually locked\n" + 
                         "compartments for the delivery and collection of mail.",
                        {"North" : "Pond",
                         "East"  : "APT9C" })
    
    BBPP        = Room ( "BBPP",
                         " Brohard Paw Park and Doggie Beach. Next to Venice Municipal Airport. A marvelous sight of \n" +
                         "happy doggos, clear, calm waters and the occassional plane flying right above.",
                        {"North" : "APT12B" } )
        
    # Place rooms in a dictionary.
    # (Game will handle this in the full version)
    roomDict = { APT12B.name: APT12B, 
                Pond.name: Pond,
                APT9C.name: APT9C,
                MainOffice.name: MainOffice,
                BBPP.name: BBPP}
    
    
    # Test out items
    
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
    
    # Test out movement
    formatX = "--------------------------------------------------------\n"
    print(formatX + "\t\tMacs Bork-Room Map\n" + formatX)
    print("[*APT12B*]-----[Pond]-----[APT9C]        N     \n" +
          "    |            |          |            |     \n" +
          "    |            |          |         W--+--E  \n" +
          " [BBPP]   [Main Office]-----!            |     \n" +
          "                                         S       ")    
    print(formatX +"\t\tMacs Bork-Room WalkThru\n" + formatX)
    
    loc = APT12B
    print("Starting room:")
    loc.describe()
    
    print (formatX + " - Traveling East from " + loc.name + "...")    #Newly Visted
    loc = roomDict[loc.exits["East"]] # find room to East, go there    (@POND)
    print ("- You are now at " + (loc.name) + "...")
    loc.describe()
    
    print (formatX + " - Traveling East from " + loc.name + "...")    #Newly Visted
    loc = roomDict[loc.exits["East"]] # find room to East, go there    (@APT9C)
    print ("- You are now at " + (loc.name) + "...")
    loc.describe()    
    
    print (formatX + " - Traveling South from " + loc.name + "...")   #Newly Visted
    loc = roomDict[loc.exits["South"]] # find room to South, go there  (@MainOffice)
    print ("- You are now at " + (loc.name) + "...")
    loc.describe()
    
    print (formatX + " - Traveling East from " + loc.name + "...")    #Previosuly Visted
    loc = roomDict[loc.exits["East"]] # find room to East, go there    (@APT9C)
    print ("- You are now BACK at " + (loc.name) + "...")
    loc.describe()
    
    print (formatX + " - Traveling West from " + loc.name + "...")    #Previously Visted
    loc = roomDict[loc.exits["West"]] # find room to West, go there    (@Pond)
    print ("- You are now BACK at " + (loc.name) + "...")
    loc.describe()
    
    print (formatX + " - Traveling West from " + loc.name + "...")    #Previously Visted
    loc = roomDict[loc.exits["West"]] # find room to West, go there    (@APT12B)
    print ("- You are now BACK at " + (loc.name) + "...")
    loc.describe()
    
    print (formatX + " - Traveling South from " + loc.name + "...")   #Newly Visted
    loc = roomDict[loc.exits["South"]] # find room to South, go there  (@BBPP)
    print ("- You are now at " + (loc.name) + "...")
    loc.describe()
    
    print (formatX + " - Traveling North from " + loc.name + "...")   #Previously Visted
    loc = roomDict[loc.exits["North"]] # find room to South, go there  (@APT12B)
    print ("- You are now BACK at " + (loc.name) + "...")
    loc.describe()
#----------------------------------------------------------------------------------------------------------------------------   

if __name__ == "__main__":
    main()