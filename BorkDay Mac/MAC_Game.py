# CSC 221
# BorkDay Mac! - Text Adventure
# Rebecca Garcia
import sys, time

from  MAC_Player import Player
##from  MAC_MyGame import startRoom


mapM = ("[*APT12B*]-----[Pond]-----[APT9C]            N      \n" +
            "    |            |          |            |      \n" +
            "    |            |          |         W--+--E   \n" +
            " [BBPP]   [Main Office]-----!            |      \n" +
            "                                         S        " )
formatX = "--------------------------------------------------------\n"
#----------------------------------------------------------------------------------------------------------------------------

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
#----------------------------------------------------------------------------------------------------------------------------

    def __str__(self):
        pass
#----------------------------------------------------------------------------------------------------------------------------

    def __repr__(self):
        pass
#----------------------------------------------------------------------------------------------------------------------------

    def output(self, message):
        """ output the message. Just uses print() in base class.
        You might for example subclass to use Flask, etc. """
        print(message)
#----------------------------------------------------------------------------------------------------------------------------
        
    def loop(self):
        """ loop(): the main game loop.
        Continues until the user quits. """
        self.isPlaying = True
        while self.isPlaying:
            self.playerAction()
        print("Game Over! (in Mac_Game def loop)\n")
        time.sleep(1)
        
        self.playAgain()
        
        
    def playAgain(self): #playagain FUNCTION   
        print("Would you like to play again? (in Mac_Game def playAgain)")
        answer = input("> ")
        if answer == "yes":
            print("restarting game...")
            time.sleep(1)
            # To restart, do what we did in main -- setup() then loop()
            self.setup()
            self.loop()
            
            
            
        else:
            print("Thanks for playing (:")
    
        
#----------------------------------------------------------------------------------------------------------------------------
        
    def end(self):
        """ finish game, inform user of score and turns played. """
        pass
#----------------------------------------------------------------------------------------------------------------------------
    
    def playerAction(self):
        """ Ask user for input, validate it, update the game state. """
        command = input("> ")
        #command = command.upper().lower() # DONT DO IF EXITS HAVE CAPITALS!!!
        words = command.split() # split on whitespace
        if len(words) < 1:
            print("No input detected (in Mac_Game def playAction)")
            return
        
        verb = words[0].upper()
        if verb == "GO":
            direction = words[1]
            self.commandGo(direction)    
        elif verb == "LOOK":
            print("You are currently in...")
            self.here.describe()
        elif verb == "QUIT":
            self.isPlaying = False
            print("quitting")
        elif verb == "GET":
            item = words[1]
            self.commandGet(item)
        elif verb == "DROP":
            item = words[1]
            self.commandDrop(item)
        elif verb == "HELP":
            print("- Start commands with words such as...\n" +
                  "\t\t - GO   \n" +
                  "\t\t - GET  \n" +
                  "\t\t - LOOK \n" +
                  "\t\t - DROP \n" +
                  "\t\t - VIEW \n" +
                  "\t\t - QUIT   " )
        
        else: # first word is verb
            print("I don't know how to", words[0])
#----------------------------------------------------------------------------------------------------------------------------

    def commandGo(self, direction):
        """ 
        input: direction to move.
        output: none
        side effect: player location is updated if possible.
        """
        
        # Special case - you can't leave a room if you have Mac but don't 
        # have his leash
        if self.player.contains("Mac") == True:
            if self.player.contains("leash") == False:
                print("Good luck getting Mac to follow without the leash...")
                return # don't move at all
            
        if self.player.contains("Mac") == True:
            if self.player.contains("leash") == True and self.player.contains("collar") == False:
                print("Oh no! Mac slips out of leash")
                print("If only he had his collar....")
                self.isPlaying = False
                return # don't move at all
            
        if self.player.contains("Mac") == True:
            if self.player.contains("leash") == True and self.player.contains("collar") == True:
                    print("OK, Mac's got his collar and his leash.")
                    # movement is now OK
                    
        
        
        # Can we go in the chosen direction from here?
        if self.here.exits.get(direction) == None:
            print("You can't go that way.")
            return
        else:   
            # this key does exist
            #print (formatX + " - Traveling " + direction + " from *TODO* DISPLAY PREVIOUS ROOM ..." + str(self.here))
            newRoomName = self.here.exits[direction]
            newRoom     = self.rooms[newRoomName]
            oldRoom = self.here
            self.here   = newRoom
            if self.isVerbose:                
                print (formatX + " - Traveling " + direction + " from " + oldRoom.name)
                print ("- You are now at " + (newRoomName) + "...")
                self.here.describe()
#----------------------------------------------------------------------------------------------------------------------------
    
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
            print("You pick up the",itemName,".")
        else:
            print("You can't see any", itemName, "here.")      
#----------------------------------------------------------------------------------------------------------------------------
        
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
#----------------------------------------------------------------------------------------------------------------------------

def main():
    game = Game()
    game.setup()
    print("Starting game -- enter command.")
    game.loop()
    game.end()


if __name__ == "__main__":
    main()