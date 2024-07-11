import os
import datetime
import asyncio
import time
from random import randint
from discord.ext import commands
import discord

class spareCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief = 'Run this command to find out how the bot is feeling')
    async def feeling(self, cxt):
        choice = (randint(1,3))
        if choice == 1:
            await cxt.send('I wanna jump off of a cliff')
        elif choice == 2:
            await cxt.send("I'm feeling good, thank you for asking")
        elif choice == 3:
            await cxt.send('Better than you boiii')

    @commands.command()
    async def suggest(self, ctx, *, sug):
        t = datetime.datetime.now()
        t = t.strftime('%c')
        suggestion = ''
        for word in sug:
            suggestion += word
        print('{}: {} : {}'.format(t, ctx.author, suggestion))
        with open('./TextLogs/Suggestions.txt', "a") as file:
            file.write('{}: {} : {}\n'.format(t, ctx.author, suggestion))
            file.close()
        await ctx.send('Thank you for your suggestion, I really appreciate the help with this project of mine')
        time.sleep(1.75)
        await ctx.channel.purge(limit=2)

    @commands.command()
    async def reviews(self, ctx):
        await ctx.send(
            'The link to the website of our resident film reviewer Glider is:\nhttps://lukeplusfilms.wixsite.com/my-site')
    
    @commands.command(aliases=['Musician'])
    async def musician(self, ctx):
        await ctx.send(
            'The link to the website of our resident musician Joe is:\nhttps://montanajoe.bandcamp.com/')

    @commands.command()
    async def spammer(self, ctx):
        if ctx.author.guild_permissions.administrator:
            for f in range(0, 550):
                time.sleep(0.5)
                await ctx.send('Nothing to see here')
                print(f)

    @commands.command()
    async def LastResort(self, ctx):
        #if ctx.author.guild_permissions.administrator:
        if ctx.author.id in [230442733234421760, 345982989957726210]:
            giraffe = ctx.guild.get_member(230442733234421760)
            await ctx.send(f"I'm Being shot by the firing squad again.... {giraffe.mention}")
            await ctx.send(giraffe.mention)
            await ctx.send(giraffe.mention)
            import sys
            sys.exit()

    @commands.command()
    async def praise(self, ctx):
        if ctx.author.guild_permissions.administrator:
            guild = self.client.get_guild(761652116375994448)
            user = guild.get_member(747838795704959027)
            for f in range(0, 550):
                await asyncio.sleep(1)
                await ctx.send('Praise {}....Praise him!!'.format(user.mention))
                await asyncio.sleep(1)
                await ctx.send('Praise {}....Praise him!!'.format(user.mention))

    @commands.command()
    async def heathen(self, ctx):
        if ctx.author.guild_permissions.administrator:
            guild = self.client.get_guild(761652116375994448)
            user = guild.get_member(302184774456311809)
            for f in range(0, 100):
                await asyncio.sleep(1)
                await ctx.send('Speaketh heathen!!! {}'.format(user.mention))
                await asyncio.sleep(1)
                await ctx.send('Speaketh heathen!!! {}'.format(user.mention))

    @commands.command(pass_context=True, aliases=['-;'])
    async def emojiresponse(self, ctx):
        if ctx.author != self.client.user:
            await ctx.send(';-;')

    @commands.command(pass_context=True, aliases=[')'])
    async def emojiresponse2(self, ctx):
        if ctx.author != self.client.user:
            await ctx.send(';)')

    @commands.command()
    async def teamviewerReset(self, ctx):
        await ctx.send('Please wait while teamviewer is closed')
        os.system("taskkill/IM TeamViewer.exe /F")
        await asyncio.sleep(6)
        os.startfile(r"C:\Users\Public\\temp\TeamViewer\TeamViewer.exe")
        await asyncio.sleep(2)
        await ctx.send('Team Viewer should be starting up now give it a moment')
    
    @commands.command()
    async def pfp(self, ctx, *person:discord.Member):
        print(person)
        if person:
            person = person[0]
        if not person:
            person = ctx.author
        embed = discord.Embed(description='Your Profile Picture:')
        print(person)
        embed.set_image(url=person.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def lpfp(self, ctx):
        if ctx.author.id == 230442733234421760:
            guild = self.client.get_guild(819385452493537280)
            levi = guild.get_member(345982989957726210)
            embed = discord.Embed(description='Your Profile Picture:')
            embed.set_image(url=levi.avatar_url)
            await ctx.send(embed=embed)

    @commands.command()
    async def welcome(self, ctx):
        if ctx.guild.id == 761652116375994448:
            await ctx.send('A Welcome to the Ladiesman Discord Server...', file=discord.File(f'./Audio/Images/Server_Welcome.PNG'))

    @commands.command()
    async def servers(self, ctx):
        s = ''
        for f in self.client.guilds:
            s += f.name
            s += '\n'
        await ctx.send(s)

    @commands.command()
    async def leave(self, ctx):
        for f in self.client.guilds:
            if f.id == 848669966593294336:
                #s = self.client.get_guild(848669966593294336)
                await f.leave()

def setup(client):
    client.add_cog(spareCommands(client))
