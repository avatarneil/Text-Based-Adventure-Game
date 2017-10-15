import sys
import numpy

class StdObject():

    def __init__(self, name, longDesc="", shortDesc=""):
        self.name = name
        self.longDesc = longDesc
        self.shortDesc = shortDesc
    
    def __str__(self):
        return "\nName: {0}\nlongDesc: {1}\nshortDesc: {2}\n".format(self.name,self.longDesc,self.shortDesc)


class Item(StdObject):

    def __init__(self, name,longDesc="", shortDesc="", ownership=""):
        super().__init__(name, longDesc, shortDesc)
        self.ownership = ownership

    def __str__(self):
        return super().__str__()

class Container(Item):

    def __init__(self, name, longDesc="", shortDesc=""):
        super().__init__(name, longDesc, shortDesc)
        self.inventory = []
    
    def __str__(self):
        return "Container"



testStdObject = StdObject("Zac","An absolute nerd","Nerd")
testItem = Item("Sword","a glowing magic sword","magic sword")

print(testStdObject)
print(testItem)
