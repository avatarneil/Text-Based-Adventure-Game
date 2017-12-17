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
    """ Console handles player input and printing
    messages to the player. """

    @classmethod
    def tell(cls, msg):
        sys.stdout.write("{0}\n".format(msg))

    @classmethod
    def prettyprint(cls, msg):
        sys.stdout.write("{0}\n".format(Lang.prettify(msg)))

    @classmethod
    def input(cls):
        cmd = input()
        cmd_parsed = world.parse_input(cmd)
        world.execute(cmd_parsed)


class StdObject():
    """ Base object from which all other objects derive from.
    Should never be used directly. """

    def __init__(self, name, location="limbo"):
        self.name = name
        self.aliases = [self.name]
        self.location = location
        self.description = ""

        world.add(self)

    def __str__(self):
        return "a StdObject called '{0}'".format(self.name)

    def __repr__(self):
        return "StdObject\nName: {0}\Description: {1}\Location: {2}"\
               "\n".format(self.name, self.description, self.location)

    def set_desc(self, new_desc):
        self.description = new_desc

    def add_alias(self, new_alias):
        if type(new_alias) == type(['list']):
            self.aliases += new_alias
        elif type(new_alias) == type('string'):
            self.aliases.append(new_alias)
        else:
            raise(TypeError("New alias must be list or string."))

    def do_action(self, action, doer, target):
        # TODO: handle actions
        pass


class Living(StdObject):
    """ Base class from which all living things derive from.
    Should never be used directly. """

    def __init__(self, name, location="limbo"):
        super().__init__(name, location)
        self.gender = "x"
        self.race = "human"
        self.inventory = Container("{0}'s inventory".format(self.name))

    def __str__(self):
        return Lang.a("{0} {1} Living named '{2}'".format(Lang.gender(self), self.race, self.name))

    def __repr__(self):
        return "Living\nName: {0}\description: {1}\location: {2}\ngender: {3}\nrace: {4}".format(
            self.name, self.description, self.location, self.gender, self.race)

    def give_item(self, item):
        """ Inserts the given item into this Living's inventory. """

        self.inventory.add_item(item)

    def has_item(self, item) -> bool:
        """ Returns whether or not this Living currently has
        the specified item (True/False). """

        return self.inventory.has_item(item)

    def say(self, msg):
        Console.tell("{0} says, \"{1}\"".format(self.name, msg))


class Player(Living):
    """ Controls the Player and handles interaction. """

    def __init__(self, name, location="limbo"):
        super().__init__(name, location)
        self.add_alias(["me","myself"])

    def __str__(self):
        return Lang.a("{0} {1} Player named '{2}'".format(Lang.gender(self), self.race, self.name))

    def __repr__(self):
        return "Player\nName: {0}\description: {1}\location: {2}\ngender: {3}\nrace: {4}".format(
            self.name, self.description, self.location, self.gender, self.race)


class Item(StdObject):
    """ Generic base class for interactible items. """

    def __init__(self, name, location="limbo", value=0):
        super().__init__(name, location)
        self.value = value

    def __str__(self):
        return "an Item called '{0}'".format(self.name)

    def __repr__(self):
        return "Item\nName: {0}\description: {1}\location: {2}"\
            "\n".format(self.name, self.description, self.location)


class Container(Item):
    """ Game object that is used to store other objects. """

    def __init__(self, name, location="limbo"):
        super().__init__(name, location)
        self.contents = []

    def __str__(self):
        return "a Container called '{0}'".format(self.name)

    def __repr__(self):
        return "Container\nName: {0}\description: {1}\location: {2}"\
               "\n".format(self.name, self.description, self.location)

    def show_contents(self):
        """ Prints the name of the container followed by
        its contents, each in a new line. """

        if not self.contents:
            print(Lang.prettify("{0} is empty.".format(self.name)))
            return

        print("Contents of {0}:".format(self.name))
        for item in self.contents:
            print(Lang.prettify(item))

    def add_item(self, item):
        """ Inserts the given item into the Container's inventory """

        self.contents.append(item)

    def has_item(self, item) -> bool:
        """ Returns whether or not the Container currently contains
        the specified item. """

        return item in self.contents

    def transfer_to(self, other, item) -> bool:
        """ Transfers an item from this Container's inventory to another's.
        Returns True if successful, False if not. """

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
        self.population = {}
        self.player = None

    def add(self, thing):
        """ Adds an object into the world space. """

        if not type(thing) == type([]):
            thing = [thing]
    
        for i in thing:
            if type(i) is Player:
                self.player = i
            else:
                self.population[i.name] = i

    def get_keywords(self, loc):
        """ Returns a list of all valid keywords for the given location. """

        keywords = list(itertools.chain.from_iterable([x.aliases for x in self.population.values() if x.location == loc]))
        # Neil, I apologize in advance for this line ^^^

        return keywords

    def parse_input(self, input_data):
        """ Takes inputs and parses into a more convenient datatype """

        if type(input_data) is not str:
            try:
                input_data = str(input_data)
            except AttributeError:
                return "input_data is not parsable as a string"

        keywords = self.get_keywords(self.player.location)
        print(keywords)
        input_words = input_data.split(' ')
        print(input_words)
        valid_words = [w for w in input_words if w in keywords]
        print(valid_words)

    def execute(self, cmd):
        # TODO: extrapolate and execute commands
        pass

world = World()
