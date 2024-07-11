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
import pypokedex
from pypokedex import exceptions as e
import requests
import json
from langdetect import detect
import goslate

class pokemon_(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.Pokeapi_Base_Url_Pokemon = "https://pokeapi.co/api/v2/pokemon"
        self.Pokeapi_Base_Url_Moves = "https://pokeapi.co/api/v2/move"

    @commands.command(aliases=['p'])
    async def pokemon(self, ctx, name=None, gender="m", shiny="n"):
        if name and gender in ['m', 'f', 'M', 'F'] and shiny in ['y', 'n', 'Y', 'N']:
            if gender.lower() == 'm':
                if shiny.lower() == 'y':
                    sprite = 'shiny'
                else:
                    sprite = 'default'
            elif gender.lower() == 'f':
                if shiny.lower() == 'y':
                    sprite = 'shiny_female'
                else:
                    sprite = 'female'
            try:
                Pokemon = pypokedex.get(name=name.lower()) #f'{self.Pokeapi_Base_Url_Pokemon}/{name}')
            except e.PyPokedexHTTPError:
                await ctx.send('Something went wrong, please try again. This may be due to spelling or it is possible the API is down right now.')

            if not Pokemon.sprites[0][sprite] and shiny.lower() == 'n':
                sprite = 'default'
            elif not Pokemon.sprites[0][sprite] and shiny.lower() == 'y':
                sprite = 'shiny'


            if Pokemon:
                moves = ''
                try:
                    p = requests.get(f'{self.Pokeapi_Base_Url_Pokemon}/{name.lower()}')
                    p = p.json()
                except requests.exceptions.RequestException:
                    await ctx.send('Something went wrong, please try again. This may be due to spelling or it is possible the API is down right now.')
                    return
                count = 0
                end = "  |  "
                g = 0
                for move in p['moves']:
                    i = len(moves) + len(p['moves'][count]['move']['name']) + 3
                    if i < 999:
                        p['moves'][count]['move']['name'] = p['moves'][count]['move']['name'].replace('-', ' ')
                        p['moves'][count]['move']['name'] = p['moves'][count]['move']['name'].capitalize()
                        moves += f"{p['moves'][count]['move']['name']}{end}"
                        f = end
                        count += 1
                        next = count + 1
                        g += 1
                        #if g == 2 or g == 3:
                        if f == "  |  " and g == 3:
                            g = 0
                            end = "\n"
                        else:
                            if f == "\n":
                                try:
                                    if p['moves'][next]['move']['name']:
                                        end = "  |  "
                                except:
                                    pass
                    else:
                        if not moves.endswith('\nToo many moves to fit:'):
                            moves += '\nToo many moves to fit:'

                abilities = ''
                for ability in p['abilities']:
                    abilities += f"{ability['ability']['name'].capitalize().replace('-', ' ')}\n"
                types = ''
                for type in p['types']:
                    types += f"{type['type']['name'].capitalize().replace('-', ' ')}\n"

                embed= discord.Embed(description=f'**{name.capitalize()}:**', color=0x9e0000)
                embed.set_thumbnail(url=Pokemon.sprites[0][sprite])
                embed.add_field(name='Basic info:', value=f"""Types:
{types}
Weight: \n~{format(p['weight']/10, '.01f')}kg
Height: \n~{format(p['height']/10, '.01f')}m""")

                embed.add_field(name='Base Stats:', value=f'''HP: {Pokemon.base_stats.hp}
Attack: {Pokemon.base_stats.attack}
SP Attack: {Pokemon.base_stats.sp_atk}
Defense: {Pokemon.base_stats.defense}
SP Defense: {Pokemon.base_stats.sp_def}
Speed: {Pokemon.base_stats.speed}\n''', inline=True)

                embed.add_field(name='Abilities:', value=abilities, inline=True)
                embed.add_field(name='\nMoves:', value=moves, inline=False)
                await ctx.send(embed=embed)

            else:
                await ctx.send('Something went wrong, please try again.')
        else:
            await ctx.send('Please follow the correct syntax as shown below inside of the <>\n``;pokemon <name> <m/f>(Gender) <y/n>(Shiny or not)``')

    @commands.command(aliases=['pm'])
    async def pmove(self, ctx, *args):
        query = ''
        if args:
            info = ''
            for word in args:
                query += word
                if len(args) > 1 and args[len(args)-1] != word:
                    query += '-'
            query = query.lower()
            try:
                move = requests.get(f'{self.Pokeapi_Base_Url_Moves}/{query}')
                move = move.json()
            except:
                await ctx.send('Something went wrong, please try again. This may be due to spelling or it is possible the API is down right now.')
                return
            try:
                if move['meta']['drain'] != 0:
                    info += f'Drain: {move["meta"]["drain"]}'
                if move['meta']['flinch_chance'] != 0:
                    info += f"Flinch Chance: {move['meta']['flinch_chance']}"
                if move['meta']['healing'] != 0:
                    info += f"Healing: {move['meta']['healing']}"
                if move['meta']['stat_chance'] != 0:
                    info += f"Status chance: {move['meta']['stat_chance']}"
            except:
                pass
            move_flavour_text = move['flavor_text_entries'][0]['flavor_text'].replace("\n", ' ')
            lang = detect(move_flavour_text)
            if lang != 'en':
                gs = goslate.Goslate()
                move_flavour_text = gs.translate(move_flavour_text , 'en')
            embed = discord.Embed(description=f'**{query.capitalize().replace("-", " ")}:**', color=0x9e0000)
            embed.add_field(name='Description:', value=f"""{move_flavour_text}
**Type:**
{move['type']['name'].capitalize()}
**Targetting Type:**
{move['target']['name'].replace("-", " ").capitalize()}
""")
            embed.add_field(name='Stats:', inline=False, value=f"""Accuracy: {move['accuracy']}
Power: {move['power']}
PP: {move['pp']}
{info}
""")
            await ctx.send(embed=embed)
            
        else:
            await ctx.send('Please follow the correct syntax as shown below inside of the <>\n``;pmove <name>``')


    @commands.command()
    async def moveset(self, ctx, name):
        moves = ''
        moves2= ''
        try:
            p = requests.get(f'{self.Pokeapi_Base_Url_Pokemon}/{name.lower()}')
            p = p.json()
        except requests.exceptions.RequestException:
            await ctx.send('Something went wrong, please try again. This may be due to spelling or it is possible the API is down right now.')
            return
        count = 0
        end = "  |  "
        g = 0
        
        for move in p['moves']:
                p['moves'][count]['move']['name'] = p['moves'][count]['move']['name'].replace('-', ' ')
                p['moves'][count]['move']['name'] = p['moves'][count]['move']['name'].capitalize()
                moves += f"{p['moves'][count]['move']['name']}{end}"
                f = end
                count += 1
                next = count + 1
                g += 1
                if f == "  |  " and g == 3:
                    g = 0
                    end = "\n"
                else:
                    if f == "\n":
                        try:
                            if p['moves'][next]['move']['name']:
                                end = "  |  "
                        except:
                            pass
        await ctx.send(f"{name.capitalize()}'s moveset is:\n{moves}")



async def setup(client):
    await client.add_cog(pokemon_(client))
