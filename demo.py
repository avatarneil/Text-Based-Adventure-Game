# locations: home, starbucks
# livings: player, hipster, cia
# items: coffee, money, letter

import tbag

world = tbag.World()

player = world.add(tbag.Player("Joe"))
hipster = world.add(tbag.Living("hipster"))
cia = world.add(tbag.Living("CIA Agent"))

coffee = world.add(tbag.Item("decaf chai latte"))
money = world.add(tbag.Item("money"))