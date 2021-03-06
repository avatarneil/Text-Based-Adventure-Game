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
            "read": ["read", "look", "examine"],
            "destroy": ["destroy", "trash", "throw", "toss", "ignore"]
        }
    
    def set_text(self, lines):
        self.text = lines
    
    def do_action(self, action_name, doer):
        tbag.Console.debug("{0} doing action {1} from doer {2}".format(self.name, action_name, doer))
        do = "nothing"
        for actions in self.actions.values():
            for a in actions:
                if a == action_name:
                    do = a
        
        if do == "read":
            print("\n")
            for line in self.text:
                print(line)
            print("\n")
        elif do == "destroy":
            tbag.Console.tell("You toss the letter in the trash can. Out of sight, out of mind.")
            del tbag.world.population[self.name]
        elif do == "nothing":
            tbag.Console.tell("You can't {0} the {1}.".format(action_name, self.name))


class Customer(tbag.Living):
    def __init__(self, name, location="limbo"):
        super().__init__(name, location)
        self.appearance = {
            hair: "brown",
            eyes: "brown",
            shirt: "blue t-shirt",
            pants: "khakis",
            other: "",
        }


tbag.world.add_loc("starbucks", "the small Starbucks cafe where you've worked"\
                   "for the past two months")

player = tbag.Player("Joe Schmoe", "starbucks")

jake = tbag.Living("Jake from Statefarm", "starbucks")
jake.add_alias("jake")

cia = tbag.Living("CIA Agent", "starbucks")
cia.add_alias(["agent","spy"])

note = Note("mysterious note")
note.add_alias(["note","letter","message","paper"])
note.set_text(["Dear {0},".format(tbag.world.player.name),"",
                 "You have been selected from a pool of over 1000 candidates",
                 "to perform a top secret mission. Your mission, should you",
                 "choose to accept it, is of utmost importance to national",
                 "security. However, we cannot share more details unless you",
                 "are willing to cooperate. If you accept this mission, leave",
                 "the cafe through the back door and rendezvous with your",
                 "handler in the alleyway immediately.","",
                 "Please hurry. Time is of the essence.","",
                 "                                          -A friend"])
cia.give_item(note)

coffee = tbag.Item("decaf chai latte", "starbucks")
coffee.add_alias(["coffee","decaf","chai","latte"])

while True:
    tbag.Console.input()