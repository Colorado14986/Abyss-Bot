import discord
import discord.voice_client
from discord.ext import commands
import datetime

class raidPrevention(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        list = message.content.split()
        num = 0
        for f in list:
            if "<@" in f:
                num += 1
            if num == 8 and message.guild.id in [761652116375994448, 768128590763393025]:
                await message.author.ban(reason="You are most likely a raid bot, due to the 7 pings you sent in a single message", delete_message_days=1)
                general = discord.utils.get(message.guild.channels, name="general")
                await message.channel.send(f"{message.author.mention} has been banned for likely being a spam bot")


def setup(client):
    client.add_cog(raidPrevention(client))