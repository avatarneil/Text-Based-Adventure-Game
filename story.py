import sys
import numpy

class StdObject():

    def __init__(self,name,longDesc="",shortDesc=""):
        self.name = name
        self.longDesc = longDesc
        self.shortDesc = shortDesc
    
    def __str__(self):
        return "Name: {0}\nlongDesc: {1}\nshortDesc: {2}\n".format(self.name,self.longDesc,self.shortDesc)


#class Living(StdObject):

test = StdObject("Zac","An absolute nerd","Nerd")

print(test)