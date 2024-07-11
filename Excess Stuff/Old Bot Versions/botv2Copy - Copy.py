import os
import youtube_dl
import discord
import datetime
import asyncio
import time
import discord.voice_client
import urllib.request
import re
from random import randint
from discord.ext import commands
from discord.utils import find, get


youtube_dl.utils.bug_reports_message = lambda: ''
intents = discord.Intents.all()
global client
client = discord.Client(intents=intents)
intents.members = True
client = commands.Bot(command_prefix = ';', intents = intents)
client.remove_command('help')
#status = ['Dying on the inside']
status = ['With the void']
queu = []

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

def url_to_name():
    global queu
    global youtube
    global video_id
    global queu2

    for word in queu:
        num = 0
        qi = queu[num]
        youtube = re.findall(r'(https?://)?(www\.)?((youtube\.(com))/watch\?v=([-\w]+)|youtu\.be/([-\w]+))', qi)
        video_id = [c for c in youtube[0] if c]  # Get rid of empty list objects
        video_id = video_id[len(video_id) - 1]  # Return the last item in the list
        queu2 = video_id[num]
        num += 1


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


serve = 'O'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name='With The Void'))
    guild = client.get_guild(761652116375994448)
    user = guild.get_member(796467856677142530)
    n = user.display_name
    if n != "Giraffe's Test Subject":
        await user.edit(nick="Giraffe's Test Subject")
        print('Attempts are shown from here down:')

@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        entry = 'Hello {}!'.format(guild.name),'My prefix is ";"'
        await general.send('Hello {}!, My prefix is ";"'.format(guild.name))

@client.event
async def on_member_join(member):
    if serve == 'T':
        guild = client.get_guild(436904688521314307)
        channel = guild.get_channel(436904688521314309)
        print ('{} has joined {}.'.format(member, guild))
        await channel.send('Well Well Well, look who decided to show up\n{} has joined **{}**'.format(member.mention, guild))
    if serve == 'O':
        guild = client.get_guild(761652116375994448)
        channel = guild.get_channel(773661309777477672)
        print ('{} has joined {}.'.format(member, guild))
        await channel.send('Well Well Well, look who decided to show up\n{} has joined **{}**'.format(member.mention, guild))


@client.event
async def on_member_remove(member):
    if serve == 'T':
        guild = client.get_guild(436904688521314307)
        channel = guild.get_channel(436904688521314309)
        print('{} has left {}.'.format(member, guild))
        await channel.send('Oh no...{} has left....Anyways'.format(member.mention))
    if serve == 'O':
        guild = client.get_guild(761652116375994448)
        channel = guild.get_channel(773661309777477672)
        print ('{} has left {}.'.format(member, guild))
        await channel.send('Oh no...{} has left....Anyways'.format(member.mention))

@client.event
async def on_member_update(before, after):
    id = before.id
    if id == 796467856677142530:
        print('hah you wish')
        guild = client.get_guild(761652116375994448)
        user = guild.get_member(796467856677142530)
        n = user.display_name
        if n != "Giraffe's Test Subject":
            await user.edit(nick="Giraffe's Test Subject")




