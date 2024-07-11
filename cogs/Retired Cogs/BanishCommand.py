import os
import youtube_dl
import discord
import asyncio
import discord.voice_client
from pytube import YouTube
from discord.ext import commands
from discord.utils import find, get
from random import randint

class BanishCommand_(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        #if after.channel.name != 'The Void':
        try:
            if before.channel.name == 'The Void':
                guild = member.guild
                Void = find(lambda x: x.name == 'The Void', guild.voice_channels)
                opt = 0
                try:
                    opt = len(Void.channel_members)
                except:
                    pass
                voice = get(self.client.voice_clients, guild=member.guild)
                if len(Void.channel_members) == 0:
                    Void = find(lambda x: x.name == 'The Void', guild.voice_channels)
                    await Void.delete()
        except:
            return

    @commands.command(aliases=['banish'])
    async def Banish(self, ctx, player: discord.Member):
        guild = ctx.guild
        if player.id not in self.client.mobile_users:
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                guild.me: discord.PermissionOverwrite(read_messages=True)
            }
            channel = await guild.create_voice_channel('The Void', overwrites=overwrites)
            #general = find(lambda x: x.name == 'The Void', guild.text_channels)
            await player.move_to(channel)


    '''@commands.command()
    async def sleep(self, ctx):
        Boiyo = ctx.guild.get_member(418087030950723606)
        for f in range(0, 5):
            await self.client.send_message(Boiyo, "You said to tell you to Sleep")
'''

def setup(client):
    client.add_cog(BanishCommand_(client))
