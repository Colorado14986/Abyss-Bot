from urban import UrbanClient
import os
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
from random import randint
import json
import giphypop
import requests
from AyDictionary import AyDictionary
from bs4 import BeautifulSoup
import re

class fun_commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, aliases=['8ball', '8Ball', 'Eightball', '8b', '8B'])
    async def eightball(self, ctx):
        num = randint(0, 2)
        responses = ['Yes', 'No', 'Nah pal']
        if num == 0:
            await ctx.send(responses[num])
        if num == 1:
            await ctx.send(responses[num])
        if num == 2:
            await ctx.send(responses[num])

    @commands.command(pass_context=True, aliases=['def', 'ub', 'Define', 'Def'])
    async def define(self, ctx, *, search):
        query = ''
        for words in search:
            query += words
        client = UrbanClient()
        defs = client.get_definition(query)
        d = []
        e = []
        for i in defs:
            d.append(i.definition)
            e.append(i.example)
        d[0] = d[0].replace('[', '')
        d[0] = d[0].replace(']', '')
        e[0] = e[0].replace('[', '')
        e[0] = e[0].replace(']', '')
        embed = discord.Embed(title=f'Search: {query}')
        embed.add_field(name='Definition:', value=f'{d[0]}')
        embed.add_field(name='Example:', value=f'{e[0]}', inline=False)
        embed.add_field(name="If this isn't what you were looking for:", value="Feel free to try ;dict for an answer from a real dictionary rather than the urban kind")
        await ctx.send(embed=embed)
        #definition = urbandict.define(query)
        #embed = discord.Embed(title=f'Search: {definition[0]["word"]}')
        #embed.add_field(name='Definition:', value=f'\n{definition[0]["def"]}')
        #embed.add_field(name='Example:', value=f'{definition[0]["example"]}', inline=False)
        #await ctx.send(embed=embed)
    
    @commands.command()
    async def dict(self, ctx, query):
        dict = AyDictionary()
        meanings = dict.meaning(query)
        embed = discord.Embed(title=f'Dictionary search for {query}')
        try:
            limit_reached = 0
            if meanings['Noun']:
                Meanings_noun  = ''
                for f in meanings['Noun']:
                    if limit_reached == 0:
                        f = f.title()
                        if len(Meanings_noun) < 900:
                            Meanings_noun += f'-{f}\n'
                embed.add_field(name='Meanings as noun:', value = Meanings_noun)
        except:
              pass          
        try:
            limit_reached = 0
            if meanings['Verb']:
                Meanings_verb  = ''
                for f in meanings['Verb']:
                    if limit_reached == 0:
                        f = f.title()
                        if len(Meanings_verb) < 900:
                            Meanings_verb += f'-{f}\n'
                embed.add_field(name='Meanings as Verb:', value = Meanings_verb)
        except:
            pass
        embed.add_field(name="If this isn't what you were looking for:", value="Feel free to try ;def for an answer from the urban dictionary rather than the official kind", inline=False)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True, aliases=['wouldyourather', 'Wouldyourather', 'Wyr'])
    async def wyr(self, ctx):
        with open('./TextLogs/wyr_Questions.txt', 'r', encoding="utf8") as file:
            questions = []
            for line in file:
                questions.append(line)
            Q = randint(0, (len(questions)))
            embed = discord.Embed(title=f'Would you rather...')
            embed.add_field(name='\u200b', value=f'{questions[Q]}')
            msg = await ctx.channel.send(embed=embed)
            await msg.add_reaction('\N{Leftwards Black Arrow}')
            await msg.add_reaction('\N{Black Rightwards Arrow}')
            file.close()

    @commands.command(pass_context=True, aliases=['AFK'])
    async def afk(self, ctx):
        afk = False
        if ctx.author.display_name == 'AFK':
            afk = True
        if not afk:
            with open(f'./TextLogs/Nicks/[{ctx.guild.id}] {ctx.author.id}.json', 'w+') as file:
                n = {
                    'name' : f'{ctx.author.display_name}'
                }
                file.write(json.dumps(n, indent=0))
            await ctx.author.edit(nick='AFK')
            await ctx.author.edit(mute=True)
            await ctx.send('You are now listed as AFK and muted')

        if afk:
            with open(f'./TextLogs/Nicks/[{ctx.guild.id}] {ctx.author.id}.json', 'r') as file:
                f = file.read()
                Name = json.loads(f)
                Name = Name["name"]
            await ctx.author.edit(nick=Name)
            await ctx.author.edit(mute=False)
            await ctx.send('You are no longer listed as AFK and unmuted')

    @commands.command()
    @commands.is_owner()
    async def speak(self, ctx, *Content):
        #await ctx.channel.purge(limit=1)
        pattern = re.compile(r"\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d")
        # await ctx.send(Content)
        reply = ''
        channel = 0
        for f in Content:
            if pattern.match(f):
                channel = ctx.message.guild.get_channel(int(f))
            else:
                reply += f'{f} '
        if channel != 0:
            await channel.send(reply)
        else:         
            await ctx.message.delete()
            await ctx.send(reply)

    @commands.command()
    async def rsd(self, ctx):
        URL = "http://rsdb.org"
        r = requests.get(URL) 
        soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
        word = soup.find('div', attrs = {'class':'slur'})
        race = soup.find('div', attrs = {'class':'race'})
        details = soup.find('div', attrs = {'class':'details'})
        print((word.text.strip())) # type: ignore
        print(race.text.strip()) # type: ignore
        print(details.text.strip()) # type: ignore
        embed = discord.Embed(title='Racial slur of the day:')
        embed.add_field(name='Word:', value=word.text.strip()) # type: ignore
        embed.add_field(name='Race:', value=race.text.strip()) # type: ignore
        embed.add_field(name='Details:', value=details.text.strip(), inline=False) # type: ignore
        await ctx.send(embed=embed)


            
async def setup(client):
    await client.add_cog(fun_commands(client))
