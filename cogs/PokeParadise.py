import discord
import discord.voice_client
from discord.ext import commands, tasks
from discord.utils import find, get
from random import randint
from PIL import Image, ImageDraw, ImageSequence, ImageFont
import io
import datetime
import time
import json
import os
import subprocess
import os, random
import asyncio



class PokeParadise_Server_Stuff(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.leaders = {
            931172935576735764 : 83897138240585728, #Shop:Gecko
            1000961711056105582 : 485869725297934337, #Daycare:Quinn
            1015881671574298674 : 1063857402199420929, #ArtNook:Slip

            1069049915625447424 : 302594311483031562, #gym1:Shear
            1069049842560663622 : 135412193435844609, #gym2:Joito
            1069049889805303878 : 701815691912806483, #gym3:Eddy
            1069049902019137636 : 906626822899392515, #gym4:SanSan
            1069049931144384563 : 1063857402199420929, #gym5:Slip
            1069049993991823380 : 200641158936920065, #gym6:Beg
            1069050007690424403 : 318018389727641600, #gym7:Gibura
            1069054334605729852 : 485869725297934337, #gym8:Quinn
            #e4
            1069050414835699812 : 270251264699269121, #e4-1:Rajang
            1069051231802237028 : 951561204625702912, #e4-2:Digital
            1069051222612529162 : 684631144590868487, #e4-3:Wooper
            1069051240178266213 : 110444955314454528, #e4-4:Sick
            1073376752258257017 : 110444955314454528 #Champion:Sick
        }

    '''@commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 915014434546659360:
            print(time.time() - member.created_at.timestamp())
            if time.time() - member.created_at.timestamp() < 259200:
                await member.ban(reason="You have been auto banned for being a suspicous account")
            elif time.time() - member.created_at.timestamp() > 259200 and time.time() - member.created_at.timestamp() < 2592000:
                await member.kick(reason="Your account is too young, you have been kicked automatically")
            else:
                pass'''
    
    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        if user.guild.id in [915014434546659360, 348294717798219776]:
            logging = discord.utils.get(user.guild.channels, name="logging")
            if not logging:
                logging = discord.utils.get(user.guild.channels, name="logs")
            if user.guild.id == 348294717798219776:
                logging = self.client.get_channel(754024303946891336)
            t = datetime.datetime.now()
            t = t.strftime('%X')
            embed = discord.Embed(description=f'Member removed reaction', color=0xd24e01)
            embed.set_author(name=f"{user}",
                            icon_url=f"{user.avatar.url}")
            embed.add_field(name='Emoji', value=reaction.emoji)
            embed.set_footer(text=f"Time: {t}")
            await logging.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild.id in [915014434546659360, 1094625349997953056, 789181743445573722]:
            if message.content.split(" ")[0] == ":ban" and "@everyone" not in message.content.lower() and "@here" not in message.content.lower():
                await message.channel.send(f'Billie has banned {message.content.split(" ")[1]}\n{message.content.split(" ")[1]} has left...')
            if message.content.split(" ")[0] == ":kick" and "@everyone" not in message.content.lower() and "@here" not in message.content.lower():
                await message.channel.send(f'Billie has kicked {message.content.split(" ")[1]}.....how rude is that.....poor {message.content.split(" ")[1]}')
            
#Muffin
        if message.guild.id == 915014434546659360 and message.author.id != 796467856677142530:
            role2 = discord.utils.get(message.guild.roles, name='Great')
            role3 = discord.utils.get(message.guild.roles, name='Ultra')
            role4 = discord.utils.get(message.guild.roles, name='Master')
            role5 = discord.utils.get(message.guild.roles, name='Beast')
            if "do you" in message.content.lower() and "alexander" in message.content.lower():
                if role2 not in message.author.roles and role3 not in message.author.roles and role4 not in message.author.roles and role5 not in message.author.roles:
                    await message.channel.send("Muffin, stop joining you will be banned on sight, this is getting ridiculous")
                    await asyncio.sleep(2)
                    await message.channel.send(f"And banned, goodbye {message.author.mention}")
                    await message.author.ban()

    @commands.command()
    async def roleless(self, ctx):
        role = discord.utils.find(lambda r: r.name == 'Trial Mod', ctx.message.guild.roles)
        if ctx.author.guild_permissions.administrator or role in ctx.author.roles:
            guild = ctx.author.guild
            for member in guild.members:
                if len(member.roles) == 1:
                    await member.kick(reason='They never found the rules')
                    await ctx.send(f'{member} was kicked')
            await ctx.send('Any roleless members were kicked')
    
    @commands.command()
    async def clean(self, ctx):
        def not_pinned(msg):
            return not msg.pinned
        try:
            if ctx.author.guild_permissions.administrator or self.leaders[ctx.channel.id] == ctx.author.id or ctx.author.id == 521207861846474772: #Scout for all
                await ctx.channel.purge(limit=500, check=not_pinned)
            else:
                msg = "This is not your channel, you hold no power here {0.author.mention}".format(ctx.message)
                await ctx.send(msg)
        except KeyError:
            msg = "This is not your channel, you hold no power here {0.author.mention}".format(ctx.message)
            await ctx.send(msg)


    @commands.command()
    async def bob(self, ctx, member:discord.Member):
        if ctx.author.guild_permissions.administrator or ctx.author.id == 626180555133812753:
            def is_target(msg):
                return msg.author.id == member.id
            role = discord.utils.get(member.guild.roles, name='Muted')
            await member.add_roles(role)
            await ctx.channel.purge(limit=50, check=is_target)

    @commands.command(aliases=["pos", "PoS"])
    async def muffin(self, ctx, member:discord.Member):
        role = discord.utils.get(member.guild.roles, name='Muted')
        role2 = discord.utils.get(member.guild.roles, name='Great')
        role3 = discord.utils.get(member.guild.roles, name='Ultra')
        role4 = discord.utils.get(member.guild.roles, name='Master')
        role5 = discord.utils.get(member.guild.roles, name='Beast')
        if role2 not in member.roles and role3 not in member.roles and role4 not in member.roles and role5 not in member.roles:
            #await member.add_roles(role)
            #await ctx.send(f"{member.mention} you have been suspected of being an alt of a recently banned user, as a temporary measure you have been muted for now, please wait a little bit while a mod checks you out \n||<@230442733234421760>||")
            def is_target(msg):
                return msg.author.id == member.id
            role = discord.utils.get(member.guild.roles, name='Muted')
            await member.add_roles(role)
            await ctx.channel.purge(limit=50, check=is_target)
            await ctx.send(f"{member.mention} you have been suspected of being an alt of a recently banned user, as a temporary measure you have been muted for now, please wait a little bit while a mod checks you out \n||<@230442733234421760>||")
            


    @commands.command()
    async def rule2(self, ctx):
        embed = discord.Embed(title='Here is Rule 2:', colour=0xff0000)
        embed.set_image(url="attachment://Rule.png")
        await ctx.send(file=discord.File("Images\PokeRules\Rule2.PNG", filename="Rule.png"), embed=embed)

    @commands.command()
    async def rule(self, ctx, number=None):
        if number != None:
            embed = discord.Embed(title=f'Here is Rule {number}:', colour=0xff0000)
            embed.set_image(url="attachment://Rule.png")
            await ctx.send(file=discord.File(f"Images\PokeRules\Rule{number}.PNG", filename="Rule.png"), embed=embed)
        else:
            embed = discord.Embed(title=f'Here are the rules:', colour=0xff0000)
            embed.set_image(url="attachment://Rule.png")
            await ctx.send(file=discord.File(f"Images\PokeRules\All.PNG", filename="Rule.png"), embed=embed)
        
    @commands.command()
    async def DisplayChampion(self, ctx, number, member:discord.Member, imageName, colour):
        colour = int(colour, 16)
        embed = discord.Embed(description=f'{number} Season Pokémon Paradise Server Champion', color=colour)
        embed.add_field(name= 'Name:', value=member.mention, inline=False)
        embed.set_image(url="attachment://Champion.png")
        await ctx.send(file=discord.File(f"Images\PokeChampions\{imageName}.png", filename="Champion.png"), embed=embed)
        await ctx.message.delete()

    @commands.command(aliases=["champion"])
    async def Champion(self, ctx):
        embed = discord.Embed(description=f'Current Pokémon Paradise Server Champion', color=0xb10d0d)
        embed.set_image(url="attachment://Champion.png")
        await ctx.send(file=discord.File(f"Images\PokeChampions\Sick.png", filename="Champion.png"), embed=embed)



    @commands.command()
    async def GreatBanishment(self, ctx):
        await ctx.send(f"{ctx.author.mention} has used Great Banishment and summoned forth the abyss to take those marked for it's grasp in their inactive state")
        await ctx.send("https://tenor.com/view/abyss-black-hole-galaxy-universe-gif-17715038")
        await ctx.send("Though your time here has come to an end for the moment, we wish you all luck with the mercy of the void you are entering")
        role = discord.utils.find(lambda r: r.name == 'Marked by the abyss', ctx.message.guild.roles)

        for member in ctx.message.guild.members:
            if role in member.roles:
                await member.kick(reason='Inactivity')
                await ctx.send(f'{member} fell into the abyss')
        await ctx.send('The portal has closed...')
        await ctx.send("For those still here, please be careful of any leftover void *stuff* in the area, who knows what it might do")
        await ctx.send("https://tenor.com/view/void-stuff-doctor-who-david-gif-5508554")

    @commands.command(aliases=["Tea", "Sweet"])
    async def tea(self, ctx):
        await ctx.send("https://tenor.com/view/loof-and-timmy-loof-tea-rex-tea-love-tea-lover-gif-25185105")

    @commands.command(aliases=["Billie"])
    async def billie(self, ctx):
        await ctx.send("https://tenor.com/view/australia-gif-18930796")
    
    @commands.command(aliases=["Wooper"])
    async def wooper(self, ctx):
        await ctx.send("https://tenor.com/view/marx-2219-meme-wow-yes-gif-22915194")

    @commands.command(aliases=["Vatik"])
    async def vatik(self, ctx):
        gifs = ["https://tenor.com/view/bear-sitting-down-park-bench-waiting-patient-gif-16359379", "https://tenor.com/view/bear-gif-20541523", "https://tenor.com/view/bear-gif-24467180", "https://tenor.com/view/bear-gif-24520429"]
        num = randint(0, 3)
        await ctx.send(gifs[num])

    @commands.command(aliases=["Hosney", "hos", "hodny", "Hodny"])
    async def hosney(self, ctx):
        gifs = ["https://tenor.com/view/doctor-who-david-tennant-gif-3530378", "https://tenor.com/view/doctor-who-matt-smith-doctor-who-gif-5876165", "https://tenor.com/view/doctor-who-snap-tardis-david-tennant-gif-17590283", "https://tenor.com/view/doctor-who-dr-who-smirk-david-tennant-gif-3888385", "https://tenor.com/view/doctor-who-matt-smith-excuse-me-try-to-keep-up-make-sense-gif-5065687", "https://tenor.com/view/doctorwho-mattsmith-eleven-lonely-gif-5139394", "https://tenor.com/view/11th-doctor-doctor-who-doctor-dancing-dance-bowties-are-cool-gif-18293437", "https://tenor.com/view/oh-yes-oh-yeah-omg-david-tennant-doctow-who-gif-16574020", "https://tenor.com/view/doctor-who-gif-19820227", "https://tenor.com/view/doctor-who-tenth-doctor-ten-hello-hi-gif-15454636", "https://tenor.com/view/doctor-who-dr-who-david-tennant-smile-laugh-gif-3963005", "https://tenor.com/view/doctor-who-wilf-wilfred-dance-gif-25199662", "https://tenor.com/view/oh-yes-right-correct-david-tennant-doctor-who-gif-9222745", "https://tenor.com/view/10th-doctor-smile-gif-20188335", "https://tenor.com/view/doctor-who-dr-who-falling-david-tennant-ten-gif-15450241", "https://tenor.com/view/tenth-doctor-doctor-who-well-gif-13782620", "https://tenor.com/view/raining-sad-david-tennant-doctor-who-tenth-doctor-gif-17689514", "https://tenor.com/view/raining-sad-david-tennant-doctor-who-tenth-doctor-gif-17689514", "https://tenor.com/view/doctor-who-david-tennant-peek-tenth-doctor-gif-16294517", "https://tenor.com/view/dr-who-doctor-who-matt-smith-universally-recognized-mature-gif-4692534", "https://tenor.com/view/tv-comedy-sci-fi-bbc-doctor-who-gif-3486254", "https://tenor.com/view/doctor-who-david-tennant-10th-doctor-tenth-doctor-this-is-fine-gif-18263861", "https://tenor.com/view/love-and-monsters-doctor-who-dr-who-tumblr-david-tennant-gif-21669604", "https://tenor.com/view/davidt-tennant-doctor-who-10-cake-celebrate-gif-17272016", "https://tenor.com/view/doctor-who-david-tennant-im-very-good-doctor-who-david-tennant-david-tennant-doctor-who-gif-24732635", "https://tenor.com/view/doctor-who-whovian-david-tennant-gif-8677190", "https://tenor.com/view/dr-who-doctor-who-david-tennant-frown-sad-gif-4433017", "https://tenor.com/view/doctor-who-ridiculous-crazy-daft-david-tennant-gif-7533162", "https://tenor.com/view/doctor-who-11th-doctor-matt-smith-dance-party-gif-3301416", "https://tenor.com/view/doctor-peter-capaldi-doctor-who-i-am-doctor-idiot-who-gif-4662557", "https://media.discordapp.net/attachments/791359435037212672/999433714180300830/300px-Movie2007_Mr_Hosney_quiet.gif", "https://tenor.com/view/thats-why-im-here-obi-wan-obi-wan-kenobi-star-wars-gif-18535648", "https://tenor.com/view/obi-wan-kenobi-jedi-master-star-wars-another-happy-landing-landing-gif-17180367", "https://tenor.com/view/so-uncivilised-gif-24177115", "https://tenor.com/view/doctor-who-whovian-tardis-david-tennant-gif-8051146", "https://tenor.com/view/buffy-angel-socializingisbrutal-whedon-gif-4588158", "https://tenor.com/view/allonsy-gif-13250108", "https://tenor.com/view/timeywimey-dr-who-david-tennant-gif-7863239", "https://tenor.com/view/10th-doctor-who-deal-with-it-gif-5990743", "https://tenor.com/view/mm9200-gif-22895005", "https://tenor.com/view/david-tennant-doctor-who-gif-8869753", "https://tenor.com/view/davidtennant-doctorwho-ten-judgingyou-gif-4812222", "https://tenor.com/view/doctorwho-live-people-time-davidtennant-gif-7336262", "https://tenor.com/view/doctor-who-tenth-doctor-gif-22356562", "https://tenor.com/view/ten-david-tennant-doctor-who-gif-5267793", "https://tenor.com/view/tenth-doctor-dont-do-that-doctor-who-gif-14870355", "https://tenor.com/view/bye-doctor-who-10th-doctor-tardis-gif-20389713", "https://tenor.com/view/tenth-doctor-tuxedo-ten-tenth-doctor-tuxedo-david-tennant-voyage-of-the-damned-gif-18012492", "https://tenor.com/view/doctor-who-dr-who-partners-in-crime-donna-noble-catherine-tate-gif-20329251", "https://tenor.com/view/doctor-who-davidtennant-gif-5751628", "https://tenor.com/view/yes-i-can-see-that-nodding-doctor-who-david-tennant-gif-16328165", "https://tenor.com/view/hope-gif-4531483", "https://tenor.com/view/possibly-go-wrong-doctor-10th-gif-26167384", "https://tenor.com/view/run-running-gtfo-do-not-want-doctor-who-gif-3782194", "https://tenor.com/view/doctor-who-matt-smith-happy-gif-11875772", "https://tenor.com/view/david-tennant-what-did-i-do-this-time-mistake-mistaken-wrong-gif-5739191", "https://tenor.com/view/david-tennant-doctor-who-tenth-gif-3414638", "https://tenor.com/view/doctor-who-dr-who-david-tennant-i-do-it-brilliantly-brilliant-gif-5051457", "https://tenor.com/view/tv-shows-dr-who-oh-this-is-brilliant-brilliant-gif-14859737", "https://tenor.com/view/doctorwho-howdidyoudothat-mattsmith-eleven-davidtennant-gif-5650308", "https://tenor.com/view/doctorwho-believe-ican-davidtennant-ten-gif-7659537", "https://tenor.com/view/doctor-who-whovian-peter-capaldi-gif-9361756", "https://tenor.com/view/doctorwho-doctor-dr-who-ten-gif-4654060"]
        length = len(gifs)-1 
        num = randint(0, length)
        await ctx.send(gifs[num])

    @commands.command(aliases=["Slip"])
    async def slip(self, ctx):
        gifs = ["https://tenor.com/view/11th-doctor-doctor-who-doctor-dancing-dance-bowties-are-cool-gif-18293437", "https://tenor.com/view/elmo-flames-burning-fire-gif-5342919", "https://tenor.com/view/cnft-cult-cnft-cult-gif-23185807", "https://tenor.com/view/oh-yes-oh-yeah-omg-david-tennant-doctow-who-gif-16574020", "https://tenor.com/view/doctor-who-gif-19820227", "https://tenor.com/view/doctor-who-tenth-doctor-ten-hello-hi-gif-15454636", "https://tenor.com/view/doctor-who-dr-who-david-tennant-smile-laugh-gif-3963005", "https://tenor.com/view/doctor-who-wilf-wilfred-dance-gif-25199662", "https://tenor.com/view/oh-yes-right-correct-david-tennant-doctor-who-gif-9222745", "https://tenor.com/view/10th-doctor-smile-gif-20188335", "https://tenor.com/view/doctor-who-dr-who-falling-david-tennant-ten-gif-15450241", "https://tenor.com/view/tenth-doctor-doctor-who-well-gif-13782620", "https://tenor.com/view/raining-sad-david-tennant-doctor-who-tenth-doctor-gif-17689514", "https://tenor.com/view/raining-sad-david-tennant-doctor-who-tenth-doctor-gif-17689514", "https://tenor.com/view/doctor-who-david-tennant-peek-tenth-doctor-gif-16294517", "https://tenor.com/view/dr-who-doctor-who-matt-smith-universally-recognized-mature-gif-4692534", "https://tenor.com/view/tv-comedy-sci-fi-bbc-doctor-who-gif-3486254", "https://tenor.com/view/doctor-who-david-tennant-10th-doctor-tenth-doctor-this-is-fine-gif-18263861", "https://tenor.com/view/love-and-monsters-doctor-who-dr-who-tumblr-david-tennant-gif-21669604", "https://tenor.com/view/davidt-tennant-doctor-who-10-cake-celebrate-gif-17272016", "https://tenor.com/view/doctor-who-david-tennant-im-very-good-doctor-who-david-tennant-david-tennant-doctor-who-gif-24732635", "https://tenor.com/view/doctor-who-whovian-david-tennant-gif-8677190", "https://tenor.com/view/dr-who-doctor-who-david-tennant-frown-sad-gif-4433017", "https://tenor.com/view/doctor-who-ridiculous-crazy-daft-david-tennant-gif-7533162", "https://tenor.com/view/doctor-who-11th-doctor-matt-smith-dance-party-gif-3301416", "https://tenor.com/view/doctor-peter-capaldi-doctor-who-i-am-doctor-idiot-who-gif-4662557", "https://tenor.com/view/thats-why-im-here-obi-wan-obi-wan-kenobi-star-wars-gif-18535648", "https://tenor.com/view/obi-wan-kenobi-jedi-master-star-wars-another-happy-landing-landing-gif-17180367", "https://tenor.com/view/so-uncivilised-gif-24177115", "https://tenor.com/view/doctor-who-whovian-tardis-david-tennant-gif-8051146"]
        length = len(gifs)-1
        num = randint(0, length)
        await ctx.send(gifs[num])

    class BRTB(discord.ui.View):
        @discord.ui.button(label="Ban", style=discord.ButtonStyle.danger)
        async def button_callback(self, interaction, button):
            gifs = ["https://tenor.com/view/11th-doctor-doctor-who-doctor-dancing-dance-bowties-are-cool-gif-18293437", "https://tenor.com/view/elmo-flames-burning-fire-gif-5342919", "https://tenor.com/view/cnft-cult-cnft-cult-gif-23185807", "https://tenor.com/view/oh-yes-oh-yeah-omg-david-tennant-doctow-who-gif-16574020", "https://tenor.com/view/doctor-who-gif-19820227", "https://tenor.com/view/doctor-who-tenth-doctor-ten-hello-hi-gif-15454636", "https://tenor.com/view/doctor-who-dr-who-david-tennant-smile-laugh-gif-3963005", "https://tenor.com/view/doctor-who-wilf-wilfred-dance-gif-25199662", "https://tenor.com/view/oh-yes-right-correct-david-tennant-doctor-who-gif-9222745", "https://tenor.com/view/10th-doctor-smile-gif-20188335", "https://tenor.com/view/doctor-who-dr-who-falling-david-tennant-ten-gif-15450241", "https://tenor.com/view/tenth-doctor-doctor-who-well-gif-13782620", "https://tenor.com/view/raining-sad-david-tennant-doctor-who-tenth-doctor-gif-17689514", "https://tenor.com/view/raining-sad-david-tennant-doctor-who-tenth-doctor-gif-17689514", "https://tenor.com/view/doctor-who-david-tennant-peek-tenth-doctor-gif-16294517", "https://tenor.com/view/dr-who-doctor-who-matt-smith-universally-recognized-mature-gif-4692534", "https://tenor.com/view/tv-comedy-sci-fi-bbc-doctor-who-gif-3486254", "https://tenor.com/view/doctor-who-david-tennant-10th-doctor-tenth-doctor-this-is-fine-gif-18263861", "https://tenor.com/view/love-and-monsters-doctor-who-dr-who-tumblr-david-tennant-gif-21669604", "https://tenor.com/view/davidt-tennant-doctor-who-10-cake-celebrate-gif-17272016", "https://tenor.com/view/doctor-who-david-tennant-im-very-good-doctor-who-david-tennant-david-tennant-doctor-who-gif-24732635", "https://tenor.com/view/doctor-who-whovian-david-tennant-gif-8677190", "https://tenor.com/view/dr-who-doctor-who-david-tennant-frown-sad-gif-4433017", "https://tenor.com/view/doctor-who-ridiculous-crazy-daft-david-tennant-gif-7533162", "https://tenor.com/view/doctor-who-11th-doctor-matt-smith-dance-party-gif-3301416", "https://tenor.com/view/doctor-peter-capaldi-doctor-who-i-am-doctor-idiot-who-gif-4662557", "https://tenor.com/view/thats-why-im-here-obi-wan-obi-wan-kenobi-star-wars-gif-18535648", "https://tenor.com/view/obi-wan-kenobi-jedi-master-star-wars-another-happy-landing-landing-gif-17180367", "https://tenor.com/view/so-uncivilised-gif-24177115", "https://tenor.com/view/doctor-who-whovian-tardis-david-tennant-gif-8051146"]
            length = len(gifs)-1
            num = randint(0, length)
            await interaction.response.send_message(gifs[num], ephemeral=True)

    @commands.command(aliases=["BRTB", "brtb"])
    async def button(self, ctx):
        gifs = ["https://tenor.com/view/11th-doctor-doctor-who-doctor-dancing-dance-bowties-are-cool-gif-18293437", "https://tenor.com/view/elmo-flames-burning-fire-gif-5342919", "https://tenor.com/view/cnft-cult-cnft-cult-gif-23185807", "https://tenor.com/view/oh-yes-oh-yeah-omg-david-tennant-doctow-who-gif-16574020", "https://tenor.com/view/doctor-who-gif-19820227", "https://tenor.com/view/doctor-who-tenth-doctor-ten-hello-hi-gif-15454636", "https://tenor.com/view/doctor-who-dr-who-david-tennant-smile-laugh-gif-3963005", "https://tenor.com/view/doctor-who-wilf-wilfred-dance-gif-25199662", "https://tenor.com/view/oh-yes-right-correct-david-tennant-doctor-who-gif-9222745", "https://tenor.com/view/10th-doctor-smile-gif-20188335", "https://tenor.com/view/doctor-who-dr-who-falling-david-tennant-ten-gif-15450241", "https://tenor.com/view/tenth-doctor-doctor-who-well-gif-13782620", "https://tenor.com/view/raining-sad-david-tennant-doctor-who-tenth-doctor-gif-17689514", "https://tenor.com/view/raining-sad-david-tennant-doctor-who-tenth-doctor-gif-17689514", "https://tenor.com/view/doctor-who-david-tennant-peek-tenth-doctor-gif-16294517", "https://tenor.com/view/dr-who-doctor-who-matt-smith-universally-recognized-mature-gif-4692534", "https://tenor.com/view/tv-comedy-sci-fi-bbc-doctor-who-gif-3486254", "https://tenor.com/view/doctor-who-david-tennant-10th-doctor-tenth-doctor-this-is-fine-gif-18263861", "https://tenor.com/view/love-and-monsters-doctor-who-dr-who-tumblr-david-tennant-gif-21669604", "https://tenor.com/view/davidt-tennant-doctor-who-10-cake-celebrate-gif-17272016", "https://tenor.com/view/doctor-who-david-tennant-im-very-good-doctor-who-david-tennant-david-tennant-doctor-who-gif-24732635", "https://tenor.com/view/doctor-who-whovian-david-tennant-gif-8677190", "https://tenor.com/view/dr-who-doctor-who-david-tennant-frown-sad-gif-4433017", "https://tenor.com/view/doctor-who-ridiculous-crazy-daft-david-tennant-gif-7533162", "https://tenor.com/view/doctor-who-11th-doctor-matt-smith-dance-party-gif-3301416", "https://tenor.com/view/doctor-peter-capaldi-doctor-who-i-am-doctor-idiot-who-gif-4662557", "https://tenor.com/view/thats-why-im-here-obi-wan-obi-wan-kenobi-star-wars-gif-18535648", "https://tenor.com/view/obi-wan-kenobi-jedi-master-star-wars-another-happy-landing-landing-gif-17180367", "https://tenor.com/view/so-uncivilised-gif-24177115", "https://tenor.com/view/doctor-who-whovian-tardis-david-tennant-gif-8051146"]
        length = len(gifs)-1
        num = randint(0, length)
        await ctx.send("https://i.makeagif.com/media/12-05-2014/0RqB_K.gif", view=self.BRTB())
    
    @commands.command()
    async def slap(self, ctx, victim:discord.Member):
        if victim.nick != None:
            name = victim.nick
        else:
            name = victim.name
        im = Image.open('Images/Gifs/head-slap-duh.gif')
        frames = []
        font = ImageFont.truetype("Images/Gifs/Fonts/ComicSansMS3.ttf", 25)
        for frame in ImageSequence.Iterator(im):
            d = ImageDraw.Draw(frame)
            d.text((300,80), name, font=font)
            del d

            b = io.BytesIO()
            frame.save(b, format="GIF")
            frame = Image.open(b)
            frames.append(frame)
        frames[0].save('Images/Gifs/Slap_Victim.gif', save_all=True, append_images=frames[1:])
        await ctx.send(file= discord.File('Images/Gifs/Slap_Victim.gif'))

                       
async def setup(client):
    await client.add_cog(PokeParadise_Server_Stuff(client))
