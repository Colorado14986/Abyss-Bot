import discord
import discord.voice_client
from discord.ext import commands, tasks
from discord.utils import find, get
from random import randint
from datetime import datetime
import time
import json
import os
import subprocess
import os, random


class Funzie_Server_Stuff(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 559119490571567106:
            embed = discord.Embed()
            embed.add_field(name='Funzie has moved to a new server here is the link:', value='[Click Here:](https://discord.gg/va5Z4QKtGT)')
            channel = await member.create_dm()
            await channel.send(embed=embed)
            await member.kick()  

def setup(client):
    client.add_cog(Funzie_Server_Stuff(client))

