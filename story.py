import sys
import numpy


class StdObject():

    def __init__(self, name, longDesc="", shortDesc=""):
        self.name = name
        self.longDesc = longDesc
        self.shortDesc = shortDesc
    
    def __str__(self):
        return "A StdObject called '{0}'.".format(self.name)

    def __repr__(self):
        return "Name: {0}\nlongDesc: {1}\nshortDesc: {2}"\
            "\n".format(self.name, self.longDesc, self.shortDesc)


class Living(StdObject):

    def __init__(self, name, longDesc = "", shortDesc = "",
                gender = "x", race = "human"):
        super().__init__(name, longDesc, shortDesc)
        self.gender = gender
        self.race = race
        self.inventory = Container("{0}'s Inventory".format(self.name))
    
    def __str__(self):
        return "A Living named '{0}'.".format(self.name)

    def __repr__(self):
        return "Name: {0}\nlongDesc: {1}\nshortDesc: {2}\ngender: {3}\nrace: {4}".format(
                    self.name, self.longDesc, self.shortDesc, self.gender, self.race)
    
    def pronoun(self):
        return {'m':'he', 'f':'she', 'x':'they'}[self.gender]

    def give(self, item):
        self.inventory.add(item)


class Player(Living):
    
    def __init__(self, name, longDesc= "", shortDesc = "",
                gender = "x", race = "human"):
        super().__init__(name, longDesc, shortDesc, gender, race)
    
    def __str__(self):
        return "A Player named '{0}'.".format(self.name)

    def __repr__(self):
        return "Name: {0}\nlongDesc: {1}\nshortDesc: {2}\ngender: {3}\nrace: {4}".format(
                    self.name, self.longDesc, self.shortDesc, self.gender, self.race)


class Item(StdObject):

    def __init__(self, name, longDesc="", shortDesc=""):
        super().__init__(name, longDesc, shortDesc)
    
    def __str__(self):
        return "An Item called '{0}'.".format(self.name)

    def __repr__(self):
        return "Name: {0}\nlongDesc: {1}\nshortDesc: {2}"\
            "\n".format(self.name, self.longDesc, self.shortDesc)


class Container(Item):

    def __init__(self, name, longDesc="", shortDesc=""):
        super().__init__(name, longDesc, shortDesc)
        self.inventory = []
    
    def __str__(self):
        return "A Container called '{0}'.".format(self.name)

    def __repr__(self):
        return "Name: {0}\nlongDesc: {1}\nshortDesc: {2}"\
            "\n".format(self.name, self.longDesc, self.shortDesc)

    def add(self, item):
        self.inventory.append(item)


def test_suite():
    testStdObject = StdObject("object", "a nonspecific generic object",  "a generic object")
    testLiving = Living("living thing", "a living, breathing being", "a living thing")
    testPlayer = Player("Zac", "the star of the show", "you")
    testItem = Item("item", "just a random item lying around", "an item")
    testContainer = Container("container", "a container for holding items", "a container")

    print(testStdObject)
    print(testLiving)
    print(testPlayer)
    print(testItem)
    print(testContainer)

    print(repr(testPlayer))
    print(testPlayer.pronoun())
    testPlayer.give(testItem)

test_suite()