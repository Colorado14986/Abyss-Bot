import os
import youtube_dl
import discord
import datetime
import asyncio
import time
import discord.voice_client
from random import randint
from discord.ext import commands, tasks
from discord.utils import find, get
import subprocess
import os
from dotenv import load_dotenv
from discord_components import *

youtube_dl.utils.bug_reports_message = lambda: ''
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = ';', intents = intents)
DiscordComponents(client)
client.remove_command('help')
queu = []
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.joins = {
        230442733234421760: 'https://www.youtube.com/watch?v=crv99-LT4j8', #Giraffe
        418087030950723606: 'https://www.youtube.com/watch?v=_nce9A5S5uM',#Boiyo
        83897138240585728: 'https://www.youtube.com/watch?v=D-0HbnyIMlY',#Gecko
        #488434417816043520: 'https://www.youtube.com/watch?v=EPX5IBbfmEQ',#NEA.coming together
        #488434417816043520: 'https://www.youtube.com/watch?v=1Gw8L11UG4Q',#Nea.Claire
        488434417816043520: 'https://youtu.be/1Rxhv96SWAg',#NEA.Pronunciation
        626081191207895040: 'https://www.youtube.com/watch?v=zIuNrejw4EA',#Xbox
    }

client.mobile_users = [
    345982989957726210,#Levi
    ]

client.onjoins = True

@client.command()
async def onjoins(ctx):
    state = client.onjoins
    if ctx.author.guild_permissions.administrator:
        if state:
            client.onjoins = False
            await ctx.send('Join sound effects are now toggled off')
        if not state:
            client.onjoins = True
            await ctx.send('Join sound effects are now toggled on')

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
                    client.unload_extension(f'cogs.{filename[:-3]}')
                except:
                    pass
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                client.load_extension(f'cogs.{filename[:-3]}')
        await ctx.send('All cogs reset')



# @client.command()
# async def CogReset(ctx):
#     num = 0
#     cogs = []
#     for cog in client.cogs:
#         cogs.append(cog)
#     for f in range(0, len(cogs)):
#         client.remove_cog(cogs[f])
#     for f in range(0, len(cogs)):
#         client.add_cog(cogs[f])



client.run(os.getenv("ABYSS_BOT_TOKEN"))
