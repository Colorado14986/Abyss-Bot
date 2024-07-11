import discord.voice_client
from pytube import YouTube
from random import randint
from discord.ext import commands
from discord.utils import find, get
import re


class dnd(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.dmSpeaking = False

    @commands.command()
    async def dmspeaking(self, ctx):
        if ctx.author.id == 230442733234421760 and self.dmSpeaking == False:
            self.dmSpeaking = True
            for member in ctx.author.voice.channel.members:
                if member.id != 230442733234421760:
                    await member.edit(mute=True)
            await ctx.send('https://tenor.com/view/alastor-hazbin-hotel-gif-26763497')

        elif ctx.author.id == 230442733234421760 and self.dmSpeaking == True:
            self.dmSpeaking = False
            for member in ctx.author.voice.channel.members:
                if member.id != 230442733234421760:
                    await member.edit(mute=False)
            await ctx.send('https://tenor.com/view/hazbin-hotel-alastor-pfp-gif-1879653440911491019')

    @commands.command()
    async def roll(self, ctx, *, args=""):
        if not re.match(r"[^dD\d\s]", args) and len(args) < 1000:
            dicePattern = r"(\d[\d]?[\d]?[\d]?[\d]?[\d]?[dD]\d[\d]?[\d]?[\d]?[\d]?[\d]?)"
            multPattern = r"[dD]"
            string = re.split(dicePattern, args)
            rolls = ''

            ind = 0
            for f in string:
                number = 0
                if re.match(dicePattern, f):
                    a = re.split(multPattern, f)
                    try:  
                        a[0] = int(a[0])
                        a[1] = int(a[1])
                        for e in range(0, a[0]):
                            rand = randint(1, a[1])
                            number += rand
                            if len(rolls) < 500:
                                rolls += f"{rand} "
                        string[ind] = str(number)
                    except:
                        continue

                ind += 1
            equation = ''.join(string)
            try:
                total = eval(equation)
                if total < 240:
                    embed = discord.Embed(title=f'Request: {args}')
                else:
                    embed = discord.Embed(title=f'Request:')
                if len(rolls) < 500:
                    embed.add_field(name='Rolls:', value=f'{rolls}', inline=False)
                else:
                    embed.add_field(name='Rolls:', value=f'Not enough space on the table', inline=False)
                if len(rolls) < 500:
                    embed.add_field(name='Results:', value=f'{equation}', inline=False)
                else:
                    embed.add_field(name='Results:', value=f'See above', inline=False)
                embed.add_field(name="Total", value=f"{total}")
                await ctx.send(embed=embed)
            except:
                await ctx.send("https://tenor.com/view/nouns-nounish-nounsdao-abacus-counting-gif-16562575250327679873")
        else:
            await ctx.send("https://tenor.com/view/blocked-nope-do-not-stop-ksi-gif-13628205")
        


async def setup(client):
    await client.add_cog(dnd(client))