@client.event
async def on_message(message):
    user = message.author.mention
    if 'server for the first time' in message.content:
                    await message.channel.send('If you have op hold F3 then press F4 to toggle through the gamemodes for ease')
    if message.author.id != 204255221017214977 and 437808476106784770 and 159985870458322944 and 234395307759108106 and 414925323197612032 and 270904126974590976 and 266624760782258186:
        if message.author == client.user and message.channel.id != 791359435037212672:
            with open('./TextLogs/BotLog.txt', 'a') as file:
                file.write('{}\n'.format(message.author))
                file.close()
        #if message.author.bot: return
        #if message.channel.id == 791359435037212672: return
        if not message.author.bot and message.channel.id != 791359435037212672:
            with open('./TextLogs/ActivityLog.txt', 'a') as file:
                file.write('{}\n'.format(message.author))
                file.close()
    else:
        pass
    if message.channel.id == 802288407749328916:
        td = client.get_emoji('\N{Thumbs Down Sign}')
        tu = client.get_emoji('\N{Thumbs Up Sign}')
        await message.add_reaction('\N{Thumbs Up Sign}')
        await message.add_reaction('\N{Thumbs Down Sign}')

    if "asdfrg" in message.content:
            await message.channel.send('asdfrg')
            print('sent')

    if message.author != client.user:
        if "triggered" in message.content:
            await message.channel.send('''Hah {} you are:\nhttps://tenor.com/view/triggered-angry-mad-gif-12026482'''.format(user))

        elif ("best hits" in message.content):
            if message.author != client.user:
                if 'orin' in message.content:
                    await message.channel.send('''
                    Corin's best hits have to be:
"I don't go out with girls"
"**I AM NOT A CHAV**"
"They look like emo's"
"I have trouble speaking to women"
"I'm stuck in the *gay* zone"
"I take pride in being gay"
"I shall leave now because u are a bunch of weebs who like "Cute anime girls"

''')
                if 'oiyo' in message.content:
                    await message.channel.send('''Boiyo's best hits have to be:
"I need a *loooooooong* one"
""
""
''')
                if 'ecko' in message.content:
                    await message.channel.send('''Gecko's best hits have to be:
"Yes, I want your balls"
""
""
''')
                if 'box' in message.content:
                    await message.channel.send('''Xbox's best hits have to be:
"child murder is unquestionably slap stick comedy"
^in the context of orphans
""
""
''')
                if 'ugget' in message.content:
                    await message.channel.send('''Nugget's best hits have to be:
""
""
""
''')
                if 'oe' in message.content:
                    await message.channel.send('''Joe's best hits have to be:
"Gay"
"pweease wemove my diswike :pleading_face:"
^Joey and DT10
""
''')
                if 'ack' in message.content:
                    await message.channel.send('''Jack's best hits have to be:
"No I don't want to get arrested"
"I wanna be a racist, show me how!"
""
''')
                if ('NEA' in message.content) or ('nea' in message.content):
                    await message.channel.send('''NEA's best hits have to be:
"ahoy laddies"
""
""
''')
                if ('tar' in message.content) or ('azer' in message.content):
                    await message.channel.send('''Stargazer's best hits have to be:
"I'm going to curb stomp your head into a fucking smoothie"
""
""
''')
                if 'unar' in message.content:
                    await message.channel.send('''Lunar's best hits have to be:
"Boiyo is a sssss-oh hello Boiyo"
""
""
''')
    
        elif message.content.startswith('Skyra'):
            guild = client.get_guild(761652116375994448)
            bots = guild.get_channel(761676002366586881)
            bs = 761676002366586881
            ng = 803255421606952965
            if (bs != message.channel.id) and (ng != message.channel.id):
                await message.channel.send("That can't be used here, please go to {}".format(bots.mention))

        elif message.content.startswith('skyra'):
            guild = client.get_guild(761652116375994448)
            bots = guild.get_channel(761676002366586881)
            bs = 761676002366586881
            ng = 803255421606952965
            print(message.channel)
            if (bs != message.channel.id) and (ng != message.channel.id):
                await message.channel.send("That can't be used here, please go to {}".format(bots.mention))

        elif message.content.startswith('S!'):
            guild = client.get_guild(761652116375994448)
            bots = guild.get_channel(761676002366586881)
            bs = 761676002366586881
            ng = 803255421606952965
            if (bs != message.channel.id) and (ng != message.channel.id):
                await message.channel.send("That can't be used here, please go to {}".format(bots.mention))

        elif message.content.startswith('s!'):
            guild = client.get_guild(761652116375994448)
            bots = guild.get_channel(761676002366586881)
            bs = 761676002366586881
            ng = 803255421606952965
            if (bs != message.channel.id) and (ng != message.channel.id):
                await message.channel.send("That can't be used here, please go to {}".format(bots.mention))

        elif 'Clean <Num:Whole number>' in message.content:
            await message.delete()

        await client.process_commands(message)


@client.command(brief = 'Run this command to find out how the bot is feeling')
async def feeling(cxt):
    choice = (randint(1,3))
    if choice == 1:
        await cxt.send('I wanna jump off of a cliff')
    elif choice == 2:
        await cxt.send("I'm feeling good, thank you for asking")
    elif choice == 3:
        await cxt.send('Better than you boiii')


@client.command(brief = 'Deletes messages in current channel between 1 and 100\nOnly available to those with the Administrator permission')
async def purge(ctx, amount):
    amount = int(amount)
    amount += 1
    if ctx.author.guild_permissions.administrator:
        await ctx.channel.purge(limit = amount)
    else:
        msg = "You're an average joe {0.author.mention}, you can't use that".format(ctx.message)
        await ctx.send(msg)

