import os
import youtube_dl
import discord
import asyncio
import discord.voice_client
from pytube import YouTube
from discord.ext import commands
from discord.utils import find, get
from random import randint

class GeckoCommands_(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['gecko_bonk'])
    async def bonk_gecko(self, ctx):
        with open('./TextLogs/Gecko_Bonks.txt', 'r') as file:
            for line in file:
                number = int(line)
                number += 1
        with open('./TextLogs/Gecko_Bonks.txt', 'w') as file:
            file.write(str(number))
        bonk = self.client.get_command('bonk')
        try:
            await ctx.invoke(bonk)
        except:
            pass
        if ctx.guild.id == 778654803617644544:
            try:
                Gecko = ctx.guild.get_member(83897138240585728)
                await asyncio.sleep(1)
                jail = ctx.guild.get_channel(866135351050240050)
                await Gecko.move_to(jail)
            except:
                return
    @commands.command()
    async def gbonks(self, ctx):
        with open('./TextLogs/Gecko_Bonks.txt', 'r') as file:
            for line in file:
                number = int(line)
        await ctx.send(f'Gecko has been bonked {number} times')

    @commands.command()
    async def cum(self, ctx):
        if ctx.guild.id == 348294717798219776:
            await ctx.send('||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _ <@165242196088455168>')

def setup(client):
    client.add_cog(GeckoCommands_(client))
