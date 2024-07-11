import discord
import discord.voice_client
from discord.ext import commands, tasks
from discord.utils import find, get
from random import randint
from datetime import datetime
import time
import json
import os
import subprocess

'''
    @tasks.loop(seconds=30)
    async def megacraft_reloader(self):
        self.client.unload_extension(f'cogs.megacraft')
        self.client.load_extension(f'cogs.megacraft')
        self.client.unload_extension(f'cogs.music')
        self.client.load_extension(f'cogs.music')
'''

class listeners(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.sfx_reloader.start()
        #self.megacraft_reloader.start()
        #self.ass_saver.start()
        self.nick_checker.start()
        #self.tester.start()

    @tasks.loop(seconds=5)
    async def sfx_reloader(self):
        self.client.unload_extension(f'cogs.joins')
        self.client.load_extension(f'cogs.joins')

    @tasks.loop(minutes=1)
    async def nick_checker(self):
        try:
            #print(self.client.activity)
            #await self.client.change_presence(activity=discord.Game(name='With The Void'))
            guild = self.client.get_guild(761652116375994448)
            user = guild.get_member(796467856677142530)
            n = user.display_name
            guild2 = self.client.get_guild(685930371149201491)
            user2 = guild2.get_member(796467856677142530)
            n2 = user2.display_name
            guild3 = self.client.get_guild(833745752827887616)
            user3 = guild3.get_member(796467856677142530)
            n3 = user3.display_name
            if n != "Giraffe's Test Subject" or n2 != "Giraffe's Test Subject" or n3 != "Giraffe's Test Subject":
                await user.edit(nick="Giraffe's Test Subject")
                await user2.edit(nick="Giraffe's Test Subject")
                #await user3.edit(nick="Giraffe's Test Subject")
        except:
            pass

    @tasks.loop(seconds=5)
    async def tester(self):
        #try:
        await self.client.wait_until_ready()
        guild = self.client.get_guild(761652116375994448)
        if guild.me.activity != 'with the void':
            await self.client.change_presence(activity=discord.Game(name='With The Void'))
        #except:
            #pass

    @tasks.loop(minutes=5)
    async def ass_saver(self):
        ct = datetime.now()
        times = [5, 6, 9, 10, 11, 12, 13, 14, 15]
        wednesday_times = [5, 6, 9, 10, 11, 12, 13, 14]
        days = [0, 1, 3, 4]
        if ct.weekday() in days and ct.hour in times:
            # try:
            #     os.system("taskkill/IM discord.exe /F")
            # except:
            #     pass
            try:
                subprocess.call(r"D:\Bot\Excess Stuff\Screen_off.bat")
            except:
                pass
        if ct.weekday() == 2 and ct.hour in wednesday_times:
            # try:
            #     os.system("taskkill/IM discord.exe /F")
            # except:
            #     pass
            try:
                subprocess.call(r"D:\Bot\Excess Stuff\Screen_off.bat")
            except:
                pass


    @commands.Cog.listener()
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self.client))
        # Normal Status:
        await self.client.change_presence(activity=discord.Game(name='With The Void'))
        # Guess who's back:
        #await self.client.change_presence(activity=discord.Game(name="Guess who's back...back, back again I am back tell a friend"))


        '''
        guild = self.client.get_guild(761652116375994448)
        user = guild.get_member(796467856677142530)
        n = user.display_name
        guild2 = self.client.get_guild(685930371149201491)
        user2 = guild2.get_member(796467856677142530)
        n2 = user2.display_name
        guild3 = self.client.get_guild(833745752827887616)
        user3 = guild3.get_member(796467856677142530)
        n3 = user3.display_name
        
        if n != "Giraffe's Test Subject" or n2 != "Giraffe's Test Subject" or n3 != "Giraffe's Test Subject":
            await user.edit(nick="Giraffe's Test Subject")
            await user2.edit(nick="Giraffe's Test Subject")
            await user3.edit(nick="Giraffe's Test Subject")

            print('Attempts are shown from here down:')
        '''
        # for emoji in self.client.emojis:
        #     print("Name:", emoji.name + ",", "ID:", emoji.id)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        general = find(lambda x: x.name == 'general', guild.text_channels)
        if not general:
            general = find(lambda x: x.name == '💬╿général', guild.text_channels)
        if general and general.permissions_for(guild.me).send_messages:
            entry = 'Hello {}!'.format(guild.name), 'My prefix is ";"'
            await general.send('Hello {}!, My prefix is ";"\nBe sure to run ;help for help with my setup and commands.'.format(guild.name))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        #guild = self.client.get_guild(761652116375994448)
        #channel = guild.get_channel(773661309777477672)
        if member.guild.id != 778654803617644544:
            channel = discord.utils.get(member.guild.channels, name="general")
            '''if not channel:
                channel = find(lambda x: x.name == '💬╿général', guild.text_channels)'''
        #if member.guild.id == 778654803617644544:
        #    channel = discord.utils.get(member.guild.channels, name="introduction")
        print('{} has joined {}.'.format(member, member.guild))
        '''if member.guild.id == 843558625854488588:
            await channel.send(f'Welcome {member.mention} to the Earth SMP, please make sure to checkout the "Getting started" category of channels and find the ip in #ip-and-dynmap')'''
        if not member.guild.id in [778654803617644544, 843558625854488588, 819385452493537280, 559119490571567106, 899889012259573771]:#Remove to turn on for other server, and un-hash the if statement above
            await channel.send(
            'Well Well Well, look who decided to show up\n{} has joined **{}**'.format(member.mention, member.guild))

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        #guild = self.client.get_guild(761652116375994448)
        #channel = guild.get_channel(773661309777477672)
        channel = discord.utils.get(member.guild.channels, name="general")
        '''if not channel:
            channel = find(lambda x: x.name == '💬╿général', guild.text_channels)'''
        print('{} has left {}.'.format(member, member.guild))
        if member.guild.id == 761652116375994448:
            await channel.send('Oh no...{} has left....Anyways'.format(member.mention))
        else:
            if not member.guild.id in [778654803617644544, 559119490571567106, 819385452493537280]:
                 await channel.send(f'{member.mention} has left us...')


    @commands.Cog.listener()
    async def on_message(self, message):
        user = message.author.mention
        if message.author.id != 204255221017214977 and 437808476106784770 and 159985870458322944 and 234395307759108106 and 414925323197612032 and 270904126974590976 and 266624760782258186:
            if message.guild.id == 761652116375994448:
                if message.author == self.client.user and message.channel.id not in [791359435037212672, 813477397772238858, 813477437798744085, 806531215762653204]:
                    with open('./TextLogs/BotLog.txt', 'a') as file:
                        file.write('{}\n'.format(message.author))
                        file.close()
                # if message.author.bot: return
                # if message.channel.id == 791359435037212672: return
                if not message.author.bot and message.channel.id not in [791359435037212672, 761676002366586881, 806531215762653204]:
                    # spam exception : , 763072814651277406]:
                    if message.author.id != 377862119112179712:
                        with open('./TextLogs/ActivityLog.txt', 'a') as file:
                            file.write('{}\n'.format(message.author))
                            file.close()
                        # print(message.author.name)
                        # with open('./TextLogs/ActivityLog.json', 'w+') as file:
                        #     l = json.load(file)
                        #     r = open('./TextLogs/ActivityLog.json', 'w')
                        #     await message.channel.send(l)
                        #     user = str(message.author.name)
                        #     if f'{user}' not in l:
                        #         l[user] = 1
                        #         file.write(json.dumps(l, indent=1))
                        #     else:
                        #         l[user] += 1
                        #         file.write(json.dumps(l, indent=1))
                        #     #r.close()

                    if message.author.id == 377862119112179712:
                        with open('./TextLogs/ActivityLog.txt', 'a') as file:
                            file.write('Wobbles\n')
                            file.close()
                    if message.author.id == 256087251992313857:
                        with open('./TextLogs/ActivityLog.txt', 'a') as file:
                            file.write('Ryan\n')
                            file.close()
        elif message.content == "Are you sure that's your code? Link codes are 4 numbers long.":
            await message.delete()

        else:
            pass
        if "asdfrg" in message.content:
            if message.author.guild_permissions.administrator:
                await message.channel.send('asdfrg')
        if message.author.id != 796467856677142530:
            if message.channel.id in [802288407749328916, 916769356275400755]:
                await message.add_reaction('\N{Thumbs Up Sign}')
                await message.add_reaction('\N{Thumbs Down Sign}')



            '''if message.author.id != 796467856677142530:
                if "triggered" in message.content:
                    await message.channel.send(''Hah {} you are:\nhttps://tenor.com/view/triggered-angry-mad-gif-12026482''.format(user))
            '''
            if message.author.id == 747838795704959027:
                await message.channel.send('Praise him')
                await message.channel.send('Praise him')

            if '4:20' in message.content:
                if 'https' not in message.content:
                    if '>' not in message.content:
                        await message.channel.send('4:20 YAY!!!!')
            if '420' in message.content:
                if 'https' not in message.content:
                    if '>' not in message.content:
                        await message.channel.send('420, Noice')
            if '69' in message.content:
                if 'https' not in message.content:
                    if '>' not in message.content:
                        await message.channel.send('69, Noice')
            '''
            if 'whats 9+10' in message.content or "What's 9+10" in message.content or "what's 9+10" in message.content or "Whats 9+10" in message.content:
                if 'https' not in message.content:
                    if '>' not in message.content:
                        await message.channel.send('21? IDK, I stupid')
            if ' 21' in message.content:
                if 'https' not in message.content:
                    if '>' not in message.content:
                        if '217' not in message.content:
                            await message.channel.send('21? You stupid')
            '''
            if '68+1' in message.content:
                if 'https' not in message.content:
                    if '>' not in message.content:
                        await message.channel.send('69, Noice')

            if 'ahoy ladies' in message.content:
                await message.channel.send('https://tenor.com/view/steve-joe-kerry-scoop-ahoy-ahoy-stranger-things-gif-17227867')
            if 'ahoy laddies' in message.content:
                await message.channel.send('https://tenor.com/view/steve-joe-kerry-scoop-ahoy-ahoy-stranger-things-gif-17227867')
            if 'Ahoy ladies' in message.content:
                await message.channel.send('https://tenor.com/view/steve-joe-kerry-scoop-ahoy-ahoy-stranger-things-gif-17227867')
            if 'Ahoy laddies' in message.content:
                await message.channel.send('https://tenor.com/view/steve-joe-kerry-scoop-ahoy-ahoy-stranger-things-gif-17227867')
            if 'Ahoy Ladies' in message.content:
                await message.channel.send('https://tenor.com/view/steve-joe-kerry-scoop-ahoy-ahoy-stranger-things-gif-17227867')
            if 'Ahoy Laddies' in message.content:
                await message.channel.send('https://tenor.com/view/steve-joe-kerry-scoop-ahoy-ahoy-stranger-things-gif-17227867')

            rr = randint(1, 14986)
            if rr == 420:
                await message.channel.send('Hah get rolled\nhttps://tenor.com/view/rickroll-gif-20044935')


        #Outside of the self loop but fits with the above area
        if 'ahoy' in message.content:
            al = self.client.get_emoji(821148094670438480)
            await message.add_reaction(al)
        if 'Ahoy' in message.content:
            al = self.client.get_emoji(821148094670438480)
            await message.add_reaction(al)
        if 'pog' in message.content or 'Pog' in message.content:
            if message.guild.id in [879108434904100896, 761652116375994448]:
                hank_pog = self.client.get_emoji(877201142893916160)
                await message.add_reaction(hank_pog)


    

def setup(client):
    client.add_cog(listeners(client))