@client.command()
async def kick(ctx, member:discord.Member, *, reason=None):
    if ctx.author.guild_permissions.administrator:
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

@client.command()
async def ban(ctx, member:discord.Member, *, reason=None):
    if ctx.author.guild_permissions.administrator:
        await member.ban(reason=reason)

    else:
        msg = "You're an average joe {0.author.mention}, you can't use that".format(ctx.message)
        await ctx.send(msg)

@client.command()
async def mute(ctx, member: discord.Member):
     if ctx.author.guild_permissions.administrator:
        role = discord.utils.get(member.guild.roles, name='Muted')
        await member.add_roles(role)
        await ctx.send('{} has been muted\n**Silence shall now fall**...for a while at least'.format(member.mention))
     else:
        msg = "You're an average joe {0.author.mention}, you can't use that".format(ctx.message)
        await ctx.send(msg)

@client.command()
async def unmute(ctx, member: discord.Member):
     if ctx.author.guild_permissions.administrator:
        role = discord.utils.get(member.guild.roles, name='Muted')
        await member.remove_roles(role)
        await ctx.send('{} has been unmuted\nYou can do the speak now I guess'.format(member.mention))
     else:
        msg = "You're an average joe {0.author.mention}, you can't use that".format(ctx.message)
        await ctx.send(msg)

@client.command()
async def help(cxt):
    await cxt.send('''
Here is the current list of commands:
(I would suggest sticking to the bot channel of your respective server, but what do I know I'm just a bot)

__**Basic Commands:**__
;suggest [your suggestion] - Helps me with development of the bot and make your ideas known for future additions
;MOTWLB - View the current leader board for the activity based component of the MOTW selection
(Spammed messages, and tts will not be counted. However in the case of tts time in vc will still be counted by moderators)


;feeling - Run this command to find how the bot is feeling
;gif - (in dev and currently disabled) Supplies random gif
;quote - (in dev) Responds with a random quote


__**Administrator Commands:**__
__(Must have the Administrator permission to run):__
;purge [number] - Deletes messages in current channel between 1 and 100\nOnly available to those with the Administrator permission
;kick [member]
;ban [member]
;mute [member]
;unmute [member]
    ''')
@client.command()
async def suggest(ctx, sug):
    t = datetime.datetime.now()
    t = t.strftime('%c')
    print('{}: {} : {}'.format(t, ctx.author, sug))
    with open('./TextLogs/Suggestions.txt', "a") as file:
        file.write('{}: {} : {}\n'.format(t, ctx.author, sug))
        file.close()
    await ctx.send('Thank you for your suggestion, I really appreciate the help with this project of mine')
    time.sleep(1.75)
    await ctx.channel.purge(limit = 2)

@client.command()
async def MOTWLB(ctx):
    f = open('./TextLogs/ActivityLog.txt', 'r')
    d = dict()
    lb = []
    for line in f:
        line = line.strip()
        if line in d:
            d[line] = d[line] + 1
        else:
            d[line] = 1
    sorted_dict = {}
    sorted_keys = sorted(d, key=d.get)

    for w in sorted_keys:
        sorted_dict[w] = d[w]
    await ctx.send('''Member Of the Week Activity Leaderboard:
**Member   :   Messages this week**''')
    limit = len(sorted_keys)
    for key in reversed(sorted_dict.keys()):
        lb.append('{}  :  {}'.format(key, d[key]))
    lb = ('\n'.join(lb))
    await ctx.send(lb)

@client.command()
async def botlog(ctx):
    f = open('./TextLogs/BotLog.txt', 'r')
    d = dict()
    for line in f:
        line = line.strip()
        if line in d:
            d[line] = d[line] + 1
        else:
            d[line] = 1
    for key in list(d.keys()):
        await ctx.send('{}  :  {}'.format(key, d[key]))

@client.command()
async def join(ctx):
    voiceChannel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if not ctx.message.author.voice:
        await('You are not connected to a voice channel')
        return
    if not voice and voiceChannel:
        await voiceChannel.connect()
    if voice and voiceChannel != voice.channel:
        await voice.disconnect()
        await voiceChannel.connect()

@client.command()
async def queue(ctx, url):
    global queu

    queu.append(url)
    await ctx.send(f'`{url}` added to queue!')

