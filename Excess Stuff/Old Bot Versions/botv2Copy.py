import os
import youtube_dl
import discord
import datetime
import asyncio
import time
import discord.voice_client
from pytube import YouTube
from random import randint
from discord.ext import commands
from discord.utils import find, get


youtube_dl.utils.bug_reports_message = lambda: ''
intents = discord.Intents.all()
global client
#client = discord.Client(intents=intents)
intents.members = True
client = commands.Bot(command_prefix = ';', intents = intents)
client.remove_command('help')
#status = ['Dying on the inside']
status = ['With the void']
queu = []
global autom
autom = False

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
        yt = YouTube(queu[num])
        name = yt.title
        queu2.append(name)
        num += 1
        # num = 0
        # qi = queu[num]
        # youtube = re.findall(r'(https?://)?(www\.)?((youtube\.(com))/watch\?v=([-\w]+)|youtu\.be/([-\w]+))', qi)
        # video_id = [c for c in youtube[0] if c]  # Get rid of empty list objects
        # video_id = video_id[len(video_id) - 1]  # Return the last item in the list
        # queu2 = video_id[num]
        # num += 1


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
    guild = client.get_guild(761652116375994448)
    channel = guild.get_channel(773661309777477672)
    print ('{} has joined {}.'.format(member, guild))
    await channel.send('Well Well Well, look who decided to show up\n{} has joined **{}**'.format(member.mention, guild))


@client.event
async def on_member_remove(member):
    guild = client.get_guild(761652116375994448)
    channel = guild.get_channel(773661309777477672)
    print ('{} has left {}.'.format(member, guild))
    await channel.send('Oh no...{} has left....Anyways'.format(member.mention))

@client.event
async def on_member_update(before, after):
    if before.id == 796467856677142530:
        print('hah you wish')
        guild = client.get_guild(761652116375994448)
        user = guild.get_member(796467856677142530)
        n = user.display_name
        if n != "Giraffe's Test Subject":
            await user.edit(nick="Giraffe's Test Subject")


@client.event
async def on_message(message):
    user = message.author.mention
    if message.author.id != 204255221017214977 and 437808476106784770 and 159985870458322944 and 234395307759108106 and 414925323197612032 and 270904126974590976 and 266624760782258186:
        if message.author == client.user and message.channel.id not in [791359435037212672, 804050410218061895, 804051517237755955, 806531215762653204]:
            with open('./TextLogs/BotLog.txt', 'a') as file:
                file.write('{}\n'.format(message.author))
                file.close()
        #if message.author.bot: return
        #if message.channel.id == 791359435037212672: return
        if not message.author.bot and message.channel.id not in [791359435037212672, 761676002366586881, 806531215762653204]:
        #spam exception : , 763072814651277406]:
            if message.author.id != 377862119112179712:
                with open('./TextLogs/ActivityLog.txt', 'a') as file:
                    file.write('{}\n'.format(message.author))
                    file.close()
            if message.author.id == 377862119112179712:
                with open('./TextLogs/ActivityLog.txt', 'a') as file:
                    file.write('Wobbles\n')
                    file.close()
    else:
        pass
    if message.channel.id == 802288407749328916:
        await message.add_reaction('\N{Thumbs Up Sign}')
        await message.add_reaction('\N{Thumbs Down Sign}')

    if "asdfrg" in message.content:
        if message.author.guild_permissions.administrator:
            await message.channel.send('asdfrg')

   # if "testing" in message.content:
   #     print("hope?")

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
"I shall leave now because u are a bunch of weebs who like 'Cute anime girls'"
"Poggers"
"I don't want to listen to creepy music. I might piss my self"
"why do i have so many best hits?"
"If I live twice as long ill be an omega boomer"
"Whos Freddie Mercury"
"Who tf are the goonies.......Are they like the avengers"
"I'm a simp" x2

''')
                if 'oiyo' in message.content:
                    await message.channel.send('''Boiyo's best hits have to be:
