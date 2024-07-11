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


class Inanna_Server_Stuff(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 1104879054005477529:
            channel = self.client.get_channel(1104931648157536297)
            true_member_count = len([m for m in member.guild.members if not m.bot])
            embed=discord.Embed(title=f"Welcome to {member.guild.name}!!", description=f"We hope you enjoy your stay here, please follow the instructions in <#1104898328715599982>", color=0xd49bb2)
            embed.set_author(name=f"{member.name} has joined!!!", icon_url=member.avatar.url)
            embed.set_image(url="https://cdn.discordapp.com/attachments/1104895649637470309/1105162540230656110/B8mjo62.png")
            embed.set_footer(text=f"You are our {true_member_count}th member!")
            await channel.send(embed=embed)

    @commands.command()
    async def cleanse(self, ctx):
        def not_pinned(msg):
            return not msg.pinned
        if ctx.author.id in [1063857402199420929, 295668065654276097, 968004263211048981, 230442733234421760, 852276344799756399]: #Scout for all
            await ctx.channel.purge(limit=500, check=not_pinned)
        else:
            msg = "You do not have the perms for this command"
            await ctx.send(msg)

async def setup(client):
    await client.add_cog(Inanna_Server_Stuff(client))
