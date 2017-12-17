# locations: home, starbucks
# livings: player, hipster, cia
# items: coffee, money, letter

import tbag

player = tbag.Player("Joe", "starbucks")

hipster = tbag.Living("hipster", "starbucks")

cia = tbag.Living("CIA Agent", "starbucks")
cia.add_alias(["agent","spy"])

money = tbag.Item("money")
hipster.give_item(money)

letter = tbag.Item("letter")
letter.add_alias(["envelope","message"])
cia.give_item(letter)

coffee = tbag.Item("decaf chai latte", "starbucks")
coffee.add_alias(["coffee","decaf","chai","latte"])

while True:
    tbag.Console.input()