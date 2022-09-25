from distutils.sysconfig import customize_compiler
import sqlite3
from game_data import pet, game_user, enemy
connection = sqlite3.connect("./secrets/PyBot.db")
cursor = connection.cursor()

@staticmethod
def create_tables():
    try:
        cursor.execute("""
            CREATE TABLE users 
                (player_id TEXT, xp INTEGER, lvl INTEGER, hp INTEGER, atk INTEGER, 
                def INTEGER, pet_id TEXT, crit_chance INTEGER, crit_dmg INTEGER, 
                dmg_spread INT)
            """)
        print("Created Users")
    except Exception as e:
        print(e)

    try:
        cursor.execute("""
            CREATE TABLE pets 
                (pet_id TEXT, level INTEGER, xp INTEGER, hp INTEGER, atk INTEGER,
                def INTEGER)
                """)
        print("Created pets")
    except Exception as e:
        print(e)

    try:
        cursor.execute("""
        CREATE TABLE battles
            (player_id TEXT, enemy_name TEXT, enemy_hp INT, enemy_xp INT,
            enemy_attack INT, enemy_def INT, enemy_dmg_spread INT,
            enemy_gold INT)
            """)
        print("Created battles")
    except Exception as e:
        print(e)

    try:
        cursor.execute("""
        CREATE TABLE eqpt 
            (player_id TEXT, weapon_id INT, armor_id INT, ring_id INT,
            helmet_id INT, boots_id INT)
        """)
        print("Created eqpt")
    except Exception as e:
        print(e)

    try:
        cursor.execute("""
        CREATE TABLE items
            (item_id TEXT, item_desc TEXT, buyable INT, craftable INT, cost INT)
        """)
        print("Created inv")
    except Exception as e:
        print(e)

    try:
        cursor.execute("""
        CREATE TABLE inv
            (player_id TEXT, gold INT, potions INT)
        """)
        print("Created inv")
    except Exception as e:
        print(e)


@staticmethod
def create_items(name, desc, buyable, craftable, cost):
    '''
    Adds a new item into the table
    '''
    if buyable:
        buyable = 1
    else: 
        buyable = 0
    
    if craftable:
        craftable = 1
    else:
        craftable = 0

    cursor.execute(f"INSERT INTO items VALUES ({name}, {desc}, {buyable}, {craftable}, {cost})")
    connection.commit()

@staticmethod
def drop(table):
    cursor.execute(f"DROP TABLE {table}")

@staticmethod
def commit():
    connection.commit()

'''
PLAYER METHODS
'''
# id, xp, lvl, hp, atk, def, pet_id, crit_chance, crit_dmg, dmg spread
# Note: Player level is calculated based on total xp
@staticmethod
def new_user(id):
    '''
    Adds a new user into the system
    '''
    cursor.execute(f"INSERT INTO users VALUES ({id}, 0, 1, 100, 5, 0, NULL, 1, 2, 1)")
    cursor.execute(f"INSERT INTO inv VALUES ({id}, 100, 5)")

def has_user(id) -> bool:
    return len(cursor.execute(f"SELECT * FROM users WHERE player_id = {id}").fetchall()) > 0

@staticmethod
def get_user(id) -> game_user:
    ''''
    Returns a game_user object with the given ID
    '''
    stats = cursor.execute(f"SELECT * FROM users WHERE player_id = {id}").fetchall()
    gm = game_user(stats[0])
    return gm

@staticmethod
def update_hp(id, delta) -> int:
    '''
    Changes the HP of a user to a new amount.
    new HP = old HP + delta
    Returns the new HP
    '''
    player_hp = cursor.execute(f"SELECT hp FROM users WHERE player_id = {id}").fetchall()[0][0]
    print(player_hp)
    player_hp += delta
    cursor.execute(f"UPDATE users SET hp = {player_hp} WHERE player_id = {id}")
    return player_hp
    
@staticmethod
def update_xp(id, xp) -> int:
    '''
    Changes xp to a new amount
    '''
    cursor.execute(f"UPDATE users SET xp = {xp} WHERE player_id = {id}")
    connection.commit()

def update_level(id, level) -> int:
    '''
    Change the level of the player
    '''
    cursor.execute(f"UPDATE users SET lvl = {level} WHERE player_id = {id}")
    connection.commit()


'''
COMBAT METHODS
'''

@staticmethod
def in_fight(id):
    '''
    Returns true if the user is currently in a fight
    '''
    return len(cursor.execute(f"SELECT * FROM battles WHERE player_id = {id}").fetchall()) > 0

# TODO - change from dummy fight
# id, e name, e hp, e xp, e atk, e def, e dmg spread, e gold
@staticmethod
def new_fight(id):
    '''
    Create a new fight
    '''
    cursor.execute(f"INSERT INTO battles VALUES ({id}, \"Dummy Enemy\", 100, 5000, 3, 3, 0, 15)")

@staticmethod
def dmg_enemy(id, dmg_dealt) -> int:
    '''
    Deal damage to the current enemy the user is fighting. 
    Returns the enemies current HP after damage is dealt
    '''
    enemy_hp = cursor.execute(f"SELECT enemy_hp FROM battles WHERE player_id = {id}").fetchall()[0][0]
    enemy_hp -= dmg_dealt
    cursor.execute(f"UPDATE battles SET enemy_hp = {enemy_hp}")
    return enemy_hp

@staticmethod
def get_enemy(id) -> enemy:
    '''
    Returns fight data for player with given id
    '''
    fight = cursor.execute(f"SELECT * FROM battles WHERE player_id = {id}").fetchall()[0]
    em = enemy(fight)
    return em

def end_fight(id):
    '''
    Removes the fight for player with id from the table
    '''
    cursor.execute(f"DELETE FROM battles WHERE player_id = {id}")

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


#create_tables()