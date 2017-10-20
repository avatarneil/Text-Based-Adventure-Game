"""
Text Based Adventure Game Engine (tbag.py)
A set of classes and methods for creating
player-driven text-based experiences.
"""

import sys

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
    def inputParser(cls, inputData):
        """ Takes inputs and parses into a more convenient datatype """

        if type(inputData) is str:  # if inputData is a string case
            firstWord = inputData.partition(' ')[0]
        else:
            try:
                inputData = str(inputData)
                firstWord = inputData.partition(' ')[0]
            except AttributeError:
                return "inputData is not parsable as a string"

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


class StdObject():
    """ Base object from which all other objects derive from.
    Should never be used directly. """

    def __init__(self, name, longDesc="", shortDesc=""):
        self.name = name
        self.longDesc = longDesc
        self.shortDesc = shortDesc
        self.actions = {}

    def __str__(self):
        return "a StdObject called '{0}'".format(self.name)

    def __repr__(self):
        return "StdObject\nName: {0}\nlongDesc: {1}\nshortDesc: {2}"\
               "\n".format(self.name, self.longDesc, self.shortDesc)

    def attach_action(self, action_name, action):
        """ Adds an Action to this objects dictionary
        of valid actions to perform on it. """

        self.actions[action_name] = action

    def detach_action(self, action_name):
        """ Deletes an action from this object's dictionary
        of valid actions to perform on it. """

        del self.actions[action_name]

    def has_action(self, action_name) -> bool:
        """ Returns whether or not this object has an action
        with the given name. (True/False) """

        return self.actions[action_name]


class Living(StdObject):
    """ Base class from which all living things derive from.
    Should never be used directly. """

    def __init__(self, name, longDesc="", shortDesc="",
                 gender="x", race="human"):
        super().__init__(name, longDesc, shortDesc)
        self.gender = gender
        self.race = race
        self.inventory = Container("{0}'s inventory".format(self.name))

    def __str__(self):
        return Lang.a("{0} {1} Living named '{2}'".format(Lang.gender(self), self.race, self.name))

    def __repr__(self):
        return "Living\nName: {0}\nlongDesc: {1}\nshortDesc: {2}\ngender: {3}\nrace: {4}".format(
            self.name, self.longDesc, self.shortDesc, self.gender, self.race)

    def give_item(self, item):
        """ Inserts the given item into this Living's inventory. """

        self.inventory.add_item(item)

    def has_item(self, item) -> bool:
        """ Returns whether or not this Living currently has
        the specified item (True/False). """

        return self.inventory.has_item(item)

    def do_action(self, action_name, target):
        """ Attempts to perform the specified action on the specified target.
        Returns True if successful, otherwise returns False. """

        if target.has_action(action_name):
            target.actions[action_name].execute(self, target)
            return True
        else:
            return False


class Player(Living):
    """ Controls the Player and handles interaction. """

    def __init__(self, name, longDesc="", shortDesc="",
                 gender="x", race="human"):
        super().__init__(name, longDesc, shortDesc, gender, race)

    def __str__(self):
        return Lang.a("{0} {1} Player named '{2}'".format(Lang.gender(self), self.race, self.name))

    def __repr__(self):
        return "Player\nName: {0}\nlongDesc: {1}\nshortDesc: {2}\ngender: {3}\nrace: {4}".format(
            self.name, self.longDesc, self.shortDesc, self.gender, self.race)


class Item(StdObject):
    """ Generic base class for interactible items. """

    def __init__(self, name, longDesc="", shortDesc="", value=0):
        super().__init__(name, longDesc, shortDesc)
        value = value

    def __str__(self):
        return "an Item called '{0}'".format(self.name)

    def __repr__(self):
        return "Item\nName: {0}\nlongDesc: {1}\nshortDesc: {2}"\
            "\n".format(self.name, self.longDesc, self.shortDesc)


class Container(Item):
    """ Game object that is used to store other objects. """

    def __init__(self, name, longDesc="", shortDesc=""):
        super().__init__(name, longDesc, shortDesc)
        self.contents = []

    def __str__(self):
        return "a Container called '{0}'".format(self.name)

    def __repr__(self):
        return "Container\nName: {0}\nlongDesc: {1}\nshortDesc: {2}"\
               "\n".format(self.name, self.longDesc, self.shortDesc)

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


class Location(StdObject):
    """ Handles the contents of a certain game location. """

    def __init__(self, name, longDesc, shortDesc):
        super().__init__(self, name, longDesc, shortDesc)
        self.inventory = Container(
            "Contents of Location '{0}'".format(self.name))

    def add_item(self, item):
        self.inventory.add_item(item)

    def get_keywords(self) -> list:
        # TODO: dynamically create lists of every valid keyword for a Location
        pass

    def get_desc():
        contents_descs = [Lang.a(x.shortDesc) for x in self.inventory.contents]
        return Lang.prettify("{0}. there is {1}".format(self.shortDesc, ', '.join(contents_descs)))


class Exit(StdObject):
    """ Handles moving the Player from one Location to another. """

    def __init__(self, name, longDesc, shortDesc):
        super().__init__(self, name, longDesc, shortDesc)
        self.destination = None


class Action():  # lawsuit
    """ Actions are attached to StdObjects using StdObject.attach_action().
    Once an action has been atatched to a StdObject, any living can perform
    that action using Living.do_action() """
    # TODO: StdObject.attach_action()
    # TODO: Living.do_action()

    def __init__(self, name, base, tell=None, synonyms=None):
        self.base = base  # eg. write, open, go
        self.name = name
        if not tell:  # eg. writes, opens, goes
            self.tell = base + 's'
        else:
            self.tell = tell
        if not synonyms:
            self.synonyms = []
        else:
            self.synonyms = synonyms

    def execute(self, doer, target) -> bool:
        return("Default action '{0}' performed by '{1}' on '{2}'.".format(
               self.name, doer, target))
