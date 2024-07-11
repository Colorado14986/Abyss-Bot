import discord
import discord.voice_client
from discord.ext import commands
import datetime

class raidPrevention(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.name == "ParadoxofNaturesIS" or member.name == "Hyss-Ho":
            await member.ban()            
        

    @commands.Cog.listener()
    async def on_message(self, message):
        list = message.content.split()
        num = 0
        for f in list:
            if "<@" in f:
                num += 1
            if num >= 8 and message.guild.id in [761652116375994448, 768128590763393025, 915014434546659360]:
                await message.author.ban(reason="You are most likely a raid bot, due to the 7 pings you sent in a single message", delete_message_days=1)
                general = discord.utils.get(message.guild.channels, name="general")
                await message.channel.send(f"{message.author.mention} has been banned for likely being a spam bot")
        if 'OPENSEA' in message.content and 'mint' in message.content:
            await message.author.ban(reason="NFT Scammer", delete_message_days=5)


async def setup(client):
    await client.add_cog(raidPrevention(client))
