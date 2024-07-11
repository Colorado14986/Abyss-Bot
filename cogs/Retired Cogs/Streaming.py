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


class Streaming_(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == 835991015273005067:
            if payload.emoji.id == 821148094670438480:
                guild = self.client.get_guild(761652116375994448)
                role = discord.utils.get(guild.roles, name="Stream Notifications")
                member = guild.get_member(int(payload.user_id))
                await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == 835991015273005067:
            if payload.emoji.id == 821148094670438480:
                guild = self.client.get_guild(761652116375994448)
                role = discord.utils.get(guild.roles, name="Stream Notifications")
                member = guild.get_member(int(payload.user_id))
                await member.remove_roles(role)


def setup(client):
    client.add_cog(Streaming_(client))