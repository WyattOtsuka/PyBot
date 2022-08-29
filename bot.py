import discord
import json
import sqlite3
import db_helper as db

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
        if not db.has_user(message.author.id):
            db.new_user(message.author.id)
            # TODO - Starting prompt
        else:
            if message.content == f'{prefix}adv' or message.content == f'{prefix}adventure':
                adventure(message.author.id)

            await message.channel.send('Hello!')


'''
PLAYER METHODS
'''
@staticmethod
def adventure(id):
    '''
    Rolls dmg dealt and dmg taken. Handles winning and losing
    '''
    pass

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

@staticmethod
def roll_new_fight():
    '''
    Create a new monster with stats based on the players level
    '''
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


client.run(configs['token'])