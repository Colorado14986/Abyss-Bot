import os
import discord
import asyncio
from random import random, randint
from discord.ext import commands, tasks
from discord.utils import find

intents = discord.Intents.all()
client = discord.Client(intents = intents)
intents.members = True
client = commands.Bot(command_prefix = ';', intents = intents)
status = ['Dying on the inside']


serve = 'T'


@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        entry = 'Hello {}!'.format(guild.name),'My prefix is ";"'
        await general.send('Hello {}!, My prefix is ";"'.format(guild.name))



client.run(os.getenv("ABYSS_BOT_TOKEN"))
guild = client.get_guild(436904688521314307)
print(guild)