"I need a *loooooooong* one"
"you were an alpha male"
"Want to be server owner?"
^ DM sent to *Corin* of all people...
"hey gecko, would you like to own my server?"
"that's not incriminating, that's funny"
"where you live is a shithole" - OlBoiyo [12/11/2020]
". justin ugh fine i guess you are my little pogchamp" - OlBoiyo [25/11/2020]
"DON'T LEAK THIS TO THE PUBLIC" - OlBoiyo [28/11/2020]
"I am the Lorax, I speak for the trees! Save the Amazon or I'll break your knees!" - OlBoiyo [02/12/2020]
"Do you think Amy rose from sonic is “hot@" - OlBoiyo [05/12/2020]
"I murdered the little girl"
"please don't call me soggy dog"
"A bunch of people stitched together against their will to create an abomination do be kinda hot tbh"

''')
                if 'ecko' in message.content:
                    await message.channel.send('''Gecko's best hits have to be:
"Yes, I want your balls"
"ohhhhh that's so cool"
^^ In response to "i stabbed myself earlier" - Lunar
"!ban @Gecko On LapTop"
"imagine being gay"
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
"beetlejuice is hot"
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
"I'm crucifying Brian"
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
"i stabbed myself earlier" 
^ Followed by:
"ohhhhh that's so cool" - Gecko
""
''')
                if 'iraffe' in message.content:
                    await message.channel.send('''giraffe's best hits have to be:
