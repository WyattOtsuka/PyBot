import sqlite3
from game_data import pet, game_user
connection = sqlite3.connect("./secrets/PyBot.db")
cursor = connection.cursor()

class db_helper:

    @staticmethod
    def create_tables():
        try:
            cursor.execute("CREATE TABLE users (player_id TEXT, xp INTEGER, hp INTEGER, atk INTEGER, def INTEGER, pet_id TEXT, crit_chance INTEGER, crit_dmg INTEGER)")
            cursor.execute("CREATE TABLE pets (pet_id TEXT, level INTEGER, xp INTEGER, hp INTEGER, atk INTEGER, def INTEGER")
        except:
            pass

    # id, xp, hp, atk, def, pet_id, crit_chance, crit_dmg
    # Note: Player level is calculated based on total xp
    @staticmethod
    def new_user(id):
        '''
        Adds a new user into the system
        '''
        cursor.execute(f"INSERT INTO users VALUES ({id}, 0, 100, 5, 0, NULL, 1, 2)")

    @staticmethod
    def get_user(id) -> game_user:
        ''''
        Returns a game_user object with the given ID
        '''
        stats = cursor.execute(f"SELECT * FROM users WHERE player_id = {id}").fetchall()[0]
        gm = game_user(stats)
        return gm

    @staticmethod
    def update_hp(id, delta) -> int:
        '''
        Changes the HP of a user to a new amount.
        new HP = old HP + delta
        Returns the new HP
        '''
        pass

    @staticmethod
    def update_xp() -> int:
        '''
        Changes xp to a new amount
        '''

    '''
    TODO
    Pet
        get(id)
        new_pet(args)
        update_hp() -> int
        update_xp() -> int

    ''' 