import os
import youtube_dl
import discord
import asyncio
import discord.voice_client
from pytube import YouTube
from discord.ext import commands
from discord.utils import find, get
from random import randint


youtube_dl.utils.bug_reports_message = lambda: ''
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

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

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
        num = randint(0, length)
        song = sound_urls[num]

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

    @commands.command()
    async def play(self, ctx, *args):
        global queu
        #global autom
        #queu = ['https://www.youtube.com/watch?v=2X_2IdybTV0F']
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
            if not args[0].startswith('https'):
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
            if args[0].startswith('https'):
                queu.append(args[0])
                url = args[0]

            await ctx.send("``{}`` added to queue!\n If the song doesn't start please either let the current song end and run ``;play``/``;next`` again or run ``;next`` to play now".format(url))
            try:
                p = self.client.get_command('play')
                await ctx.invoke(p)
            except:
                print('failed')

    @commands.command()
    async def next(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)
        voice.stop()
        await ctx.send('Loading next track:')
        p = self.client.get_command('play')
        await ctx.invoke(p)

    @commands.command()
    async def queue(self, ctx):
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

    @commands.command(aliases=['clear'])
    async def empty(self, ctx):
        global queu
        if queu:
            queu = []
        elif not queu:
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
        voice = get(self.client.voice_clients, guild=ctx.guild)
        voice.stop()
        await ctx.send('Music stopped')

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
        gif = 'https://tenor.com/view/minecraft-dwarf-diggy-diggy-hole-gif-19504482'
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
    
    
    @commands.command(pass_context=True, aliases=['Gecs', '100gecs', '100'])
    async def gecs(self, ctx):
        songs = ['https://www.youtube.com/watch?v=z97qLNXeAMQ', 'https://www.youtube.com/watch?v=9YO5ruvFSCU', 'https://www.youtube.com/watch?v=zahL_DQPM08']
        gif = 'https://tenor.com/view/gecs-danganronpa-fnaf-voltron-simpson-gif-18191678'
        name = 'gecs'
        await multi_sound(self, ctx, songs, gif, name)
        
def setup(client):
    client.add_cog(music(client))