@client.command()
async def search(ctx, *args):
    global gueu
    search_keywords = ""
    for word in args:
        search_keywords += word
        search_keywords += '+'
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keywords)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    url = ("https://www.youtube.com/watch?v=" + video_ids[0])
    queu.append(url)
    await ctx.send(f'`{url}` added to queue!')

@client.command()
async def play(ctx, *args):
    # voiceChannel = ctx.message.author.voice.channel
    # voice = get(client.voice_clients, guild=ctx.guild)
    # if not ctx.message.author.voice:
    #     await('You are not connected to a voice channel')
    #     return
    # if not voice and voiceChannel:
    #     await voiceChannel.connect()
    # if voice and voiceChannel != voice.channel:
    #     await voice.disconnect()
    #     await voiceChannel.connect()
    global queu

    server = ctx.message.guild
    voice_channel = server.voice_client
    if queu:
        async with ctx.typing():
            player = await YTDLSource.from_url(queu[0], loop=client.loop)
            voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send('**Now playing:** {}'.format(player.title))
        del(queu[0])
    elif not queu:
        await ctx.send("You can't play if there isn't anything in the queue")
    # finished = 'a'
    # while finished == 'a':
    #     voice = get(client.voice_clients, guild=ctx.guild)
    #     if not voice.is_playing():
    #         if queu:
    #             try:
    #                 p = client.get_command('play')
    #                 await ctx.invoke(p)
    #                 finished = 'b'
    #             except Exception:
    #                 print('')
    #         else:
    #             return

@client.command()
async def view(ctx):
    global youtube
    global video_id
    global queu2
    url_to_name()
    # global queu
    #
    # for word in queu:
    #     youtube = re.findall(r'(https?://)?(www\.)?((youtube\.(com))/watch\?v=([-\w]+)|youtu\.be/([-\w]+))', queue[word])
    #     video_id = [c for c in youtube[0] if c]  # Get rid of empty list objects
    #     video_id = video_id[len(video_id) - 1]  # Return the last item in the list
    #     queu2 = video_id[word]

    if youtube:
        print(video_id)
        print(queu2)
    await ctx.send(f'Your queue is now `{queu2}!`')
    youtube = None
    video_id = []
    queu2 = []


@client.command()
async def empty(ctx):
    global queu
    if queu:
        queu = []
    elif not queu:
        await ctx.message.send('The queue is already empty')

@client.command()
async def remove(ctx, num):
    global queu
    num = int(num)
    if queu:
        del queu[num]
        await ctx.send('Item {} removed from the queue'.format(num))
    elif not queu:
        await ctx.send('You cant do that, the queue is already empty')


@client.command()
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    await ctx.send('Music stopped')

@client.command()
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
        await ctx.send('Music paused, run ``;resume`` to continue')
    else:
        await ctx.send('Nothing is being played at the moment')

@client.command()
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused:
        voice.resume()
        await ctx.send('Music resumed')
    else:
        await ctx.send('Nothing is paused at this time')

@client.command()
async def dc(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("I'm not in a voice channel.")
    voice = get(client.voice_clients, guild=ctx.guild)
    p = client.get_command('spurge')
    await ctx.invoke(p)

@client.command()
async def reviews(ctx):
    await ctx.send('The link to the website of our resident film reviewer Glider is:\nhttps://lukeplusfilms.wixsite.com/my-site')

@client.command()
async def spammer(ctx):
    if ctx.author.guild_permissions.administrator:
        for f in range(0,550):
            time.sleep(0.5)
            await ctx.send('testing')
            print(f)







@client.command()
async def LastResort(ctx):
    if ctx.author.guild_permissions.administrator:
        giraffe = ctx.guild.get_member(230442733234421760)
        await ctx.send(f"I'm Being shot by the firing squad again.... {giraffe.mention}")
        await ctx.send(giraffe.mention)
        await ctx.send(giraffe.mention)
        import sys
        sys.exit()


@client.command()
async def spurge(ctx):
    for file in os.listdir("./"):
        if file.endswith('.m4a'):
            os.rename(file, 'song.mp3')
            song_there = os.path.isfile('song.mp3')
            try:
                if song_there:
                    os.remove('song.mp3')
            except PermissionError:
                print('')
        if file.endswith('.webm'):
            os.rename(file, 'song.mp3')
            song_there = os.path.isfile('song.mp3')
            try:
                if song_there:
                    os.remove('song.mp3')
            except PermissionError:
                print('')

                
client.run(os.getenv("ABYSS_BOT_TOKEN"))
