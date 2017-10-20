import tbag
import sys


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

    print("{0}\n{1}\n{2}\n{3}\n{4}\n".format(
        testStdObject, testLiving, testPlayer, testItem, testContainer
    ))

    testPlayer.inventory.show_contents()
    print("TestPlayer has TestItem: {0}\n".format(
        testPlayer.has_item(testItem)))

    testPlayer.give_item(testItem)

    testPlayer.inventory.show_contents()
    print("TestPlayer has TestItem: {0}\n".format(
        testPlayer.has_item(testItem)))

    print(tbag.Lang.gender(testPlayer))
    print(tbag.Lang.pronoun(testPlayer))

    print("{0} / {1}\n{2}. {3}\n".format(
        tbag.Lang.a("test"), tbag.Lang.a("example"),
        tbag.Lang.A("banana"), tbag.Lang.A("apple")
    ))

    print(tbag.Lang.prettify(
        "these violent delights have violent ends. it doesnt look like anything to me"))

    while True:
        print(tbag.Lang.prettify(input()))


def contraction_tests():
    arg1 = sys.argv[2]
    arg2 = sys.argv[3]
    a1_pretty = tbag.Lang.prettify(arg1)
    a2_pretty = tbag.Lang.prettify(arg2)

    print("arg1: {0} | arg2: {1}\na1_p: {2} | a2_p: {3}".format(
        arg1, arg2, a1_pretty, a2_pretty
    ))

    if (a1_pretty == a2_pretty):
        print("'{0}' matches '{1}'\n{1} passes contraction_tests".format(arg1, arg2))
    else:
        print("Failed {0} does not map to {1}. It maps to {2}".format(arg1, arg2, a1_pretty))


if len(sys.argv) > 1:
    if sys.argv[1] == "contraction_tests":
        contraction_tests()


# test_suite()
