"""
Text Based Adventure Game Engine (tbag.py)
A set of classes and methods for creating
player-driven text-based experiences.
"""

import sys
import itertools

#pylint: disable=too-many-arguments
#pylint: disable=too-few-public-methods


class Lang():
    """ Language class that has methods for nice output. """

    @classmethod
    def a(cls, thing) -> str:
        """ Returns 'an' if thing starts with a vowel,
        otherwise returns 'a'. """

        if not thing:
            return
        return 'an ' + thing if thing[0] in ['a', 'e', 'i', 'o', 'u'] else 'a ' + thing

    @classmethod
    def A(cls, thing) -> str:
        """ Returns 'An' if thing starts with a vowel,
        otherwise returns 'A'. """

        return Lang.a(thing).capitalize()

    @classmethod
    def gender(cls, living) -> str:
        """ Returns 'Male', 'Female', or an empty string
        depending on the given Living's gender (m/f/x/n). """

        return {'m': 'male', 'f': 'female', 'x': '', 'n': ''}[living.gender]

    @classmethod
    def pronoun(cls, living) -> str:
        """ Returns 'he', 'she', 'they', or 'it' depending
        on the given Living's gender (m/f/x/n). """

        return {'m': 'he', 'f': 'she', 'x': 'they', 'n': 'it'}[living.gender]

    @classmethod
    def prettify(cls, phrase) -> str:
        """ Nicely formats and returns a given string. """

        if type(phrase) is not str:
            try:
                phrase = str(phrase)
            except AttributeError:
                return "phrase is not parsable as a string"

        if phrase[len(phrase) - 1].isalnum():
            phrase = phrase + '.'

        split = phrase.split(' ')

        contractions_bad = ["doesnt", "wont", "cant"]
        contractions_good = ["doesn't", "won't", "can't"]

        for i, word in enumerate(split):
            if i == 0 or split[i - 1][-1] == '.':  # if it's the first word in a
                split[i] = word.capitalize()  # sentence, capitalize it
            if word in contractions_bad:
                split[i] = contractions_good[contractions_bad.index(word)]

        return ' '.join(split)

class Console():
    """ Console handles player input and printing messages
    to the player. """

    @classmethod
    def tell(cls, msg):
        """ Prints a message to the player, followed by
        a blank line. """

        sys.stdout.write("{0}\n\n".format(msg))

    @classmethod
    def say(cls, name, msg):
        """ Tells the player that an actor with the given
        name said the given message. """

        sys.stdout.write("{0} says, \"{1}\"\n".format(name, msg))
    
    @classmethod
    def debug(cls, msg):
        """ Prints a debug message only if the script was
        run with the debug parameter. """

        if len(sys.argv) > 1 and sys.argv[1] in ['-d','-debug']:
            sys.stdout.write(">{0}\n".format(msg))

    @classmethod
    def prettyprint(cls, msg):
        """ Prints a message after running it through the
        Lang.prettify() method. """

        sys.stdout.write("{0}\n".format(Lang.prettify(msg)))

    @classmethod
    def input(cls):
        """ Gets a command from the player and passes it to
        the input parser. """

        cmd = input('\n')
        world.parse_input(cmd)


