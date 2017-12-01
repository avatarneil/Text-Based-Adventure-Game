import tbag

def test_suite():
    testStdObject = tbag.StdObject("test standard object",
                                   "a generic, standard object with no special properties",
                                   "a generic object", "limbo")
    testLiving = tbag.Living("test living",
                             "a living, breathing being",
                             "a living thing", "limbo")
    testPlayer = tbag.Player("test player",
                             "the star of the show",
                             "limbo", "you", "m", "human")
    testItem = tbag.Item("test item",
                         "a generic item used for testing purposes",
                         "an item", "limbo")
    testContainer = tbag.Container("test container",
                                   "a container for holding items",
                                   "a container", "limbo")

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

    print(tbag.Lang.prettify("these violent delights have violent ends. it doesnt look like anything to me"))

    world = tbag.World()
    '''world.init_player(
    world.init_location("forest", "a clearing in the forest", "a clearing")
    world.add_to_loc('forest',
                    

    print(world.locations['forest'].get_desc())
    print(world.locations['forest'].get_keywords())'''

    testLiving.location = 'forest'
    world.add(testLiving)


    mushroom = tbag.Item("mushroom",
                         "a short, brown mushroom growing by a tree stump",
                         "a brown mushroom", "forest")
    
    world.add(mushroom)

    print(world.get_keywords('forest'))
    mushroom.add_alias(['shroom', 'shrooms'])
    print(world.get_keywords('forest'))

test_suite()
