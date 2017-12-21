import tbag

def test_suite():
    world = tbag.World()

    testStdObject = tbag.StdObject("test standard object", "limbo")
    testStdObject.set_desc("a generic standard object with no special properties")

    testLiving = tbag.Living("test living", "limbo")
    testLiving.set_desc("a generic test Living with no purpose in life")

    testPlayer = tbag.Player("test player", "limbo")
    testPlayer.set_desc("the star of the (test) show")

    testItem = tbag.Item("test item", "limbo")
    testItem.set_desc("a generic item used for testing purposes")

    testContainer = tbag.Container("test container", "limbo")
    testContainer.set_desc("a test container for holding test items")

    print("{0}\n{1}\n{2}\n{3}\n{4}\n".format(
        testStdObject, testLiving, testPlayer, testItem, testContainer
    ))


    testPlayer.inventory.show_contents()
    print("TestPlayer has TestItem: {0}\n".format(testPlayer.has_item(testItem)))

    testPlayer.give_item(testItem)

    testPlayer.inventory.show_contents()
    print("TestPlayer has TestItem: {0}\n".format(testPlayer.has_item(testItem)))


    print(tbag.Lang.gender(testPlayer))
    print(tbag.Lang.pronoun(testPlayer))

    print("{0} / {1}\n{2}. {3}\n".format(
        tbag.Lang.a("test"), tbag.Lang.a("example"),
        tbag.Lang.A("banana"), tbag.Lang.A("apple")
    ))

    tbag.Console.prettyprint("these violent delights have violent ends. it doesnt look like anything to me\n")

    flower = tbag.Item("flower", "forest")
    flower.set_desc("a delicate looking rose growing from the base of a tree stump")
    flower.add_alias('rose')

    sword = tbag.Item("sword", "forest")
    sword.set_desc("a double-edged broadsword lodged halfway in the tree stump")

    print(tbag.world.get_keywords('forest'))
    print(tbag.world.get_keywords("limbo"))

    print(tbag.world.player)

test_suite()
