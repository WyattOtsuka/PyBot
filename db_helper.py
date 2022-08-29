import sqlite3
from game_data import pet, game_user
connection = sqlite3.connect("./secrets/PyBot.db")
cursor = connection.cursor()

@staticmethod
def create_tables():
    try:
        cursor.execute("CREATE TABLE users (player_id TEXT, xp INTEGER, hp INTEGER, atk INTEGER, def INTEGER, pet_id TEXT, crit_chance INTEGER, crit_dmg INTEGER, dmg_spread INT)")
        cursor.execute("CREATE TABLE pets (pet_id TEXT, level INTEGER, xp INTEGER, hp INTEGER, atk INTEGER, def INTEGER")
        cursor.execute("CREATE TABLE battles (enemy_hp INT, enemy_xp INT, enemy_attack INT, enemy_def INT, enemy_dmg_spread INT")
        cursor.execute("CREATE TABLE eqpt (weapon_id INT, armor_id INT, ring_id INT, helmet_id INT, boots_id INT)")
    except Exception as e:
        print(e)


# id, xp, hp, atk, def, pet_id, crit_chance, crit_dmg
# Note: Player level is calculated based on total xp
@staticmethod
def new_user(id):
    '''
    Adds a new user into the system
    '''
    cursor.execute(f"INSERT INTO users VALUES ({id}, 0, 100, 5, 0, NULL, 1, 2, 6)")

def has_user(id) -> bool:
    return len(cursor.execute(f"SELECT * FROM users WHERE player_id = {id}").fetchall()) > 0

@staticmethod
def get_user(id) -> game_user:
    ''''
    Returns a game_user object with the given ID
    '''
    stats = cursor.execute(f"SELECT * FROM users WHERE player_id = {id}").fetchall()
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

@staticmethod
def drop(table):
    cursor.execute(f"DROP TABLE {table}")

'''
TODO
Pet
    get(id)
    new_pet(args)
    update_hp() -> int
    update_xp() -> int

''' 

'''
drop("users")
drop("pets")
drop("battles")
drop("eqpt")
'''
create_tables