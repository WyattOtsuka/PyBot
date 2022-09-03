from getpass import getuser
import math
import discord
import json
import sqlite3
import db_helper as db
from random import Random

# Setting up Login
f = open("./secrets/config.json")
configs = json.load(f)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
prefix = configs['prefix']

# Setting up the database
connection = sqlite3.connect("./secrets/PyBot.db")
cursor = connection.cursor()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix):
        id = message.author.id
        if not db.has_user(id):
            db.new_user(id)
            # TODO - Starting prompt
        else:
            
            if message.content == f'{prefix}adv' or message.content == f'{prefix}adventure':
                adventure(id)

            await message.channel.send('Hello!')


'''
PLAYER METHODS
'''
@staticmethod
def adventure(id):
    '''
    Rolls dmg dealt and dmg taken. Handles winning and losing
    '''
    print("adv called")
    if db.in_fight(id):
        print("in fight")
        player_roll = Random(0,6,1)
        enemy_roll = Random(0,6,1)
    else:
        print("not in fight")
        # Get current level +/- 3 to fight level [0:inf)
        roll_new_fight(id)

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

# TODO - update from dummy fight
@staticmethod
def roll_new_fight(id):
    '''
    Create a new monster with stats based on the players level
    '''
    print("Rolling new fight")
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


client.run(configs['token'])