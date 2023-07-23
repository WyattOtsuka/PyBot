class game_user:
    # id, lvl, xp, hp, atk, def, pet_id, crit_chance, crit_dmg
    def __init__(self, args):
        self.id = args[0]
        self.xp = args[1]
        self.lvl = args[2]
        self.hp = args[3]
        self.atk = args[4]
        self.defence = args[5]
        self.pet_id = args[6]
        self.crit_chance = args[7]
        self.crit_dmg = args[8]
        self.dmg_spread = args[9]


class enemy:
    def __init__(self, args):
        self.player_id = args[0]
        self.name = args[1]
        self.hp = args[2]
        self.xp = args[3]
        self.atk = args[4]
        self.defence = args[5]
        self.dmg_spread = args[6]
        self.gold = args[7]

class item:
    def __init__(self, args):
        self.name = args[0]
        self.item_id = args[1]
        self.desc = args[2]
        self.buyable = args[3]
        self.craftable = args[4]
        self.cost = args[5]
    
class inventory:
    def __init__(self, args):
        self.player_id = args[0]
        self.item_ids = args[1]
        self.quantity = args[2]

class pet:
    def __init__(self, args):
        '''
        self.id =
        self.xp = 
        self.hp = 
        self.atk = 
        self.defence = 
        '''
        pass