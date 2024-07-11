import os
import youtube_dl
import discord
import datetime
import asyncio
import time
import discord.voice_client
from pytube import YouTube
from random import randint
from discord.ext import commands
from discord.utils import find, get
import urbandict
from urban import UrbanClient
import json


class customs(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def killer(self, ctx, *member: discord.Member):

        cd = ctx.author.voice.deaf
        cm = ctx.author.voice.mute
        if not member:
            if cd or cm:
                await ctx.author.edit(mute=False)
                await ctx.author.edit(deafen=False)
            else:
                await ctx.author.edit(mute=True)
                await ctx.author.edit(deafen=True)

        if member:
            user = ctx.guild.get_member(member[0].id)
            md = user.voice.deaf
            mm = user.voice.mute
            if ctx.author.guild_permissions.administrator:
                if md or mm:
                    await user.edit(deafen=False)
                    await user.edit(mute=False)
                else:
                    await user.edit(deafen=True)
                    await user.edit(mute=True)

    @commands.command()
    async def roll(self, ctx, *args):
        opts = []
        for word in args:
            opts.append(word)
        num = randint(0, len(opts))
        num = num - 1
        await ctx.send(f'The killer is {opts[num]}')

def setup(client):
    client.add_cog(customs(client))
