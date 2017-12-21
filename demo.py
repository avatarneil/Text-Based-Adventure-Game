"""
A demo project for the Text Based Adventure Game module.
To play, simply run 'python demo.py' from terminal.
"""

import tbag

class Note(tbag.Item):
    def __init__(self, name, location="limbo"):
        super().__init__(name, location)
        self.text = ["note placeholder text"]
        self.actions = {
            "read": ["read"],
            "destroy": ["destroy", "toss"]
        }
    
    def set_text(self, lines):
        self.text = lines
    
    def execute(self, act_name, doer):
        super().execute(act_name, doer)
        
        if self.id_action(act_name) == "read":
            print("The note reads as follows.\n")
            for line in self.text:
                print("  {0}".format(line))
        elif self.id_action(act_name) == "destroy":
            tbag.Console.tell("You toss the note in the trash can. Out of sight, out of mind.")
            tbag.world.remove(self)


class Customer(tbag.Living):
    def __init__(self, name, location="limbo"):
        super().__init__(name, location)
        self.appearance = {
            'clothes': "t-shirt annd jeans",
            'details': "",
            'accessory': "",
        }

player = tbag.Player("Joe Schmoe", "starbucks")

jake = Customer("Jake from Statefarm", "starbucks")
jake.add_alias("jake")
jake.appearance['clothes'] = "a red polo and khakis"

cia = Customer("CIA Agent", "starbucks")
cia.add_alias(["agent","businessman"])
cia.appearance['clothes'] = "a suit"
cia.appearance['accessory'] = "dark sunglasses and an earpiece"

note = Note("mysterious note", "starbucks")
note.add_alias(["note", "letter", "paper"])
note.set_text(["Dear {0},".format(tbag.world.player.name),"",
                 "You have been selected from a pool of over 1000 candidates",
                 "to perform a top secret mission. Your mission, should you",
                 "choose to accept it, is of utmost importance to national",
                 "security. However, we cannot share more details unless you",
                 "are willing to cooperate. If you accept this mission, leave",
                 "the cafe through the back door and wait for further",
                 "instructions in the alleyway.","",
                 "Please hurry. Time is of the essence.","",
                 "                                          -A friend"])
note.set_desc("a handwritten note on a small square of white paper. "\
              "You should probably read it.")

coffee = tbag.Item("coffee", "starbucks")
coffee.add_alias(["chai", "latte"])
coffee.set_desc("a decaf chai tea latte")

while True:
    tbag.Console.input()