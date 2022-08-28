class game_user:
    def __init__(self, args):
        self.id = args[0]
        self.hp = args[1]
        self.xp = args[2]
        self.atk = args[3]
        self.defence = args[4]
        self.pet_id = args[5]
        self.crit_chance = args[6]
        self.crit_dmg = args[7]