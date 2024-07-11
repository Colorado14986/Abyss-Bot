import discord
import time
import discord.voice_client
from discord.ext import commands
import asyncio

class mod_commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, aliases=['Abusereport', 'modreport', 'Modreport', 'report', 'Report'])
    async def abusereport(self, ctx, *args):
        guild = self.client.get_guild(761652116375994448)
        lab = guild.get_channel(791359435037212672)
        report = ''
        for word in args:
            report += word
            report += ' '
        with open('./TextLogs/AbuseReports.txt', "a") as file:
            file.write('{} - {}\n \n'.format(ctx.author, report))
            file.close()
        print('Report made:\n{} - {}'.format(ctx.author, report))
        await lab.send('<@!230442733234421760> a report has been made...')
        await ctx.send('Thank you for your report, it will be reviewed soon and acted upon if needed')
        time.sleep(2)
        await ctx.channel.purge(limit=2)

    @commands.command()
    async def reports(self, ctx):
        with open('./TextLogs/AbuseReports.txt', "r") as file:
            f = ''
            for line in file:
                f += line
            await ctx.send(f)
            file.close()

    @commands.command(
        brief='Deletes messages in current channel between 1 and 100\nOnly available to those with the Administrator permission')
    async def purge(self, ctx, amount):
        amount = int(amount)
        amount += 1
        if ctx.author.guild_permissions.administrator or ctx.author.id == 230442733234421760:
            await ctx.channel.purge(limit=amount)
        else:
            msg = "You're an average joe {0.author.mention}, you can't use that".format(ctx.message)
            await ctx.send(msg)

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author.guild_permissions.administrator or ctx.author.id == 230442733234421760:
            await member.kick(reason=reason)
            r = reason
            m = member
            if r == None:
                await ctx.send('{} has been kicked with no reason given'.format(m.mention))
            elif r != None:
                await ctx.send('{} has been kicked for {}'.format(m.mention, r))

        else:
            msg = "You're an average joe {0.author.mention}, you can't use that".format(ctx.message)
            await ctx.send(msg)

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author.guild_permissions.administrator or ctx.author.id == 230442733234421760:
            await member.ban(reason=reason)
            r = reason
            m = member
            if r == None:
                await ctx.send('{} has been banned with no reason given'.format(m.mention))
            elif r != None:
                await ctx.send('{} has been banned for {}'.format(m.mention, r))

        else:
            msg = "You're an average joe {0.author.mention}, you can't use that".format(ctx.message)
            await ctx.send(msg)

    @commands.command()
    async def mute(self, ctx, member: discord.Member):
        if ctx.author.guild_permissions.administrator or ctx.author.id == 230442733234421760:
            role = discord.utils.get(member.guild.roles, name='Muted')
            await member.add_roles(role)
            await ctx.send(
                '{} has been muted\n**Silence shall now fall**...for a while at least'.format(member.mention))
        else:
            msg = "You're an average joe {0.author.mention}, you can't use that".format(ctx.message)
            await ctx.send(msg)

    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        if ctx.author.guild_permissions.administrator or ctx.author.id == 230442733234421760:
            role = discord.utils.get(member.guild.roles, name='Muted')
            await member.remove_roles(role)
            await ctx.send('{} has been unmuted\nYou can do the speak now I guess'.format(member.mention))
        else:
            msg = "You're an average joe {0.author.mention}, you can't use that".format(ctx.message)
            await ctx.send(msg)

    @commands.command()
    async def ping(self, ctx, victim:discord.Member, amount:int):
        #if ctx.guild.id == 761652116375994448:
        o = False
        # if victim.id == 488434417816043520:
        #     o = True
        #     for f in range (1, amount):
        #         await ctx.send(f'OI! {victim.mention}')
        if not 0:
            if ctx.author.id == 230442733234421760 or ctx.author.id == 418087030950723606:
                for f in range (1, amount):
                    await ctx.send(f'OI! {victim.mention}')


def setup(client):
    client.add_cog(mod_commands(client))
