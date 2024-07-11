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

class best_hits(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild.id == 761652116375994448:
            if message.author.id != 796467856677142530:
                if message.channel.id == 866314750052401172:
                    if "est hit" in message.content:
                        if "oiyo" in message.content:
                            with open('./TextLogs/BestHits/Boiyo.txt', 'r', encoding="utf8") as quotes:
                                list = ""
                                for line in quotes:
                                    list += f'{line}'
                                await message.channel.send(f"Boiyo's best hits have to be:\n{list}")

                        '''if "orin" in message.content:
                            with open('./TextLogs/BestHits/Corin.txt', 'r') as quotes:
                                list = ""
                                for line in quotes:
                                    list += f'{line}'
                                await message.channel.send(f"Corin's best hits have to be:\n{list}")
'''
                        if "anni" in message.content:
                            with open('./TextLogs/BestHits/Danni.txt', 'r') as quotes:
                                list = ""
                                for line in quotes:
                                    list += f'{line}'
                                await message.channel.send(f"Danni's best hits have to be:\n{list}")

                        if "ecko" in message.content:
                            with open('./TextLogs/BestHits/Gecko.txt', 'r') as quotes:
                                list = ""
                                for line in quotes:
                                    list += f'{line}'
                                await message.channel.send(f"Gecko's best hits have to be:\n{list}")

                        if "iraffe" in message.content:
                            with open('./TextLogs/BestHits/Giraffe.txt', 'r') as quotes:
                                list = ""
                                for line in quotes:
                                    list += f'{line}'
                                await message.channel.send(f"Giraffe's best hits have to be:\n{list}")

                        if "ack" in message.content:
                            with open('./TextLogs/BestHits/Jack.txt', 'r') as quotes:
                                list = ""
                                for line in quotes:
                                    list += f'{line}'
                                await message.channel.send(f"Jack's best hits have to be:\n{list}")

                        if "oe" in message.content:
                            with open('./TextLogs/BestHits/Joe.txt', 'r') as quotes:
                                list = ""
                                for line in quotes:
                                    list += f'{line}'
                                await message.channel.send(f"Joe's best hits have to be:\n{list}")

                        if "unar" in message.content:
                            with open('./TextLogs/BestHits/Lunar.txt', 'r') as quotes:
                                list = ""
                                for line in quotes:
                                    list += f'{line}'
                                await message.channel.send(f"Lunar's best hits have to be:\n{list}")

                        if "nea" in message.content or "NEA" in message.content or "yler" in message.content or "Nea" in message.content:
                            with open('./TextLogs/BestHits/NEA.txt', 'r') as quotes:
                                list = ""
                                for line in quotes:
                                    list += f'{line}'
                                await message.channel.send(f"NEA's best hits have to be:\n{list}")

                        if "tar" in message.content or "azer" in message.content or "en" in message.content:
                            with open('./TextLogs/BestHits/Star.txt', 'r') as quotes:
                                list = ""
                                for line in quotes:
                                    list += f'{line}'
                                await message.channel.send(f"Star's best hits have to be:\n{list}")

                        if "box" in message.content:
                            with open('./TextLogs/BestHits/Xbox.txt', 'r') as quotes:
                                list = ""
                                for line in quotes:
                                    list += f'{line}'
                                await message.channel.send(f"Xbox's best hits have to be:\n{list}")


    @commands.command()
    async def quote(self, ctx, person, *, args):
        if ctx.author.guild_permissions.administrator:
            with open(f'./TextLogs/BestHits/{person}.txt', 'a') as file:
                quote ='\n'
                for word in args:
                    quote += word
                file.write(quote)
                await ctx.send('Quote added')
                await asyncio.sleep(4)
                await ctx.channel.purge(limit=2)
        else:
            ctx.send("You aren't authorised to do that")

def setup(client):
    client.add_cog(best_hits(client))
