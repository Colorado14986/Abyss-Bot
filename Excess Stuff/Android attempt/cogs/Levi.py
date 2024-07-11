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


class Levi_Server_Stuff(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 819385452493537280:
            channel = self.client.get_channel(819385452493537283)
            true_member_count = len([m for m in member.guild.members if not m.bot])
            embed=discord.Embed(title=f"Welcome to {member.guild.name} {member.name}!!", description=f"We hope you enjoy your stay here, please be sure to check out <#819582730080616509>", color=0xd49bb2)
            embed.set_author(name=f"{member.name} has joined!!!", icon_url=member.avatar_url)
            embed.set_image(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2F1pcR11ivm08%2Fmaxresdefault.jpg&f=1&nofb=1")
            embed.set_footer(text=f"You are our {true_member_count}th member!")
            await channel.send(f'||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _ {member.mention}', embed=embed)
    '''
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 345982989957726210:
            if message.guild.id == 819385452493537280:
                await message.channel.send(message.content)
    '''

    @commands.command()
    async def rat(self, ctx):
        picture_choice = random.choice(os.listdir("D:\Bot\Images\Cute rat pictures"))
        picture = discord.File(f"D:\Bot\Images\Cute rat pictures\{picture_choice}", filename="image.png")
        embed = discord.Embed(title='Here is rat:', colour=0x89cff0)
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=picture, embed=embed)

    @commands.command()
    async def ratfact(self, ctx):
        with open('./TextLogs/Rat_Facts.txt', 'r', encoding="utf8") as file:
            facts = []
            for line in file:
                facts.append(line)
            Q = randint(1, (len(facts)))
            Q = Q - 1
            embed = discord.Embed(title=f'Requested Rat Fact:', description=f'{facts[Q]}')
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Levi_Server_Stuff(client))
