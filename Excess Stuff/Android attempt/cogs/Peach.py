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


class Peach_Server_Stuff(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 899889012259573771:
            channel = self.client.get_channel(899889012259573774)
            true_member_count = len([m for m in member.guild.members if not m.bot])
            embed=discord.Embed(title=f"Welcome to {member.guild.name} {member.name}!!", description=f"We hope you enjoy your stay here, please be sure to check out <#900105001664397323>", color=0xaa8fd6)
            embed.set_author(name=f"{member.name} has joined!!!", icon_url=member.avatar_url)
            embed.set_image(url="https://cdn.discordapp.com/attachments/900001336282742856/900166801936240660/image0.png")
            embed.set_footer(text=f"You are our {true_member_count}th member!")
            await channel.send(f'||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _ {member.mention}', embed=embed)

    @commands.command(aliases=['Whois', 'whoIs', 'WhoIs'])
    async def whois(self, ctx):
        if ctx.guild.id == 899889012259573771:
            People = []
            for member in ctx.guild.members:
                if member.bot == False:
                    People.append(member)
            length = len(People) - 1
            num = randint(0, length)
            if People[num].nick == None:
                await ctx.send(f"That'd be {People[num].name}")
            else:
                await ctx.send(f"That'd be {People[num].nick}")
                      

def setup(client):
    client.add_cog(Peach_Server_Stuff(client))