class StdObject():
    """ Base object from which all other objects derive from.
    Should never be used directly. """

    def __init__(self, name="no_name", location="limbo"):
        self.name = name
        self.aliases = [self.name]
        self.description = None
        self.location = location
        self.actions = {}
        self.base_actions = {
            "examine": ["examine", "look", "analyze"]
        }
        self.description = ""

        world.add(self, location)

    def __str__(self):
        return "a StdObject called '{0}'".format(self.name)

    def __repr__(self):
        return "StdObject\nName: {0}\nDescription: {1}\nLocation: {2}"\
               "\n".format(self.name, self.description, self.location)

    def set_desc(self, new_desc):
        """ Sets a new description for the object. """
        self.description = new_desc

    def add_alias(self, new_alias):
        """ Add an alias or aliases depending on if passed
        a string or a list. """

        if type(new_alias) == type(['list']):
            self.aliases += new_alias
        elif type(new_alias) == type('string'):
            self.aliases.append(new_alias)
        else:
            raise(TypeError("New alias must be list or string."))
    
    def has_action(self, act_name) -> bool:
        """ Returns whether or not the specified action can
        be performed on this object (True/False). """

        if act_name in list(itertools.chain.from_iterable(self.actions.values())):
            return True
        elif act_name in list(itertools.chain.from_iterable(self.base_actions.values())):
            return True
        return False
    
    def id_action(self, act_name):
        all_actions = {**self.base_actions, **self.actions}

        for action, aliases in all_actions.items():
            for name in aliases:
                if name == act_name:
                    return action

    def execute(self, act_name, doer):
        """ Executes an action performed by the given
        living. """

        Console.debug("Executing action: {0} | target: {1} | doer: {2}".format(act_name, self.name, doer))

        if self.id_action(act_name) == "examine":
            if not self.description:
                Console.tell("The {0} doesn't have a description.".format(self.name))
            else:
                Console.prettyprint(self.description)


class Living(StdObject):
    """ Base class from which all living things derive from. """

    def __init__(self, name, location="limbo"):
        super().__init__(name, location)
        self.gender = "x"
        self.race = "human"
        self.inventory = Container("{0}'s inventory".format(self.name))

    def __str__(self):
        return Lang.a("{0} {1} Living named '{2}'".format(Lang.gender(self), self.race, self.name))

    def __repr__(self):
        return "Living\nName: {0}\ndescription: {1}\ngender: {2}\nrace: {4}".format(
            self.name, self.description, self.gender, self.race)

    def give_item(self, item):
        """ Inserts the given item into this Living's
        inventory. """

        self.inventory.add_item(item)

    def has_item(self, item) -> bool:
        """ Returns whether or not this Living currently
        has the specified item (True/False). """

        return self.inventory.has_item(item)

    def say(self, msg):
        """ Tells the player that this living said the
        given message. """

        Console.say(self.name, msg)
    
    def do_action(self, action, target=None):
        """ Executes the given action on the given target,
        if possible, otherwise prints an error message. """
        if not target:
            Console.tell("That doesn't make any sense.")
        elif not self.location == target.location:
            Console.tell("You don't see a {0} anywhere.".format(target.name))
            return False
        elif not target.has_action(action):
            Console.tell("You can't {0} the {1}.".format(action, target.name))
            return False
        else:
            target.execute(action, self)


class Player(Living):
    """ Stores data relevant to the Player. """

    def __init__(self, name, location="limbo"):
        super().__init__(name, location)
        self.add_alias(["me","myself"])

    def __str__(self):
        return Lang.a("{0} {1} Player named '{2}'".format(Lang.gender(self), self.race, self.name))

    def __repr__(self):
        return "Player\nName: {0}\description: {1}\ngender: {2}\nrace: {3}".format(
            self.name, self.description, self.gender, self.race)


class Item(StdObject):
    """ Generic base class for interactible items. """

    def __init__(self, name, location="limbo", value=0):
        super().__init__(name, location)
        self.value = value
        self.actions = {
            "pickup": ["pickup","take","grab"]
        }

    def __str__(self):
        return "an Item called '{0}'".format(self.name)

    def __repr__(self):
        return "Item\nName: {0}\description: {1}"\
            "\n".format(self.name, self.description)
    
    def execute(self, action, doer):
        """ Executes the given action performed by the
        given living. """

        super().execute(action, doer)
        if action == "pickup":
            doer.give_item(self)
            world.remove(self)
            return True


