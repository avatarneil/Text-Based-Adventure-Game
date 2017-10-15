import sys
import numpy


class StdObject():

    def __init__(self, name, longDesc="", shortDesc=""):
        self.name = name
        self.longDesc = longDesc
        self.shortDesc = shortDesc

    def __str__(self):
        return "Name: {0}\nlongDesc: {1}\nshortDesc: {2}\n".format(self.name, self.longDesc, self.shortDesc)


class Living(StdObject):

    def __init__(self, name, longDesc = "", shortDesc = "",
                gender = "m", race = "Human"):
        super().__init__(name, longDesc, shortDesc)
        self.gender = gender
        self.race = race
        self.inventory = Container("{0}'s Inventory".format(self.name))

    def __str__(self):
        return "Name: {0}\longDesc: {1}\shortDesc: {2}\n"\
            "gender: {3}\race: {4}\n".format(
                self.name, self.longDesc, self.shortDesc, self.gender, self.race)


class Player(Living):
    
    def __init__(self, name, longDesc= "", shortDesc = "",
                gender = "", race = ""):
        super().init(name, longDesc, shortDesc, gender, race)


class Item(StdObject):

    def __init__(self, name, longDesc="", shortDesc=""):
        super().__init__(name, longDesc, shortDesc)

    def __str__(self):
        return super().__str__()


class Container(Item):

    def __init__(self, name, longDesc="", shortDesc=""):
        super().__init__(name, longDesc, shortDesc)
        self.inventory = []

    def __str__(self):
        return "Contasner"

    def add(self, item):
        self.inventory.push(item)
