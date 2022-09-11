from email import message
from getpass import getuser
import math
import discord
import json
import sqlite3
import db_helper as db
from random import randrange

from game_data import enemy

# Setting up Login
f = open("./secrets/config.json")
configs = json.load(f)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
prefix = configs['prefix']

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    db.drop("users")
    db.drop("battles")
    db.create_tables()
    print("\n")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix):
        id = message.author.id
        content = message.content
        if content == f'{prefix}adv' or content == f'{prefix}adventure':
            if not db.has_user(id):
                db.new_user(id)
                await new_player(message)
            else:
                await adventure(id, message.channel)
        elif content == f'{prefix}help':
            await help(message.channel)
        elif content == f'{prefix}rules':
            await rules(message.channel)


'''
PLAYER METHODS
'''
@staticmethod
async def new_player(message):
    username = message.author.name
    await message.channel.send(f'''
    Welcome {username} to PyBot!
    \rUse {prefix}rules for the rules, and {prefix}help for commands
    ''')

@staticmethod
async def adventure(id, channel):
    '''
    Rolls dmg dealt and dmg taken. Handles winning and losing
    '''
    user = db.get_user(id)
    # TODO - change to scale with level
    if not db.in_fight(id):
        # Get current level +/- 3 to fight level [0:inf)
        roll_new_fight(id)
    enemy = db.get_enemy(id)

    player_roll = randrange(1,6,1)
    enemy_roll = randrange(1,6,1)

    # Add base dmg to roll * spread
    dmg_to_player = enemy_roll * enemy.dmg_spread + enemy.atk
    dmg_to_enemy = player_roll * user.dmg_spread + user.atk + 30

    player_hp = db.update_hp(id, -dmg_to_player)
    enemy_hp = db.dmg_enemy(id, dmg_to_enemy)

    if player_hp <= 0: # Loss
        await channel.send("You died")
    else:
        if enemy_hp <=0: # Win
            await channel.send("You won!")
        else: # Undecided       
            await channel.send(f"Your HP: {player_hp}\nEnemy HP: {enemy_hp}")




        
        

@staticmethod
def heal(item, count):
    '''
    Uses count amount of item to heal
    '''
    pass

@staticmethod
def points(perk, points):
    '''
    Spend points from leveling up to increase perk
    '''
    pass

@staticmethod
def perks(number, tier):
    '''
    Gives the user perk number of perk tier
    '''
    pass

# TODO - update from dummy fight, change to scale with level
@staticmethod
def roll_new_fight(id):
    '''
    Create a new monster with stats based on the players level
    '''
    # Currently Rolling Dummy fight
    db.new_fight(id)
    pass
'''
PET METHODS
'''
@staticmethod
def xp_share(percent):
    pass

@staticmethod
def set_name(name):
    pass


'''
HELPER METHODS
'''

@staticmethod
def xp_to_level(lvl) -> int:
    '''
    Returns xp required to get to next level 
    
    10 + lvl for base scaling up of the level xp. lvls 1 - 100
    math.floor(lvl/10) to make each set of 10 scale harder than the rest
    ** 1.5 for the range of 100 to about 500
    (1/2000) * (1000 - math.floor(1000/lvl)) helps keep the xp form taking off too far. 500+
    '''
    return (10 + lvl ) * math.floor(lvl/10) ** (1.5 - (1/2000) * (1000 - math.floor(1000/lvl)))

@staticmethod
async def help(channel):
    await channel.send(f'''
    **PYBOT COMMANDS**
    \r**{prefix}help:**\nDisplay this message
    \r**{prefix}rules**:\nDisplay rules
    \r**{prefix}adv** | **{prefix}adventure**:\nFight a monster
    \r**{prefix}heal [amount | auto]**:\nHeals with one or amount passed health potions. Auto heals to max hp without overhealing
    ''')

@staticmethod
async def rules(channel):
    await channel.send('''
    - No bigotry, racism, hate speech, etc. will be tolerated. You will be permenantly banned.
    - The bot does NOT have any rule against automation. The game is designed to be played by a script, and scales likewise.
    ''')
    pass

client.run(configs['token'])