class Container(Item):
    """ Game object that is used to store other objects. """

    def __init__(self, name, location="limbo"):
        super().__init__(name, location)
        self.contents = []

    def __str__(self):
        return "a Container called '{0}'".format(self.name)

    def __repr__(self):
        return "Container\nName: {0}\description: {1}"\
               "\n".format(self.name, self.description)

    def show_contents(self):
        """ Prints the name of the container followed by
        its contents, each in a new line. """

        if not self.contents:
            Console.tell(Lang.prettify("{0} is empty.".format(self.name)))
            return

        Console.tell("Contents of {0}:".format(self.name))
        for item in self.contents:
            Console.prettyprint(item)

    def add_item(self, item):
        """ Inserts the given item into the Container's
        inventory. """

        self.contents.append(item)

    def has_item(self, item) -> bool:
        """ Returns whether or not the Container currently contains
        the specified item (True/False). """

        return item in self.contents

    def transfer_to(self, other, item) -> bool:
        """ Transfers an item from this Container's
        inventory to another's. Returns True if successful,
        otherwise returns False. """

        if not self.has_item(item):
            return False

        try:
            other.give_item(self.contents.pop(self.contents.index(item)))
            return True
        except ValueError:
            return False

class World():
    """ Everything in the game is connected to
    everything else via the World space. """

    def __init__(self):
        self.tickspeed = 1000 # game heartbeat in ms
        self.locations = {}
        self.player = None

    def add(self, objs, loc):
        """ Adds an object into the world space at the
        given location. """

        if not loc in self.locations.keys():
            self.locations[loc] = []
        
        if not type(objs) is type([]):
            objs = [objs]
    
        for obj in objs:
            if type(obj) is Player:
                self.player = obj
            else:
                world.locations[loc].append(obj)
        
        Console.debug("Added {0} objects to {1}".format(
            len(objs), loc))
    
    def remove(self, obj, loc):
            self.locations[loc].remove(obj)
    
    def move(self, obj, new_loc):
        """ Pops an obj from its old location into the new
        location. """

        if not new_loc in self.locations.keys():
            self.add_loc(new_loc)
        
        self.locations[new_loc].append(self.locations[obj.location].pop(obj))

        obj.location = new_loc
    
    def add_loc(self, loc_name, loc_desc="no description given"):
        """ Adds the given location to the world. """
        self.locations[loc_name] = []

    def get_keywords(self, loc, type="both"):
        """ Returns a list of all valid keywords for the
        given location. """

        keywords = []
        for obj in self.locations[loc]:
            if not type == "actions":
                keywords += obj.aliases
            for act in obj.actions.values():
                if not type == "things":
                    keywords += act
            for act in self.player.base_actions.values():
                if not type == "things":
                    keywords += act
        
        #Console.debug("Keywords for {0}: {1}".format(loc, keywords))
        return keywords

    def parse_input(self, input_data):
        """ Takes inputs and attempts to execute a command. """

        if type(input_data) is not str:
            try:
                input_data = str(input_data)
            except AttributeError:
                return "input_data is not parseable as a string"

        keywords = self.get_keywords(self.player.location)
        input_words = input_data.split(' ')
        valid_words = [w for w in input_words if w in keywords]

        Console.debug("valid_words: {0}".format(valid_words))

        if not valid_words:
            Console.tell("That's not possible.")
        elif len(valid_words) == 1:
            self.player.do_action(self.match(valid_words[0]))
        elif len(valid_words) > 1:
            self.player.do_action(self.match(valid_words[0]), self.match(valid_words[1]))

    '''def get_matches(self, wds, loc):
        
        keywds = self.get_keywords(loc)
        if not type(wds) is type([]):
            wds = wds.split()

        results = {}

        for i, wd in enumerate(wds):
            match = ""
            if wd in keywds:
                for obj in self.locations[loc]:
                    if wd in obj.aliases:
                        match = obj
                if not match:
                    match = wd
            results[i] = match
        
        Console.debug("Best match result: {0}".format(results))
        return results'''
    
    def match(self, wd):
        Console.debug("Finding match for: {0}".format(wd))
        loc = self.player.location
        
        things = self.get_keywords(loc, 'things')
        actions = self.get_keywords(loc, 'actions')

        if wd in things:
            for obj in self.locations[loc]:
                if wd in obj.aliases:
                    Console.debug("Obj match found: {0}".format(obj))
                    return obj
        elif wd in actions:
            Console.debug("Action match found: {0}".format(wd))
            return wd
        else:
            Console.debug("No match found for {0}".format(wd))
            return 'not_found'

world = World()
