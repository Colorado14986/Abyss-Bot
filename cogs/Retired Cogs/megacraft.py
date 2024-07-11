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
'''
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild.id == 833745752827887616:
            #try:
            if any(word in message.content for word in self.profanity):
                await message.delete()
            #except:
                #pass
'''

class megacraft_(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.profanity = [
            "anal",
            "anus",
            "arse",
            "ass ",
            "b1tch",
            "ballsack",
            "bastard",
            "bitch",
            "biatch",
            "blowjob",
            "bollock",
            "bollok",
            "boner",
            "boob",
            "boobs",
            "buttplug",
            "clitoris",
            "cock",
            "bish",
            "paki",
            "cum",
            "cunt",
            "dick",
            "dildo",
            "dyke",
            "erection",
            "fag",
            "faggot",
            "feck",
            "fellate",
            "fellatio",
            "felching",
            "fuck",
            "fucks",
            "fudgepacker",
            "genitals",
            "jizz",
            "labia",
            "masturbate",
            "muff",
            "nigger",
            "nigga",
            "penis",
            "piss",
            "poop",
            "pube",
            "pussy",
            "queer",
            "scrotum",
            "sex",
            "shit",
            "sh1t",
            "slut",
            "smegma",
            "spunk",
            "tranny",
            "trannies",
            "turd",
            "twat",
            "vagina",
            "wank",
            "whore",
            "tits",
            "titty",
            "asshole",
            "fvck",
            "asshat",
            "pu55y",
            "pen1s",
        ]

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 833745752827887616:
            role = discord.utils.get(member.guild.roles, name='Applying')
            await member.add_roles(role)

    @commands.command()
    async def ip(self, ctx):
        if ctx.guild.id == 833745752827887616:
            embed = discord.Embed(description='**Server Info:**\n Also available in <#833757607746994186>')
            embed.add_field(name='IP:', value='51.79.111.26:25593')
            embed.add_field(name='Dynmap link:', value='http://51.79.111.26:8147/', inline=False)
            await ctx.send(embed=embed)

    @commands.command()
    async def ip_nolink(self, ctx):
        if ctx.author.id == 230442733234421760:
            embed = discord.Embed(description='**Server Info:**')
            embed.add_field(name='IP:', value='51.79.111.26:25593')
            embed.add_field(name='Dynmap link:', value='http://51.79.111.26:8147/', inline=False)
            await ctx.send(embed=embed)

    @commands.command()
    async def logban(self, ctx, *, log):
        if ctx.guild.id == 833745752827887616:
            t = datetime.datetime.now()
            t = t.strftime('%x')
            info = ''
            for word in log:
                info += word
            print('{}: {} : {}'.format(t, ctx.author, info))
            with open('./TextLogs/Bans.txt', "a") as file:
                file.write('{}: {} : {}\n'.format(t, ctx.author, info))
                file.close()
            await ctx.send('Ban logged, view with `;bans`')
            time.sleep(1.75)
            await ctx.channel.purge(limit=2)

    @commands.command()
    async def bans(self, ctx):
        if ctx.guild.id == 833745752827887616:
            list = ''
            with open('./textlogs/Bans.txt', 'r') as file:
                for line in file:
                    list += f'{line}\n'
            embed = discord.Embed(description='**Bans:**')
            embed.add_field(name='Oldest -> Newest:', value=list)
            await  ctx.send(embed=embed)


#role = discord.utils.get(member.guild.roles, name='Muted')
#833745752827887616
def setup(client):
    client.add_cog(megacraft_(client))
