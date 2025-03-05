# import youtube_dl
import yt_dlp
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import discord
from discord import app_commands
import datetime
import asyncio
import time
import discord.voice_client
from random import randint
from discord.ext import commands, tasks
from discord.utils import find, get
import os
from dotenv import load_dotenv
import subprocess
#from discord_components import *
import logging
import sys

'''
root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)
'''
discord.utils.setup_logging()

yt_dlp.utils.bug_reports_message = lambda: ''
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = ';', intents = intents)
#discord(client)
client.remove_command('help')
queu = []
load_dotenv()



# client.joins = {
#         #230442733234421760: 'https://www.youtube.com/watch?v=crv99-LT4j8', #Giraffe.Colorado
#         #230442733234421760: 'https://youtu.be/UMBMMMVL88M',#Giraffe.Hey
#         #230442733234421760: 'https://www.youtube.com/watch?v=FZUcpVmEHuk', #Giraffe.Garbage
#         230442733234421760: 'https://www.youtube.com/watch?v=YnKW29WPveM', #Giraffe.HelloGamers
#         #418087030950723606: 'https://www.youtube.com/watch?v=_nce9A5S5uM',#Boiyo.Jeff
#         #418087030950723606: 'https://youtu.be/UMBMMMVL88M',#Boiyo.Hey
#         #418087030950723606: 'https://youtu.be/c3oVxhXhWrs', #Boiyo.Otz
#         418087030950723606: 'https://youtu.be/v2rWjVP1_JA', #Boiyo.Ash
#         #83897138240585728: 'https://www.youtube.com/watch?v=D-0HbnyIMlY',#Gecko.R2
#         83897138240585728: 'https://www.youtube.com/watch?v=ane8xXNWwns',#Gecko.Ahoy
#         #83897138240585728: 'https://m.youtube.com/watch?v=yaVLyL2IA20',#Gecko.Die Already
#         #488434417816043520: 'https://www.youtube.com/watch?v=EPX5IBbfmEQ',#NEA.coming together
#         #488434417816043520: 'https://www.youtube.com/watch?v=1Gw8L11UG4Q',#Nea.Claire
#         #488434417816043520: 'https://youtu.be/1Rxhv96SWAg',#NEA.Pronunciation
#         488434417816043520: 'https://youtu.be/_SPMvkVLV2U', #Nea.Otz Names
#         626081191207895040: 'https://www.youtube.com/watch?v=zIuNrejw4EA',#Xbox.Xbox
#         #303216255391891466: 'https://www.youtube.com/watch?v=KR4uf-8bfpE',#Tenshi.Malaysia
#         #303216255391891466: 'https://www.youtube.com/watch?v=8-nTWaU1qPc', #Tenshi.Arcana
#         303216255391891466: 'https://youtu.be/zawQKNjsg_4', #Tenshi.Ash
#     }
# client.onjoins = True

# @client.command()
# async def onjoins(ctx):
#     state = client.onjoins
#     if ctx.author.guild_permissions.administrator:
#         if state:
#             client.onjoins = False
#             await ctx.send('Join sound effects are now toggled off')
#         if not state:
#             client.onjoins = True
#             await ctx.send('Join sound effects are now toggled on')

@client.command()
async def clist(ctx):
    helptext = ''
    for command in client.commands:
        helptext += f"{command}\n"
    await ctx.send(helptext)

@client.command()
async def reload(ctx):
    if ctx.author.id == 230442733234421760:
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                try:
                    await client.unload_extension(f'cogs.{filename[:-3]}')
                except:
                    pass
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await client.load_extension(f'cogs.{filename[:-3]}')
        await ctx.send('All cogs reset')


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with client:
        await load_extensions()
        await client.start(str(os.getenv("ABYSS_BOT_TOKEN")))

asyncio.run(main())
