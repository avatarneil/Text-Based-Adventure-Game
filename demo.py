# locations: home, starbucks
# livings: player, hipster, cia
# items: coffee, money, letter

import tbag

player = tbag.Player("Joe", "home")
hipster = tbag.Living("hipster")
cia = tbag.Living("CIA Agent")

money = tbag.Item("money")
letter = tbag.Item("letter")

hipster.give_item(money)
cia.give_item(letter)

coffee = tbag.Item("decaf chai latte", "starbucks")