import discord
import discord.voice_client
from discord.ext import commands
import datetime

class bumpCooldown(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if "Please wait" in message.embeds[0].description: # type: ignore
                for f in message.embeds[0].description.split():
                    try:
                        int(f)
                        time = datetime.datetime.now() + datetime.timedelta(minutes=int(f))
                        embed = discord.Embed(description=f'The next bump can be completed at <t:{int(time.timestamp())}:t> (This time changes depending on your time zone)')
                        await message.channel.send(embed=embed)
                    except ValueError:
                        pass
            if "Bump done!" in message.embeds[0].description:
                try:
                    time = datetime.datetime.now() + datetime.timedelta(minutes=120)
                    embed = discord.Embed(description=f'The next bump can be completed at <t:{int(time.timestamp())}:t> (This time is automatically correct to your timezone)')
                    await message.channel.send(embed=embed)
                except ValueError:
                    pass
        except:
            pass

    '''@commands.command()
    async def bump(self, ctx):
        await ctx.send(embed=discord.Embed(description='Bump done!'))'''

async def setup(client):
    await client.add_cog(bumpCooldown(client))
