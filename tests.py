import tbag

#pylint: disable-msg=invalid-variable-name
#pylint: disable-msg=invalid-attribute-name
#pylint: disable-msg=invalid-method-name

def test_suite():
    testStdObject = tbag.StdObject("test standard object",
                                   "a generic, standard object with no special properties",
                                   "a generic object")
    testLiving = tbag.Living("test living",
                             "a living, breathing being",
                             "a living thing")
    testPlayer = tbag.Player("test player",
                             "the star of the show",
                             "you", "m", "human")
    testItem = tbag.Item("test item",
                         "a generic item used for testing purposes",
                         "an item")
    testContainer = tbag.Container("test container",
                                   "a container for holding items",
                                   "a container")

    print(testStdObject)
    print(testLiving)
    print(testPlayer)
    print(testItem)
    print(testContainer)
    print("")

    testPlayer.inventory.show_contents()
    print("TestPlayer has TestItem: {0}".format(testPlayer.has_item(testItem)))
    print("")

    testPlayer.give_item(testItem)

    testPlayer.inventory.show_contents()
    print("TestPlayer has TestItem: {0}".format(testPlayer.has_item(testItem)))
    print("")

    print(tbag.Lang.gender(testPlayer))
    print(tbag.Lang.pronoun(testPlayer))
    print(tbag.Lang.a("test"))
    print(tbag.Lang.a("example"))
    print(tbag.Lang.A("test"))
    print(tbag.Lang.A("example"))


test_suite()
