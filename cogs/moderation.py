import discord
import time
import datetime
import discord.voice_client
from discord.ext import commands
import asyncio
import os
import inspect

class mod_commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def Restart(self, ctx):
        if ctx.author.id in [230442733234421760, 418087030950723606, 689876697918865421]:
            os.startfile(r"C:\Bot\Bot Runner.bat")
            await ctx.send('Bot restarted')
            await asyncio.sleep(2)
            import sys
            sys.exit()

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
    async def delid(self, ctx, messageID):
        message = await ctx.channel.fetch_message(messageID)
        await message.delete()
        await ctx.message.delete()

    @commands.command()
    async def userpurge(self, ctx, amount, member:discord.Member):
        if ctx.author.guild_permissions.administrator:
            def is_target(msg):
                return msg.author.id == member.id
            await ctx.channel.purge(limit=int(amount), check=is_target)

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
    async def ban(self, ctx, member, *, reason=None):
        if ctx.author.guild_permissions.administrator or ctx.author.id == 230442733234421760:
            try:
                for char in "<@>":
                    member = member.replace(char, "")
            except:
                pass
            member = await self.client.fetch_user(int(member))
            await ctx.guild.ban(member, reason=reason)
            r = reason
            m = member
            if r == None:
                await ctx.send('{} has been banned with no reason given'.format(m.mention))
            elif r != None:
                await ctx.send('{} has been banned for {}'.format(m.mention, r))

        else:
            msg = "You're an average joe {0.author.mention}, you can't use that".format(ctx.message)
            await ctx.send(msg)

    # @commands.command()
    # async def mute(self, ctx, member: discord.Member):
    #     if ctx.author.guild_permissions.administrator or ctx.author.id == 230442733234421760:
    #         role = discord.utils.get(member.guild.roles, name='Muted')
    #         await member.add_roles(role)
    #         await ctx.send(
    #             '{} has been muted\n**Silence shall now fall**...for a while at least'.format(member.mention))
    #     else:
    #         msg = "You're an average joe {0.author.mention}, you can't use that".format(ctx.message)
    #         await ctx.send(msg)

    # @commands.command()
    # async def unmute(self, ctx, member: discord.Member):
    #     if ctx.author.guild_permissions.administrator or ctx.author.id == 230442733234421760:
    #         role = discord.utils.get(member.guild.roles, name='Muted')
    #         await member.remove_roles(role)
    #         await ctx.send('{} has been unmuted\nYou can do the speak now I guess'.format(member.mention))
    #     else:
    #         msg = "You're an average joe {0.author.mention}, you can't use that".format(ctx.message)
    #         await ctx.send(msg)

    @commands.command()
    async def warn(self, ctx, member:discord.Member, *reason):
        if ctx.guild.id == 915014434546659360:
            channel = self.client.get_channel(925526285378281492)
            reason_string = ""
            for f in reason:
                reason_string += f
                reason_string += " "
            t = datetime.datetime.now()
            t = t.strftime('%X')

            embed = discord.Embed(description=f'Member Warned', colour=0xFFA500)
            embed.set_author(name=f"{member}",
                            icon_url=f"{member.default_avatar.url}")
            embed.add_field(name='Moderator', value=ctx.author)
            embed.add_field(name='Reason:', value=reason_string, inline=False)
            embed.set_footer(text=f"Time: {t}")
            await ctx.message.delete()
            await channel.send(embed=embed)
            await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx, victim:discord.Member, amount:int):
        if not 0:
            if ctx.author.id == 230442733234421760 or ctx.author.id == 418087030950723606:
                for f in range (1, amount):
                    await ctx.send(f'OI! {victim.mention}')

    @commands.command(aliases=["inv"])
    async def invite(self, ctx,):
        embed = discord.Embed()
        embed.add_field(name="Invite me below:", value="[Click here](https://discord.com/api/oauth2/authorize?client_id=796467856677142530&permissions=8&scope=bot)")
        await ctx.send(embed=embed)

        
async def setup(client):
    await client.add_cog(mod_commands(client))