"I ain't dancing like no nonce"
''')
    
        elif message.content.startswith('Skyra'):
            guild = client.get_guild(761652116375994448)
            bots = guild.get_channel(761676002366586881)
            bs = 761676002366586881
            ng = 803255421606952965
            if message.channel.id not in [806531215762653204, 761676002366586881, 803255421606952965]:
                await message.channel.send("That can't be used here, please go to {}".format(bots.mention))

        elif message.content.startswith('skyra'):
            guild = client.get_guild(761652116375994448)
            bots = guild.get_channel(761676002366586881)
            bs = 761676002366586881
            ng = 803255421606952965
            print(message.channel)
            if message.channel.id not in [806531215762653204, 761676002366586881, 803255421606952965]:
                await message.channel.send("That can't be used here, please go to {}".format(bots.mention))

        elif message.content.startswith('S!'):
            guild = client.get_guild(761652116375994448)
            bots = guild.get_channel(761676002366586881)
            bs = 761676002366586881
            ng = 803255421606952965
            if message.channel.id not in [806531215762653204, 761676002366586881, 803255421606952965]:
                await message.channel.send("That can't be used here, please go to {}".format(bots.mention))

        elif message.content.startswith('s!'):
            guild = client.get_guild(761652116375994448)
            bots = guild.get_channel(761676002366586881)
            bs = 761676002366586881
            ng = 803255421606952965
            if message.channel.id not in [806531215762653204, 761676002366586881, 803255421606952965]:
                await message.channel.send("That can't be used here, please go to {}".format(bots.mention))

        elif 'Clean <Num:Whole number>' in message.content:
            await message.delete()

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
        if 'ahoy' in message.content:
            al = client.get_emoji(821148094670438480)
            await message.add_reaction(al)
        if 'Ahoy' in message.content:
            al = client.get_emoji(821148094670438480)
            await message.add_reaction(al)

                
        await client.process_commands(message)

@client.event
async def on_raw_reaction_add(RawReactionActionEvent):
    guild = client.get_guild(761652116375994448)
    role_id = 815956184401444904
    role = guild.get_role(role_id)
    if RawReactionActionEvent.message_id == 815921755800731658:
        member = RawReactionActionEvent.member
        await member.add_roles(role)



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
async def help(ctx, *branch):
    if not branch:
        #print('empty')
        embed = discord.Embed(title = 'Help:', description = 'Here are the current categories for help commands\nPlease run the command again with the category typed afterwards:')
        embed.add_field(name = 'Fun:', value = 'These are the more fun commands')
        embed.add_field(name='Music:', value='These are the music commands')
        embed.add_field(name='Admin:', value='These are the admin specific commands')
        await ctx.send(embed = embed)
    if branch and 'fun' in branch:
        #print('fun')
        embed = discord.Embed(title='Fun Commands:', description='Here are all the current commands that aim to be fun:')
        embed.add_field(name=';feeling', value='Run this command to find how the bot is feeling')
        embed.add_field(name=';gif', value='(in dev and currently disabled) Supplies random gif')
        embed.add_field(name=';quote', value='(in dev) Responds with a random quote')
        await ctx.send(embed=embed)
    elif branch and 'music' in branch:
        #print('music')
        embed = discord.Embed(title='Music Commands:', description='Here are all the commands relating to the music function of the bot:\nPlease be aware in advance there is no auto play atm:')
        embed.add_field(name=';join', value="Always run this command first if bot isn't connected:\nRun this command to make the bot join the channel")
        embed.add_field(name=';play', value='This is your generic play command, either adds the url to the queue, searches for a song, or plays the next item in the queue if no song is playing')
        embed.add_field(name=';auto <on/off>', value='(Broken at the moment, please do not run as it breaks the bot) This command will turn on auto play for the duration of the queue')
        embed.add_field(name=';next', value='This command will either skip to the next song, or just play the next song if nothing is playing')
        embed.add_field(name=';stop', value='This command will stop the current track from playing')
        embed.add_field(name=';pause', value='This command will pause the current track')
        embed.add_field(name=';resume', value='This command will continue playing the paused track')
        embed.add_field(name=';remove <num>', value='This command will remove the specified track from the queue')
        embed.add_field(name=';queue', value="This command will show the current queue")
        embed.add_field(name=';empty', value='This command will clear the queue')
        embed.add_field(name=';dc', value='This command will make the bot leave the channel')
        await ctx.send(embed=embed)
    if branch and 'admin' in branch:
        #print('admin')
        embed = discord.Embed(title='Admin Commands:', description='Here are all the current admin-related commands\nYou must have the "administrator" perm to run these:')
        embed.add_field(name=';purge <num>', value='Your standard message clearing command')
        embed.add_field(name=';ban <@user> <Reason>', value='Bans the mentioned member and supplies a reason if included (It can be run without a reason given)')
        embed.add_field(name=';kick <@user> <Reason>', value='Kicks the mentioned member and supplies a reason if included (It can be run without a reason given)')
        embed.add_field(name=';mute <@user>', value='Mutes the mentioned user until the ;unmute command is ran or the role is removed manually')
        embed.add_field(name=';unmute <@user>', value='Removes the muted role from the mentioned member')
        await ctx.send(embed=embed)



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

@client.command(pass_context = True , aliases=['motwlb'])
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
async def play(ctx, *args):
    global queu
    #global autom
    #queu = ['https://www.youtube.com/watch?v=2X_2IdybTV0F']
    if not args:
        voice = get(client.voice_clients, guild=ctx.guild)
        if not voice.is_playing():
            server = ctx.message.guild
            voice_channel = server.voice_client
            if queu:
                async with ctx.typing():
                    player = await YTDLSource.from_url(queu[0], loop=client.loop)
                    voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

                await ctx.send('**Now playing:** {}'.format(player.title))
                del(queu[0])
                # while autom == True:
                #     try:
                #         a = client.get_command('auto')
                #         await ctx.invoke(a)
                #     except:
                #         print('')
            elif not queu:
                await ctx.send("You can't play if there isn't anything in the queue\nIf auto mode was on it has now been disabled, to use it gain please add to the queue and run ``;auto on``")
                autom = False
    if args:
        global gueu
        search_keywords = ""
        print(args)
        for word in args:
            search_keywords += word
            search_keywords += '+'
        #link = "https://www.youtube.com/results?search_query=test"
        #link += search_keywords
        #search = link
        ##with ytdl as ydl:
        infosearched = ytdl.extract_info(f"ytsearch:{search_keywords}", download=False)
        #print(infosearched)
        url = infosearched['entries'][0]['webpage_url']
        queu.append(url)
        ##print(link)
        #html = urllib.request.urlopen(link)
        #video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        #url = ("https://www.youtube.com/watch?v=" + video_ids[0])
        ##print(url)
        #queu.append(url)
        ##print(queu)

        await ctx.send("``{}`` added to queue!\n If the song doesn't start please either let the current song end and run ``;play``/``;next`` again or run ``;next`` to play now".format(url))
        try:
            p = client.get_command('play')
            await ctx.invoke(p)
        except:
            print('failed')


@client.command()
async def next(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    await ctx.send('Loading next track:')
    p = client.get_command('play')
    await ctx.invoke(p)


@client.command()
async def queue(ctx):
    global youtube
    global video_id
    global queu
    global queu2
    queu2 = []
    for f in queu:
        num = 0
        yt = YouTube(f)
        name = yt.title
        queu2.append(name)
        num += 1
    await ctx.send(f'Your queue is now ``{queu2}!``')
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
    num = num - 1
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

@client.command(context_pass = True, aliases = ['ahoy ladies', 'ahoyladies'])
async def ahoy(ctx, *, loop=None, stream=False):
    global queu
    # try:

    try:
        voiceChannel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)
        if not ctx.message.author.voice:
            pass
        if not voice and voiceChannel:
            await voiceChannel.connect()
        if voice and voiceChannel != voice.channel:
            await voice.disconnect()
            await voiceChannel.connect()
        if 'https://www.youtube.com/watch?v=ane8xXNWwns' not in queu:
            queu.append('https://www.youtube.com/watch?v=ane8xXNWwns')
            print(queu)
        if 'https://www.youtube.com/watch?v=ane8xXNWwns' in queu[0]:
            pl = client.get_command('play')
            try:
                await ctx.invoke(pl)
            except:
                print('ahoy failed play')
    except:
        print('Ahoy not, in voicechannel {}'.format(ctx.author))
    await ctx.channel.send('https://tenor.com/view/steve-joe-kerry-scoop-ahoy-ahoy-stranger-things-gif-17227867')
    # except:
    #     print('Ahoy: User not in voice, failed at first step most likely (see other outputs)')

@client.command(pass_context = True , aliases=['hellothere', 'hello there', 'Hellothere', 'Hello there'])
async def ht(ctx):
    global queu
    # try:

    try:
        voiceChannel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)
        if not ctx.message.author.voice:
            pass
        if not voice and voiceChannel:
            await voiceChannel.connect()
        if voice and voiceChannel != voice.channel:
            await voice.disconnect()
            await voiceChannel.connect()
        if 'https://www.youtube.com/watch?v=eaEMSKzqGAg' not in queu:
            queu.append('https://www.youtube.com/watch?v=eaEMSKzqGAg')
            print(queu)
        if 'https://www.youtube.com/watch?v=eaEMSKzqGAg' in queu[0]:
            pl = client.get_command('play')
            try:
                await ctx.invoke(pl)
            except:
                print('hello there failed play')
    except:
        print('hello there not, in voicechannel {}'.format(ctx.author))

@client.command(pass_context = True , aliases=['diggy', 'Dwarf', 'diggydiggy', 'Diggy', 'Diggydiggy', 'Diggydiggyhole', 'diggydiggyhole'])
async def dwarf(ctx):
    global queu
    # try:

    try:
        voiceChannel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)
        if not ctx.message.author.voice:
            pass
        if not voice and voiceChannel:
            await voiceChannel.connect()
        if voice and voiceChannel != voice.channel:
            await voice.disconnect()
            await voiceChannel.connect()
        if 'https://www.youtube.com/watch?v=ytWz0qVvBZ0' not in queu:
            queu.append('https://www.youtube.com/watch?v=ytWz0qVvBZ0')
            print(queu)
        if 'https://www.youtube.com/watch?v=ytWz0qVvBZ0' in queu[0]:
            pl = client.get_command('play')
            try:
                await ctx.invoke(pl)
            except:
                print('diggy diggy failed play')
    except:
        print('diggy diggy not, in voicechannel {}'.format(ctx.author))

@client.command(pass_context = True , aliases=['Giggity', 'giggitygiggity', 'Giggitygiggity'])
async def giggity(ctx):
    global queu
    # try:

    try:
        voiceChannel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)
        if not ctx.message.author.voice:
            pass
        if not voice and voiceChannel:
            await voiceChannel.connect()
        if voice and voiceChannel != voice.channel:
            await voice.disconnect()
            await voiceChannel.connect()
        if 'https://www.youtube.com/watch?v=YWFW0B9EBx0' not in queu:
            queu.append('https://www.youtube.com/watch?v=YWFW0B9EBx0')
            print(queu)
        if 'https://www.youtube.com/watch?v=YWFW0B9EBx0' in queu[0]:
            pl = client.get_command('play')
            try:
                await ctx.invoke(pl)
            except:
                print('giggity failed play')
    except:
        print('giggity not, in voicechannel {}'.format(ctx.author))

@client.command()
async def gae(ctx):
    global queu
    try:
        voiceChannel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)
        if not ctx.message.author.voice:
            pass
        if not voice and voiceChannel:
            await voiceChannel.connect()
        if voice and voiceChannel != voice.channel:
            await voice.disconnect()
            await voiceChannel.connect()
        if 'https://www.youtube.com/watch?v=iqMV1Mdm8ZA' not in queu:
            queu.append('https://www.youtube.com/watch?v=iqMV1Mdm8ZA')
            print(queu)
        if 'https://www.youtube.com/watch?v=iqMV1Mdm8ZA' in queu[0]:
            pl = client.get_command('play')
            try:
                await ctx.invoke(pl)
            except:
                print('gae failed play')
    except:
        print('gae not, in voicechannel {}'.format(ctx.author))

@client.command()
async def gay(ctx):
    global queu
    try:
        voiceChannel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)
        if not ctx.message.author.voice:
            pass
        if not voice and voiceChannel:
            await voiceChannel.connect()
        if voice and voiceChannel != voice.channel:
            await voice.disconnect()
            await voiceChannel.connect()
        if 'https://www.youtube.com/watch?v=NAj26rVWK14' not in queu:
            queu.append('https://www.youtube.com/watch?v=NAj26rVWK14')
            print(queu)
        if 'https://www.youtube.com/watch?v=NAj26rVWK14' in queu[0]:
            pl = client.get_command('play')
            try:
                await ctx.invoke(pl)
            except:
                print('gay failed play')
    except:
        print('gay not, in voicechannel {}'.format(ctx.author))

# @client.command()
# async def auto(ctx, *yn):
#     global autom
#     global queu
#     if 'on' in yn:
#         autom = True
#         #print(f'yn true {autom}')
#     if 'off' in yn:
#         autom = False
#         #print(f'yn false {autom}')
#     #print(f'before while {autom}')
#     if queu:
#         while autom == True:
#             try:
#                 #print(f'in try {autom}')
#                 p = client.get_command('play')
#                 await ctx.invoke(p)
#             except:
#                 #print(f'in except {autom}')
#                 await asyncio.sleep(5)
#                 #print(f'after sleep {autom}')
#                 a = client.get_command('auto')
#                 await ctx.invoke(a)
#
#
#     #print(f'before while {autom}')
#     if autom is True:
#         while autom is True:
#             try:
#                 #print(f'in try {autom}')
#                 p = client.get_command('play')
#                 await asyncio.sleep(5)
#                 await ctx.invoke(p)
#             except:
#                 #print(f'in except {autom}')
#                 await asyncio.sleep(5)
#                 #print(f'after sleep {autom}')
#                 a = client.get_command('auto')
#                 await ctx.invoke(a)
#
#         if not yn:
#             await ctx.send('You have not specified on or off, please repeat the command with this included')
#             #print(f'before the trys {autom}')


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
            await ctx.send('Nothing to see here')
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

@client.command()
async def lbpurge(ctx):
    if ctx.author.guild_permissions.administrator:
        guild = client.get_guild(761652116375994448)
        user = guild.get_member(747838795704959027)
        with open('./TextLogs/BotLog.txt', 'w') as file:
            file.write('Not Suspicious#7966\n')
            file.close()
        with open('./TextLogs/ActivityLog.txt', 'w') as file:
            file.write('{}\n'.format(ctx.author))
            file.close()
        await ctx.send('Both motwlb and the bot log has been cleared')

@client.command()
async def praise(ctx):
    if ctx.author.guild_permissions.administrator:
        guild = client.get_guild(761652116375994448)
        user = guild.get_member(747838795704959027)
        for f in range(0,550):
            await asyncio.sleep(1)
            await ctx.send('Praise {}....Praise him!!'.format(user.mention))
            await asyncio.sleep(1)
            await ctx.send('Praise {}....Praise him!!'.format(user.mention))

@client.command(pass_context = True , aliases=['-;'])
async def emojiresponse(ctx):
    if ctx.author != client.user:
        await ctx.send(';-;')

@client.command(pass_context = True , aliases=[')'])
async def emojiresponse2(ctx):
    if ctx.author != client.user:
        await ctx.send(';)')

@client.command()
async def test(ctx, *args):
    search = ''
    for word in args:
        search += word
        search += ' '

@client.command(pass_context = True , aliases=['Abusereport', 'modreport', 'Modreport'])
async def abusereport(ctx, *args):
    guild = client.get_guild(761652116375994448)
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
    await ctx.channel.purge(limit = 2)

@client.command()
async def reports(ctx):
    with open('./TextLogs/AbuseReports.txt', "r") as file:
        f = ''
        for line in file:
            f += line
        await ctx.send(f)
        file.close()

@client.command()
async def teamviewerReset(ctx):
    await ctx.send('Please wait while teamviewer is closed')
    os.system("taskkill/IM TeamViewer.exe /F")
    await asyncio.sleep(6)
    os.startfile(r"C:\Users\Public\\temp\TeamViewer\TeamViewer.exe")
    await asyncio.sleep(2)
    await ctx.send('Team Viewer should be starting up now give it a moment')

class playerData:
    user = ''
    health = 100
    max_attack = 5
    defense = 0
#global p1
#global p1_Member
#global p2
#global p2_Member
global gameStarted
gameStarted = False
#p1 = playerData()
#p2 = playerData()

def hpcheck():
    global p1
    global p1_Member
    global p2
    global p2_Member
    global gameStarted
    global winner
    if p1.health <0:
        winner = p2_Member
        gameStarted = False

    if p2.health <0:
        winner = p1_Member
        gameStarted = False


@client.command(pass_context = True, aliases = ['fight'])
async def startfight(ctx, member:discord.Member):
    global p1
    global p1_Member
    global p2
    global p2_Member
    global gameStarted
    global currentPlayer
    global gameTurn
    global winner
    winner = None
    if not gameStarted:
        p1 = playerData()
        p2 = playerData()
        p1.user = ctx.author.id
        p1_Member = ctx.author
        p2.user = member.id
        p2_Member = member
        if p1_Member.id != p2_Member.id:
            print('\nFight Started:')
            print(p1_Member)
            print(p2_Member)
            await ctx.send('''Fight Started:
            {} vs {}'''.format(p1_Member.mention, p2_Member.mention))
            gameStarted = True
            gameTurn = p2_Member.id
            await ctx.send('{} it is your turn:\nPlease run ``;move`` along with attack, fortify, or train'.format(p2_Member.mention))
        if p1_Member.id == p2_Member.id:
            await ctx.send("You don't need my help to fight yourself")
    else:
        await ctx.send('A fight has already been started, please wait until it is completed and try again')

@client.command()
async def move(ctx, choice):
    global p1
    global p1_Member
    global p2
    global p2_Member
    global gameStarted
    global currentPlayer
    global gameTurn
    global winner
    print('\n{}\nhp:{}\nattack:{}\ndefense:{}'.format(p1_Member, p1.health, p1.max_attack, p1.defense))
    print('\n{}\nhp:{}\nattack:{}\ndefense:{}'.format(p2_Member, p2.health, p2.max_attack, p2.defense))
    currentPlayer = ctx
    if gameTurn != ctx.author.id and gameStarted is True:
        await ctx.send('Please wait for your turn')
    if gameTurn == ctx.author.id and gameStarted:
        if choice == 'train':
            increase = randint(1, 5)
            if currentPlayer.author.id == p1_Member.id:
                gameTurn = p2_Member.id
                p1.max_attack = p1.max_attack + increase
                await ctx.send('''{} You trained your skills for a bit and gained {} attack\nYou now have a maximum attack of {}
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(currentPlayer.author.mention, increase, p1.max_attack, p2_Member.mention))
            if currentPlayer.author.id == p2_Member.id:
                gameTurn = p1_Member.id
                p2.max_attack = p2.max_attack + increase
                await ctx.send('''{} You trained your skills for a bit and gained {} attack\nYou now have a maximum attack of {}
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(currentPlayer.author.mention, increase, p2.max_attack, p1_Member.mention))

        if choice == 'fortify':
            increase = randint(1, 5)
            if currentPlayer.author.id == p1_Member.id:
                gameTurn = p2_Member.id
                p1.defense = p1.defense + increase
                await ctx.send('''{} You have flexed really hard and gained {} defense\nYou now have a defense of {}
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(currentPlayer.author.mention, increase, p1.defense, p2_Member.mention))
            if currentPlayer.author.id == p2_Member.id:
                gameTurn = p1_Member.id
                p2.defense = p2.defense + increase
                await ctx.send('''{} You have flexed really hard and gained {} defense\nYou now have a defense of {}
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(currentPlayer.author.mention, increase, p2.defense, p1_Member.mention))


        if choice == 'attack':
            if ctx.author.id == p1_Member.id:
                gameTurn = p2_Member.id
                damage = randint(0, p1.max_attack)
                truedamage = damage - p2.defense
                if truedamage >0 and damage != p1.max_attack:
                    p2.health = p2.health - truedamage
                if damage == p2.max_attack:
                    p2.health = p2.health - damage
                if p2.defense > 0 and damage != p1.max_attack:
                    if truedamage > 0:
                        await ctx.send('''You attempted to land a hit of {}, but after {} defended you only dealt {} leaving them with {} health
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(damage, p2_Member.mention, truedamage, p2.health, p2_Member.mention))
                    if truedamage <= 0:
                        await ctx.send('''You tried to attack but were blocked with ease by {}
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(p2_Member.mention, p2_Member.mention))
                if p2.defense == 0 and truedamage >0:
                    await ctx.send('''You dealt a perfect hit of {} as {} has no defense leaving them with {} health
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(damage, p2_Member.mention, p2.health, p2_Member.mention))
                if damage == p1.max_attack:
                    await ctx.send('''You dealt a critical blow of {} dealing full damage and bypassing {}'s defences leaving them with {} health
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(damage, p2_Member.mention, p2.health, p2_Member.mention))

                hpcheck()

            if ctx.author.id == p2_Member.id:
                gameTurn = p1_Member.id
                damage = randint(0, p2.max_attack)
                truedamage = damage - p1.defense
                if p1.defense > 0 and damage != p2.max_attack:
                    if truedamage > 0:
                        await ctx.send('''You attempted to land a hit of {}, but after {} defended you only dealt {} leaving them with {} health
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(damage, p1_Member.mention, truedamage, p1.health, p1_Member.mention))
                    if truedamage <= 0:
                        await ctx.send('''You tried to attack but were blocked with ease by {}
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(p1_Member.mention, p1_Member.mention))
                if p2.defense == 0 and truedamage > 0:
                    await ctx.send('''You dealt a perfect hit of {} as {} has no defense leaving them with {} health
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(damage, p1_Member.mention, p1.health, p1_Member.mention))
                if damage == p2.max_attack:
                    await ctx.send('''You dealt a critical blow of {} dealing full damage and bypassing {}'s defences leaving them with {} health
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(damage, p1_Member.mention, p1.health, p1_Member.mention))
                hpcheck()
                

    if not gameStarted:
        if winner is None:
            await ctx.send('You must start a fight with ``;startfight <mention>`` before running this command')
        if winner.id == p1.user:
            await ctx.send('{} has won the fight with {} health remaining, better luck next time {}'.format(p1_Member.mention, p1.health, p2_Member.mention))
        if winner.id == p2.user:
            await ctx.send('{} has won the fight with {} health remaining, better luck next time {}'.format(p2_Member.mention, p2.health,p1_Member.mention))

# @client.command()
# async def fortify(ctx):
#     global p1
#     global p1_Member
#     global p2
#     global p2_Member
#     global gameStarted
#     global currentPlayer
#     global gameTurn
#     global winner
#     currentPlayer = ctx
#     if gameTurn == ctx.author.id:
#         if gameStarted:
#             increase = randint(1, 3)
#             if currentPlayer.author.id == p1_Member.id:
#                 gameTurn = p2_Member.id
#                 p1.max_attack = p1.max_attack + increase
#                 await ctx.send('''{} You trained your skills for a bit and gained {} attack\nYou now have a maximum attack of {}
# {} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(
#                     currentPlayer.author.mention, increase, p1.max_attack, p2_Member.mention))
#             if currentPlayer.author.id == p2_Member.id:
#                 gameTurn = p1_Member.id
#                 p2.max_attack = p2.max_attack + increase
#                 await ctx.send('''{} You trained your skills for a bit and gained {} attack\nYou now have a maximum attack of {}
# {} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(
#                     currentPlayer.author.mention, increase, p2.max_attack, p1_Member.mention))
#             hpcheck()
#     else:
#         await ctx.send('Please wait for your turn')

@client.command()
async def endfight(ctx):
    if ctx.author.guild_permissions.administrator:
        global gameStarted
        gameStarted = False
        await ctx.send('The active fight has been stopped')

client.run(os.getenv("ABYSS_BOT_TOKEN"))
