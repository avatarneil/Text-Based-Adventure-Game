import sys
import numpy


class StdObject():
    """ Base object from which all other objects derive from.
    Shoule never be used directly, only derived from. """

    def __init__(self, name, longDesc = "", shortDesc = ""):
        self.name = name
        self.longDesc = longDesc
        self.shortDesc = shortDesc

    def __str__(self):
        return "A StdObject called '{0}'".format(self.name)

    def __repr__(self):
        return "Name: {0}\nlongDesc: {1}\nshortDesc: {2}"\
               "\n".format(self.name, self.longDesc, self.shortDesc)


class Living(StdObject):
    """ Base class for all living things.
    Should never be used directly, only derived from. """

    def __init__(self, name, longDesc = "", shortDesc = "",
                 gender = "x", race = "human"):
        super().__init__(name, longDesc, shortDesc)
        self.gender = gender
        self.race = race
        self.inventory = Container("{0}'s Inventory".format(self.name))

    def __str__(self):
        return "A {0} {1} (Living) named '{2}'".format(self.get_gender(), self.race, self.name)

    def __repr__(self):
        return "Name: {0}\nlongDesc: {1}\nshortDesc: {2}\ngender: {3}\nrace: {4}".format(
               self.name, self.longDesc, self.shortDesc, self.gender, self.race)

    def get_gender(self):
        """ Returns 'Male', 'Female', or an empty string
        depending on the Living's gender (m/f/x). """

        return {'m':'male', 'f':'female', 'x':''}[self.gender]

    def get_pronoun(self):
        """ Returns 'he', 'she', or 'they' depending
        on the Living's gender (m/f/x). """

        return {'m':'he', 'f':'she', 'x':'they'}[self.gender]

    def give_item(self, item):
        """ Inserts the given item into this Living's inventory. """

        self.inventory.insert(item)

    def has_item(self, item) -> bool:
        """ Returns whether or not the Living currently has
        the specified item (true/false). """

        return self.inventory.has_item(item)


class Player(Living):
    """ Controls the Player and handles interaction. """

    def __init__(self, name, longDesc= "", shortDesc = "",
                 gender = "x", race = "human"):
        super().__init__(name, longDesc, shortDesc, gender, race)

    def __str__(self):
        return "A {0} {1} named {2}".format(self.get_gender(), self.race, self.name)

    def __repr__(self):
        return "Name: {0}\nlongDesc: {1}\nshortDesc: {2}\ngender: {3}\nrace: {4}".format(
            self.name, self.longDesc, self.shortDesc, self.gender, self.race)


class Item(StdObject):
    """ Generic base class for interactible items. """

    def __init__(self, name, longDesc="", shortDesc=""):
        super().__init__(name, longDesc, shortDesc)

    def __str__(self):
        return "A generic Item called '{0}'".format(self.name)

    def __repr__(self):
        return "Name: {0}\nlongDesc: {1}\nshortDesc: {2}"\
            "\n".format(self.name, self.longDesc, self.shortDesc)


class Container(Item):
    """ Game object that is used to store other objects. """

    def __init__(self, name, longDesc="", shortDesc=""):
        super().__init__(name, longDesc, shortDesc)
        self.inventory = []

    def __str__(self):
        return "A Container called '{0}'".format(self.name)

    def __repr__(self):
        return "Name: {0}\nlongDesc: {1}\nshortDesc: {2}"\
               "\n".format(self.name, self.longDesc, self.shortDesc)

    def show_contents(self):
        """ Prints the name of the container followed by
        it's contents, each in a new line. """

        print("Contents of {0}:".format(self.name))
        for item in self.inventory:
            print(item)

    def insert(self, item):
        """ Inserts the given item into the Container's inventory """

        self.inventory.append(item)

    def has_item(self, item) -> bool:
        """ Returns whether or not the Container currently contains
        the specified item. """

        return item in self.inventory

    def transfer_to(self, other, item):
        """ Transfers an item from this Container's inventory to another's. """

        if not self.has_item(item):
            return
        other.give_item(self.inventory.pop(item))


class Location(StdObject):
    """ Handles the contents of a certain game location. """

    def __init__(self, name, longDesc, shortDesc):
        super().__init__(self, name, longDesc, shortDesc)
        self.inventory = Container("{0} (Location)".format(self.name))

class Exit(Item):
    """ Exits handle moving the Player from one Location to another. """

    def __init__(self, name, longDesc, shortDesc):
        super().__init__(self, name, longDesc, shortDesc)
        self.destination = None



def test_suite():
    testStdObject = StdObject("object", "a nonspecific generic object", "a generic object")
    testLiving = Living("living thing", "a living, breathing being", "a living thing")
    testPlayer = Player("Zac", "the star of the show", "you")
    testItem = Item("item", "just a random item lying around", "an item")
    testContainer = Container("container", "a container for holding items", "a container")

    #print(testStdObject)
    #print(testLiving)
    print(testPlayer)
    print(testItem)
    print(testContainer)
    print("")

    testPlayer.inventory.show_contents()
    print("")

    print(testPlayer.has_item(testItem))
    testPlayer.give_item(testItem)
    print(testPlayer.has_item(testItem))
    print("")

    testPlayer.inventory.show_contents()

test_suite()
print(testStdObject)
