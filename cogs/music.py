import os
#import youtube_dl
import yt_dlp
import discord
import asyncio
import discord.voice_client
from pytube import YouTube, Playlist
from discord.ext import commands
from discord.utils import find, get
import random


yt_dlp.utils.bug_reports_message = lambda: ''
global queu
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

ytdl = yt_dlp.YoutubeDL(ytdl_format_options)

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

async def single_gif(self, ctx, sound_url, gif_url, name):
    global queu
    # try:
    if ctx.author.id != 689876697918865421:
        try:
            voiceChannel = ctx.message.author.voice.channel
            voice = get(self.client.voice_clients, guild=ctx.guild)
            if not ctx.message.author.voice:
                pass
            if not voice and voiceChannel:
                await voiceChannel.connect()
            if voice and voiceChannel != voice.channel:
                await voice.disconnect()
                await voiceChannel.connect()
            if sound_url not in queu:
                queu.append(sound_url)
                print(queu)
            if sound_url in queu[0]:
                pl = self.client.get_command('play')
                try:
                    await ctx.invoke(pl)
                    await ctx.send(gif_url)
                except:
                    print(f'{name} failed play')
        except:
            print('{} not, in voicechannel {}'.format(name, ctx.author))

async def multi_sound(self, ctx, sound_urls, gif_url, name):
    global queu
    length = len(sound_urls)-1
    num = random.randint(0, length)
    song = sound_urls[num]

    if ctx.author.id != 689876697918865421:
        try:
            voiceChannel = ctx.message.author.voice.channel
            voice = get(self.client.voice_clients, guild=ctx.guild)
            if not ctx.message.author.voice:
                pass
            if not voice and voiceChannel:
                await voiceChannel.connect()
            if voice and voiceChannel != voice.channel:
                await voice.disconnect()
                await voiceChannel.connect()
            if song not in queu:
                queu.append(song)
                print(queu)
            if queu[0] == song:
                pl = self.client.get_command('play')
                try:
                    await ctx.invoke(pl)
                    await ctx.send(gif_url)
                except:
                    print(f'{name} failed play')
        except:
            print('{}, in voicechannel {}'.format(name, ctx.author))

async def from_file(self, ctx, filename, title, name, *image_file):
    print(image_file)
    if ctx.author.id != 689876697918865421:
        try:
            voiceChannel = ctx.message.author.voice.channel
            voice = get(self.client.voice_clients, guild=ctx.guild)
            if not ctx.message.author.voice:
                pass
            if not voice and voiceChannel:
                await voiceChannel.connect()
            if voice and voiceChannel != voice.channel:
                await voice.disconnect()
                await voiceChannel.connect()
        except:
            print(f'{name} no vc join')
        voiceChannel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)
        voice_client: discord.VoiceClient = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        audio_source = discord.FFmpegPCMAudio(f'./Audio/{filename}')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)
            if image_file:
                await ctx.send(f'**Now Playing:** {title}', file=discord.File(f'./Audio/Images/{image_file[0]}'))
            if not image_file:
                await ctx.send(f'**Now Playing:** {title}')

