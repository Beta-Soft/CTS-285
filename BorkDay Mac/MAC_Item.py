# CSC 221
# BorkDay Mac! - Text Adventure
# Rebecca Garcia

# Item class
# We'll put all our basic subclasses here

class BaseItem:
    """
    Items are found in rooms, or in the player inventory.
    (Possibly we'll change that to being found in Container objects?)
     
    They may be used to solve puzzles, give points to score, etc.
    
    This is the base class, which only supports get, drop, and examine
    """
     
    def __init__(self, name, description):
         self._name = name
         self._description = description
         
         # set basic flags
         self._canGet = True # default to gettable
#----------------------------------------------------------------------------------------------------------------------------
         
    def __str__(self):
        return self.name + " : " + self.description
#----------------------------------------------------------------------------------------------------------------------------
    
    @property
    def name(self):
        return self._name
#----------------------------------------------------------------------------------------------------------------------------
    
    @property
    def description(self):
        """return a decorated description. 
        Decoration = things like (too heavy to lift)""" 
        desc = self._description
        # decorate with extra info as needed
        if self.canGet == 1:
            desc += " It's too heavy to lift."
        if self.canGet == 2:
            desc += " NPC!"
        return desc
#----------------------------------------------------------------------------------------------------------------------------                 
                 
    @property 
    def canGet(self):
        """ True / False -- item can be picked up. """
        return self._canGet
    
    @canGet.setter 
    def canGet(self, setting):
        """ True / False - item can be picked up. """
        self._canGet = setting
#----------------------------------------------------------------------------------------------------------------------------
 
class Item (BaseItem):
     """
     This inherits from BaseItem. 
     We'll discuss how init(), etc. work as we go.
     """
     def __init__(self, name, description):
         # "super" runs the equiv function from the base class
         super().__init__(name, description)
#----------------------------------------------------------------------------------------------------------------------------         

class UsableItem (Item):
    """
    Works like a regular item, except that
    it has one or more usable verbs
    that will cause it to make changes.
    """    
    def __init__(self, name, description):
        super().__init__(name, description)
        # item is "unused" by default
        self._wasUsed = False
#----------------------------------------------------------------------------------------------------------------------------
        
    def use(self, useVerb = "use"):
        """
        use() - call to make the object 
        change to its other state.
        TODO: this needs more thought
        Parameters
        ----------
        useVerb : TYPE, optional
            DESCRIPTION. The default is "use".
        Returns
        -------
        None.
        """
        if self._wasUsed == True:
            print("You already used this item.")
        else:
            print("You attempt to",useVerb,"the item.")
            self._wasUsed = True
#----------------------------------------------------------------------------------------------------------------------------        
    
    @property
    def description(self):
        """return a decorated description. 
        Decoration = things like (too heavy to lift)
        This example just polishes the object.""" 
        desc = self._description
        # decorate with extra info as needed
        if self._wasUsed == True:
            desc += " It's very shiny."
        else:
            desc += " It's pretty rusty."
        return desc
#----------------------------------------------------------------------------------------------------------------------------    

# Test code
def main():
    #  items in APT12B
    MAC      = Item("Mac", "The king of the show, my reason, my love, my sweet doggo!\n" +
          "      fluffy smart loyal cute 9 yr old Aussie with a tail (: \n")
    MAC.canGet = 2
    
    leash    = Item("leash", "Snoppy themed decorated leash you found\n" +
          "      in the woods hiking, possibly a gift left behind by the forest fairies?\n")
    collar   = Item("collar", "Shiny studded collar with a nicely golden\n" +
          "      engraved nametag which reads MAC\n")
    keyCard  = Item ("key card", "small plastic card used instead of a door key,\n" +
          "      bearing magnetically encoded data which is read and processed by an electronic device\n")
    bandana  = Item ("lavender infused bandana", "scientifically proven aromatherapy to reduce stress, anxiety and overexcitement in dogs\n")
    
    # Pond
    squirrel = Item("squirrel", "slender body, bushy tail & large eyed\n" +
          "      rodents that Mac is sure are EVIL\n")
    
    # APT9C
    Coqui    = Item("Coqui", "Your SUPER (lol) annoyingly rude sibling who ironically loves \n" +
          "      your dog next to as close as you do, who you can trust to dogsit (in short intervals that is) -_-'\n")
    
    #MainOffice (key)
    cardScan = Item("Card Scanner", "data input device that reads data from your keycard which will allow entry to Main Office\n")
    Armando  = Item("Armando", "Super kind apt complex maintence guy who loves dogs and jokes\n")
    
    #BB&PP
    Odette   = Item("Odette", "Thors human, Armando's partner\n")
    Thor     = Item("Thor", "the kings best doggo Rottie friend, theyre basically brother\n")
    
#----------------------------------------------------------------------------------------------------------------------------      
    key = Item("key", "It's a bit rusty.\n")
    key.canGet = 2 # test
    
    sword = UsableItem("sword", "A short sword.\n")
    
    bed = Item("bed", "It's fluffy.\n")
    bed.canGet = 1 # can't lift the bed

    
    stuff = [MAC, leash, collar, keyCard, bandana, squirrel, Coqui, cardScan, 
             Armando, Odette, Thor, key, sword, bed]
    
# =============================================================================
#     for item in stuff:
#         print(item.name, "-", item.description)
# =============================================================================
        
    sword.use()
    for item in stuff:
        print(item.name, "-", item.description, )
#----------------------------------------------------------------------------------------------------------------------------
        
if __name__ == "__main__":
    main()