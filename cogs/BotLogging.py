import logging
import discord
import discord.voice_client
from discord.ext import commands
from discord.utils import find, get
from random import randint
import time
import datetime
import json

class logging_listeners(commands.Cog):

    def __init__(self, client):
        self.client = client

    channel = ['logs', 'logging']

    @commands.Cog.listener()
    async def on_member_join(self, member):
        logging = discord.utils.get(member.guild.channels, name="logging")
        if not logging:
            logging = discord.utils.get(member.guild.channels, name="logs")
        t = datetime.datetime.now()
        t = t.strftime('%X')

        embed = discord.Embed(description=f'Member joined', color=0x1eff00)
        embed.set_author(name=f"{member}",
                         icon_url=f"{member.avatar.url}")
        embed.set_footer(text=f"Time: {t}")
        if logging:
            await logging.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        logging = discord.utils.get(member.guild.channels, name="logging")
        if not logging:
            logging = discord.utils.get(member.guild.channels, name="logs")
        t = datetime.datetime.now()
        t = t.strftime('%X')

        embed = discord.Embed(description=f'Member left', color=0x9e0000)
        embed.set_author(name=f"{member}",
                         icon_url=f"{member.avatar.url}")
        embed.set_footer(text=f"Time: {t}")
        if logging:
            await logging.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_ban(self, guild, member):
        async for entry in guild.audit_logs(action=discord.AuditLogAction.ban, limit=1):
        #logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.ban).flatten()
        #logs = logs[0]
            logging = discord.utils.get(guild.channels, name="logging")
            if not logging:
                logging = discord.utils.get(guild.channels, name="logs")
            t = datetime.datetime.now()
            t = t.strftime('%X')

            embed = discord.Embed(description=f'Member banned', color=0x9900ff)
            embed.set_author(name=f"{member}",
                             icon_url=f"{member.avatar.url}")
            embed.add_field(name='Moderator', value=entry.user)
            embed.add_field(name='Reason', value=entry.reason)
            embed.set_footer(text=f"Time: {t}")
            if logging:
                await logging.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_unban(self, guild, member):
        logging = discord.utils.get(guild.channels, name="logging")
        if not logging:
            logging = discord.utils.get(guild.channels, name="logs")
        t = datetime.datetime.now()
        t = t.strftime('%X')

        embed = discord.Embed(description=f'Member unbanned', color=0x00b3ff)
        embed.set_author(name=f"{member}",
                         icon_url=f"{member.avatar.url}")
        embed.set_footer(text=f"Time: {t}")
        if logging:
            await logging.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.content != after.content:
            if before.author.id not in [234395307759108106, 936929561302675456, 432610292342587392]:
                if before.channel.name not in ['logging', 'giraffes-development-lab', 'logs']:
                    logging = discord.utils.get(before.guild.channels, name="logging" or 'logs')
                    if not logging:
                        logging = discord.utils.get(before.guild.channels, name="logs")
                    t = datetime.datetime.now()
                    t = t.strftime('%X')
                    c = before.channel.mention

                    embed = discord.Embed(description=f'Message edited in {c}', color=0xff9500)
                    embed.set_author(name=f"{before.author}",
                                         icon_url=f"{before.author.avatar.url}")
                    embed.add_field(name='Original:', value=f'{before.content}')
                    embed.add_field(name='Edited:', value=f'{after.content}', inline=False)
                    embed.set_footer(text=f"Time: {t}")
                    if logging:
                        await logging.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.id not in [234395307759108106, 936929561302675456, 432610292342587392] and message.channel.name not in ['logging', 'giraffes-development-lab', 'logs']:
            logging = discord.utils.get(message.guild.channels, name="logging" or 'logs')
            if not logging:
                logging = discord.utils.get(message.guild.channels, name="logs")
            #logging = find(lambda x: x.name == 'logging', message.guild.text_channels)
            #logging = discord.utils.get(self.client.get_all_channels(), guild__name=message.guild.name, name='logging')
            t = datetime.datetime.now()
            t = t.strftime('%X')
            c = message.channel.mention

            embed = discord.Embed(description=f'Message deleted in {c}', color=0x9e0000)
            embed.set_author(name=f"{message.author}",
                                 icon_url=f"{message.author.avatar.url}")
            if message.content:
                embed.add_field(name='Message:', value=f'{message.content}', inline=False)
            try:
                if message.attachments[0]:
                    try:
                        embed.set_image(url=message.attachments[0].proxy_url)
                    except:
                        pass
            except IndexError:
                pass
            embed.set_footer(text=f"Time: {t}")
            if logging:
                await logging.send(embed=embed)

    @commands.Cog.listener()
    async def on_bulk_message_delete(self, messages):
        logging = False
        if messages[0].channel.name not in ['logging', 'giraffes-development-lab', 'logs']:
            logging = discord.utils.get(messages[0].guild.channels, name="logging")
        if not logging:
            logging = discord.utils.get(messages[0].guild.channels, name="logs")
        if logging:
            t = datetime.datetime.now()
            t = t.strftime('%X')
            c = messages[0].channel.mention
            ms = ''
            num = 0
            for i in range(0, (len(messages))):
                if '@' in messages[num].content:
                    messages[num].content = messages[num].content.replace('@', '')
                ms += f'{messages[num].author} : {messages[num].content}\n'
                num += 1
                if len(ms) > 1500:
                    await logging.send(f'''Messages deleted in {messages[0].channel.mention}:\n \n{ms}''')
                    ms = ""
            if logging:
                await logging.send(f'''Messages deleted in {messages[0].channel.mention}:\n \n{ms}''')

    @commands.Cog.listener() #Nick Change check
    async def on_member_update(self, before, after):
        #print('test')
        logging = discord.utils.get(before.guild.channels, name="logging")
        if not logging:
            logging = discord.utils.get(before.guild.channels, name="logs")
        t = datetime.datetime.now()
        t = t.strftime('%X')
        #print(hasattr(before, 'nick'), hasattr(after, 'nick'))
        if hasattr(before, 'nick') or hasattr(after, 'nick'):
            if before.nick != after.nick:
                embed = discord.Embed(description=f'Member Changed Nickname')
                embed.add_field(name= 'Old:', value= before.nick)
                embed.add_field(name= 'New:', value= after.nick)
                embed.add_field(name= 'ID:', value= before.id, inline=False)
                embed.set_author(name=f"{before.name}",
                                 icon_url=f"{before.avatar.url}")
                embed.set_footer(text=f"Time: {t}")
                if logging:
                    await logging.send(embed=embed)

    @commands.Cog.listener() #Name Change check
    async def on_user_update(self, before, after):
        #print('test')
        guild = self.client.get_guild(915014434546659360)
        logging = discord.utils.get(guild.channels, name="logging")
        if not logging:
            logging = discord.utils.get(guild.channels, name="logs")
        t = datetime.datetime.now()
        t = t.strftime('%X')
        #print(hasattr(before, 'nick'), hasattr(after, 'nick'))
        if hasattr(before, 'name') or hasattr(after, 'name'):
            if before.name != after.name:
                embed = discord.Embed(description=f'Member Changed Username')
                embed.add_field(name= 'Old:', value= f'{before.name}#{before.discriminator}')
                embed.add_field(name= 'New:', value= f'{after.name}#{after.discriminator}')
                embed.add_field(name= 'ID:', value= before.id, inline=False)
                embed.set_author(name=f"{before.name}",
                                 icon_url=f"{before.avatar.url}")
                embed.set_footer(text=f"Time: {t}")
                if logging:
                    await logging.send(embed=embed)


async def setup(client):
    await client.add_cog(logging_listeners(client))
