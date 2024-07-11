import os
import youtube_dl
import discord
import datetime
import asyncio
import time
import discord.voice_client
import urllib.request
import re
from random import randint
from discord.ext import commands
from discord.ext.commands import Cog
from discord.utils import find, get
global client

class Music(Cog):

    def __init__(self, bot):
        self.bot = bot
        self.counter = 0

    @commands.command()
    async def add(self):
        self.counter += 1
        await self.bot.say('Counter is now %d' % self.counter)
    @commands.command()
    async def tester(ctx):
        await ctx.send('functions')


def setup(bot):
    bot.add_cog(Music(bot))
