To start, run `python bot.py`

#Item Ids
Item Ids are unique identifiers per item. They encode information about the item. Example: 1234567890

12 is the item class
10 - Weapons
11 - Armor
12 - Ring
13 - Helmet
14 - Boots
15 - consumables
16-99 Undecided

345 is the item 
1 - Wooden Sword
2 - Rusty Knife
3 - Dull Short Sword
...
1 - Ring of String
2 - Rusted Ring
2 - Iron Ring
...

6 is the item quality. The item quality is a % modifier on the item's stats.
1 - 60% - Useless
2 - 70% - Bad
3 - 80% - Sub-par
4 - 80% - Mediocore
5 - 100% - Good
6 - 110% - Quality
7 - 120% - Unique
8 - 130% - Mythic
9 - 140% - Legendary
0 - Not Applicable

7890 is the item level. Item stats are calculated as x = x *1.01