class music(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        opt = 0
        try:
            opt = len(member.guild.voice_client.channel.members)
        except:
            pass
        voice = get(self.client.voice_clients, guild=member.guild)
        if opt == 1:
            try:
                await voice.disconnect()
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
                    if os.path.isfile('latestTTS.mp3'):
                        try:
                            os.remove('latestTTS.mp3')
                        except:
                            print('')

                
            except:
                pass


    @commands.command()
    async def join(self, ctx):
        voiceChannel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if not ctx.message.author.voice:
            await('You are not connected to a voice channel')
            return
        if not voice and voiceChannel:
            await voiceChannel.connect()
        if voice and voiceChannel != voice.channel:
            await voice.disconnect()
            await voiceChannel.connect()


    @commands.command(aliases=["PLAY"])
    async def play(self, ctx, *args):
        async def after_play(ctx):
            global queu
            del(queu[0])
            server = ctx.message.guild
            voice_channel = server.voice_client
            player = await YTDLSource.from_url(queu[0], loop=self.client.loop)
            voice_channel.play(player, after=lambda e: asyncio.run_coroutine_threadsafe(after_play(ctx), self.client.loop))
            await ctx.send('**Now playing:** {}'.format(player.title))
            print(player.title)
        global queu
        print(queu)
        p = self.client.get_command('play')
        if ctx.author.id != 689876697918865421:
            try:
                voiceChannel = ctx.message.author.voice.channel
                voice = get(self.client.voice_clients, guild=ctx.guild)
                if not ctx.message.author.voice:
                    pass
                if not voice and voiceChannel:
                    await voiceChannel.connect()
                if voice and voiceChannel != voice.channel:
                    await voice.disconnect()
                    await voiceChannel.connect()
            except:
                print(";play faIled join")
            if not args:
                voice = get(self.client.voice_clients, guild=ctx.guild)
                if not voice.is_playing():
                    server = ctx.message.guild
                    voice_channel = server.voice_client
                    if queu:
                        async with ctx.typing():
                            player = await YTDLSource.from_url(queu[0], loop=self.client.loop)
                            voice_channel.play(player, after=lambda e: asyncio.run_coroutine_threadsafe(after_play(ctx), self.client.loop))
                        await ctx.send('**Now playing:** {}'.format(player.title))
                        
                    elif not queu:
                        await ctx.send("You can't play if there isn't anything in the queue\nIf auto mode was on it has now been disabled, to use it gain please add to the queue and run ``;auto on``")
                        autom = False
            if args:
                if not args[0].startswith('https'):
                    global gueu
                    search_keywords = ""
                    print(args)
                    for word in args:
                        search_keywords += word
                        search_keywords += '+'
                    infosearched = ytdl.extract_info(f"ytsearch:{search_keywords}", download=False)
                    url = infosearched['entries'][0]['webpage_url']
                    queu.append(url)
                if args[0].startswith('https'):
                    if 'playlist' in args[0]:
                        playlist = Playlist(args[0])
                        queu.extend(playlist)
                    else:
                        queu.append(args[0])
                        url = args[0]
                        await ctx.send("``{}`` added to queue!\n If the song doesn't start please either let the current song end and run ``;play``/``;next`` again or run ``;next`` to play now".format(url))
                
                voice = get(self.client.voice_clients, guild=ctx.guild)
                if not voice.is_playing():
                    server = ctx.message.guild
                    voice_channel = server.voice_client
                    if queu:
                        async with ctx.typing():
                            player = await YTDLSource.from_url(queu[0], loop=self.client.loop)
                            voice_channel.play(player, after=lambda e: asyncio.run_coroutine_threadsafe(after_play(ctx), self.client.loop))
                        await ctx.send('**Now playing:** {}'.format(player.title))
                        
                    elif not queu:
                        await ctx.send("You can't play if there isn't anything in the queue\nIf auto mode was on it has now been disabled, to use it gain please add to the queue and run ``;auto on``")
                        autom = False

    @commands.command()
    async def shuffle(self, ctx, *args):
        global queu
        playlist2 = []
        print(queu)
        if args:
            if 'https' in args[0]:
                if 'playlist' in args[0]:
                    playlist = Playlist(args[0])
                    playlist2.extend(playlist)
                    random.shuffle(playlist2)
                    queu.extend(playlist2)
                    pl = self.client.get_command('play')
                    try:
                        await ctx.invoke(pl)
                    except:
                        pass
                else:
                    await ctx.send("Please use a playlist if you're going to add a link to this command, otherwise use `;play`")
        else:
            random.shuffle(queu)
            print(queu)

    @commands.command(aliases=['skip'])
    async def next(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)
        voice.stop()
        await ctx.send('Loading next track:')

    @commands.command()
    async def queue(self, ctx):
        global queu
        print(queu)

    @commands.command(aliases=['clear'])
    async def empty(self, ctx):
        global queu
        if queu:
            queu = []
        elif not queu:
            if ctx.guild.id == 915014434546659360:
                await ctx.send('The queue is already empty\n(If you are a gym leader you probably meant to use `;clean`)')
            else:
                await ctx.send('The queue is already empty')

    @commands.command()
    async def remove(self, ctx, num):
        global queu
        num = int(num)
        num = num - 1
        if queu:
            del queu[num]
            await ctx.send('Item {} removed from the queue'.format(num))
        elif not queu:
            await ctx.send('You cant do that, the queue is already empty')

    @commands.command()
    async def stop(self, ctx):
        global queu
        queu = []
        voice = get(self.client.voice_clients, guild=ctx.guild)
        voice.stop()
        await ctx.send('https://cdn.discordapp.com/attachments/1094625953289867384/1208538470092513381/fnr4O2t.gif?ex=65e3a628&is=65d13128&hm=c0b52c1677f54c11bfd989c5c3c866c4cb21f0aff24b3e61add7078882260e41&')

    @commands.command()
    async def pause(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
            await ctx.send('Music paused, run ``;resume`` to continue')
        else:
            await ctx.send('Nothing is being played at the moment')

    @commands.command()
    async def resume(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_paused:
            voice.resume()
            await ctx.send('Music resumed')
        else:
            await ctx.send('Nothing is paused at this time')
            
    @commands.command()
    async def dc(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.disconnect()
        else:
            await ctx.send("I'm not in a voice channel.")
        voice = get(self.client.voice_clients, guild=ctx.guild)
        p = self.client.get_command('spurge')
        await ctx.invoke(p)

    @commands.command()
    async def spurge(self, ctx):
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
            if os.path.isfile('latestTTS.mp3'):
                try:
                    os.remove('latestTTS.mp3')
                except:
                    print('')
                    
    @commands.command(pass_context=True, aliases=['diggy', 'Dwarf', 'diggydiggy', 'Diggy', 'Diggydiggy', 'Diggydiggyhole', 'diggydiggyhole'])
    async def dwarf(self, ctx):
        sound = 'https://www.youtube.com/watch?v=ytWz0qVvBZ0'
        gif = 'https://44.media.tumblr.com/38d362b3ad8d32b79081599ffa878833/tumblr_n8jyi3z8xT1qf4l9ao3_r1_500.gif'
        name = 'Dwarf'
        await single_gif(self, ctx, sound, gif, name)

    @commands.command(pass_context=True,
                      aliases=['Door'])
    async def door(self, ctx):
        sound = 'https://www.youtube.com/watch?v=aj5mm8oXZsc'
        gif = 'https://tenor.com/view/heres-johnny-stalker-creep-gif-6085004'
        name = 'Door'
        await single_gif(self, ctx, sound, gif, name)

    @commands.command()
    async def rdr(self, ctx):
        sound = 'https://www.youtube.com/watch?v=j8068ZrwicQ'
        gif = 'https://tenor.com/view/red-dead-redemption2-woody-toy-story-gif-12798603'
        name = 'RDR'
        await single_gif(self, ctx, sound, gif, name)
        
    @commands.command()
    async def pizza(self, ctx):
        sound = 'https://www.youtube.com/watch?v=V5gdQ7G8Jqo'
        gif = 'https://tenor.com/view/spider-man-pizza-time-pizza-day-pizza-dinner-gif-16271126'
        name = 'Pizza time'
        await single_gif(self, ctx, sound, gif, name)

    @commands.command(aliases=['13'])
    async def country_western(self, ctx):
        File = 'Mississippi_Whisper_13_Country_Greats.mp3'
        title = '13 Country and Western Greats by Montana Joe'
        image = '13_greats.png'
        name = '13'
        await from_file(self, ctx, File, title, name, image)

    @commands.command(aliases=['OhLook', 'ohlook', 'Oh_Look', 'oh_look', 'ol', 'Ol'])
    async def Ohlook(self, ctx):
        File = 'Oh_Look.mp4'
        title = 'The story of a young talker...'
        name = 'Oh look'
        await from_file(self, ctx, File, title, name)
    
    @commands.command()
    async def family(self, ctx):
        File = 'Welcome_to_the_family_son.mp3'
        title = 'A welcome...'
        name = 'family'
        await from_file(self, ctx, File, title, name)
        await ctx.send('https://tenor.com/view/welcome-to-the-family-son-resident-evil7-welcome-to-the-family-justnads-resident-evil-gif-20743783')

    @commands.command()
    async def neverbefore(self, ctx):
        File = 'Never_before_have_i_been_so_offended.mp4'
        title = '...Never before'
        name = 'Offended'
        await from_file(self, ctx, File, title, name)
        await ctx.send('https://tenor.com/view/offended-agree-gif-18718132')

    @commands.command()
    async def goofed(self, ctx):
        File = 'You dun goofed.mp4'
        title = 'You dun Goofed'
        name = 'Goofed'
        await from_file(self, ctx, File, title, name)
        await ctx.send('https://i.imgflip.com/gpdf3.gif')

    @commands.command()
    async def neya(self, ctx):
        File = 'Ney-a.mp4'
        title = 'A lesson in pronunciation...'
        name = 'neya'
        await from_file(self, ctx, File, title, name)

    @commands.command()
    async def dyht(self, ctx):
        File = 'Do You Honestly Think.mp3'
        title = "Do you honestly think you're fucking funny...seriously?"
        name = 'DYHT'
        await from_file(self, ctx, File, title, name)

    @commands.command()
    async def hey(self, ctx):
        File = 'Hey Everyone.mp4'
        title = "Hey Everyone, sorry I'm late"
        name = 'Hey'
        await from_file(self, ctx, File, title, name)

    @commands.command()
    async def everybody(self, ctx):
        File = "Doctor who_ Everybody lives_Trim.mp4"
        title = "Just this once... EVERYBODY LIVES!!"
        name = 'Lives'
        await from_file(self, ctx, File, title, name)
        await ctx.send('https://tenor.com/view/lives-alive-ninth-doctor-doctorwho-gif-21761280')
    
    @commands.command(aliases = ['fu', 'Fu', 'How'])
    async def how(self, ctx):
        File = "Fuck you, that's how.mp4"
        title = 'Telling you how it happened'
        name = 'How'
        await from_file(self, ctx, File, title, name)
        await ctx.send(file= discord.File('./Audio/Images/Fuck-You-thats-how.gif'))

    @commands.command(aliases=['ihy'])
    async def IHY(self, ctx):
        File = 'i-hate-you-no-you-dont.mp3'
        title = "A message of hate"
        name = 'IHY'
        await from_file(self, ctx, File, title, name)
        await ctx.send('https://tenor.com/view/doctor-who-river-song-i-hate-you-no-you-dont-matt-smith-gif-12107700')
    
    @commands.command(aliases=[])
    async def space(self, ctx):
        File = 'Space.mp4'
        title = "Space"
        name = 'Space'
        await from_file(self, ctx, File, title, name)
        await ctx.send('https://tenor.com/view/space-tim-curry-gif-7935778')

    @commands.command()
    async def storm(self, ctx):
        File = 'STORRRMMM.mp4'
        title = "Storm"
        name = 'Storm'
        await from_file(self, ctx, File, title, name)


    '''
    @commands.command(pass_context=True, aliases=['Gecs', '100gecs', '100'])
    async def gecs(self, ctx):
        songs = ['https://www.youtube.com/watch?v=z97qLNXeAMQ', 'https://www.youtube.com/watch?v=9YO5ruvFSCU', 'https://www.youtube.com/watch?v=zahL_DQPM08']
        gif = 'https://tenor.com/view/gecs-danganronpa-fnaf-voltron-simpson-gif-18191678'
        name = 'gecs'
        await multi_sound(self, ctx, songs, gif, name)
    '''

    @commands.command(pass_context=True, aliases=['Ash'])
    async def ash(self, ctx):
        songs = ['https://youtu.be/qrv8XcTniRM', 'https://youtu.be/vNz87FMk9zM', 'https://youtu.be/DxWSBRN5sUA', 'https://youtu.be/zawQKNjsg_4', 'https://youtu.be/FDefI6Is228', 'https://youtu.be/v2rWjVP1_JA', 'https://youtu.be/iYY07cEz_6A', 'https://youtu.be/D6OVZIv3e1Y', 'https://youtu.be/k_5LE7pTJjo', 'https://youtu.be/jVaU_3LbeTk', 'https://youtu.be/AGSiYqoAhE8']
        gif = 'https://tenor.com/view/ready-gun-chainsaw-gif-10358244'
        name = 'Ash'
        await multi_sound(self, ctx, songs, gif, name)
        
async def setup(client):
    await client.add_cog(music(client))
