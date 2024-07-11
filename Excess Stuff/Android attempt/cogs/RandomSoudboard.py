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


class rando(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.client.commandList = [
            'hehe',
            'ahoy',
            'ht',
            'hg',
            'fy',
            'giggity',
            'gae',
            'gay',
            'brb',
            'phil',
            'r2',
            'mission',
            'jeff',
            'hehe',
            'meat',
            'simp',
            'job',
            'family',
            'wazzup',
            'gdonkey',
            'tmo',
            'familyguy',
            'door',
        ]

    @commands.command(aliases=['rs'])
    async def random(self, ctx):
        command = self.client.commandList[randint(0, (len(self.client.commandList)-1))]
        try:
            c = self.client.get_command(command)
            await ctx.invoke(c)
        except:
            print('random soundboard failed')

def setup(client):
    client.add_cog(rando(client))