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
import giphypop
import requests
from PyDictionary import PyDictionary


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
        await ctx.send(embed=embed)
        #definition = urbandict.define(query)
        #embed = discord.Embed(title=f'Search: {definition[0]["word"]}')
        #embed.add_field(name='Definition:', value=f'\n{definition[0]["def"]}')
        #embed.add_field(name='Example:', value=f'{definition[0]["example"]}', inline=False)
        #await ctx.send(embed=embed)
    
    @commands.command()
    async def dict(self, ctx, query):
        dict = PyDictionary()
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
    async def gif(self, ctx, *args):
        phrase = ''
        g = giphypop.Giphy()
        for word in args:
            phrase += word
            phrase += ' '
        gif = g.translate(phrase=phrase)
        if gif.media_url:
            embed = discord.Embed(description=f'Gif search for: {phrase}')
            embed.set_image(url=gif.media_url)
            await ctx.send(embed=embed)
        else:
            ctx.send('Something went wrong, please try again. If this does not fix the problem please use another search term')


    @commands.command()
    @commands.is_owner()
    async def speak(self, ctx, *Content):
        #await ctx.channel.purge(limit=1)
        await ctx.message.delete()
        reply = ''
        for f in Content:
            reply += f'{f} '
        await ctx.send(reply)

            
def setup(client):
    client.add_cog(fun_commands(client))
