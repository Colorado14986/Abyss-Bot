import os
#import youtube_dl
import yt_dlp
import discord
import asyncio
import discord.voice_client
from pytube import YouTube
from discord.ext import commands
from discord.utils import find, get
from random import randint
#import cogs.music

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

class YTDLSource2(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=True):
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
                pl = self.client.get_command('play2')
                try:
                    await ctx.invoke(pl)
                    await ctx.send(gif_url)
                except:
                    print(f'{name} failed play')
        except:
            print('{} not, in voicechannel {}'.format(name, ctx.author))

async def multi_sound(self, ctx, sound_urls, gif_url, name):
    global queu
    # try:
    if ctx.author.id != 689876697918865421:
        try:
            length = len(sound_urls)-1
            clip = sound_urls[randint(0, length)]
            voiceChannel = ctx.message.author.voice.channel
            voice = get(self.client.voice_clients, guild=ctx.guild)
            if not ctx.message.author.voice:
                pass
            if not voice and voiceChannel:
                await voiceChannel.connect()
            if voice and voiceChannel != voice.channel:
                await voice.disconnect()
                await voiceChannel.connect()
            if clip not in queu:
                queu.append(clip)
                print(queu)
            if clip in queu[0]:
                pl = self.client.get_command('play2')
                try:
                    await ctx.invoke(pl)
                    message = await ctx.send(gif_url)
                except:
                    print(f'{name} no play')
        except:
            print('{}, not in voicechannel {}'.format(name, ctx.author))

async def multi_gif(self, ctx, sound_url, gif_urls, name):
    global queu
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
                pl = self.client.get_command('play2')
                try:
                    await ctx.invoke(pl)
                    length = len(gif_urls)-1
                    num = randint(0, length)
                    await ctx.send(gif_urls[num])
                except:
                    print(f'{name} no play')
        except:
            print('{}, not in voicechannel {}'.format(name, ctx.author))


class soundboard_(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def play2(self, ctx, *args):
        global queu
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
                            player = await YTDLSource2.from_url(queu[0], loop=self.client.loop)
                            voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

                        await ctx.send('**Now playing:** {}'.format(player.title))
                        del (queu[0])
                    elif not queu:
                        await ctx.send(
                            "You can't play if there isn't anything in the queue\nIf auto mode was on it has now been disabled, to use it gain please add to the queue and run ``;auto on``")
                        autom = False
            if args:
                global gueu
                search_keywords = ""
                print(args)
                for word in args:
                    search_keywords += word
                    search_keywords += '+'
                infosearched = ytdl.extract_info(f"ytsearch:{search_keywords}", download=False)
                url = infosearched['entries'][0]['webpage_url']
                queu.append(url)

                await ctx.send(
                    "``{}`` added to queue!\n If the song doesn't start please either let the current song end and run ``;play``/``;next`` again or run ``;next`` to play now".format(
                        url))
                try:
                    p = self.client.get_command('play2')
                    await ctx.invoke(p)
                except:
                    print('failed')

    @commands.command(context_pass=True, aliases=['ahoy ladies', 'ahoyladies'])
    async def ahoy(self, ctx, *, loop=None, stream=False):
        url = 'https://www.youtube.com/watch?v=ane8xXNWwns'
        gif = 'https://tenor.com/view/steve-joe-kerry-scoop-ahoy-ahoy-stranger-things-gif-17227867'
        name = 'Ahoy'
        await single_gif(self, ctx, url, gif, name)

    @commands.command(pass_context=True, aliases=['hellothere', 'hello there', 'Hellothere', 'Hello there'])
    async def ht(self, ctx):
        url = 'https://www.youtube.com/watch?v=eaEMSKzqGAg'
        gif = 'https://tenor.com/view/hello-there-hi-there-greetings-gif-9442662'
        name = 'Hellothere'
        await single_gif(self, ctx, url, gif, name)

    @commands.command(pass_context=True, aliases=['highground', 'Hg', 'Highground'])
    async def hg(self, ctx):
        url = 'https://www.youtube.com/watch?v=-H3o8r7JgGY'
        gif = 'https://tenor.com/view/laughing-tease-its-over-high-ground-gif-14651206'
        name = 'High ground'
        await single_gif(self, ctx, url, gif, name)

    @commands.command(pass_context=True, aliases=['failedyou', 'Failedyou', 'Fy'])
    async def fy(self, ctx):
        url = 'https://www.youtube.com/watch?v=VjCdNhz9fJk'
        gif = 'https://tenor.com/view/reaction-mrw-i-have-failed-you-obi-wan-kenobi-gif-4991213'
        name = 'Failed you'
        await single_gif(self, ctx, url, gif, name)

    @commands.command(pass_context=True, aliases=['Giggity', 'giggitygiggity', 'Giggitygiggity'])
    async def giggity(self, ctx):
        url = 'https://www.youtube.com/watch?v=YWFW0B9EBx0'
        gif = 'https://tenor.com/view/glenn-quagmire-family-guy-giggity-gif-4084933'
        name = 'Giggity'
        await single_gif(self, ctx, url, gif, name)

    @commands.command()
    async def gae(self, ctx):
        url = 'https://www.youtube.com/watch?v=iqMV1Mdm8ZA'
        gif = 'https://tenor.com/view/why-are-you-why-are-you-gay-pepe-julian-who-is-gay-you-are-gay-gif-15004128'
        name = 'Gae'
        await single_gif(self, ctx, url, gif, name)
        
    @commands.command()
    async def gay(self, ctx):
        url = 'https://www.youtube.com/watch?v=NAj26rVWK14'
        gif = 'https://tenor.com/view/ha-gay-ken-jeong-youre-gay-thats-gay-gif-16371455'
        name = 'Gay'
        await single_gif(self, ctx, url, gif, name)
        
    @commands.command()
    async def brb(self, ctx):
        url = 'https://www.youtube.com/watch?v=ZQn6VHIIGjE'
        gif = 'https://tenor.com/view/arnold-schwarzenegger-the-terminator-ill-be-back-gif-4367793'
        name = 'Brb'
        await single_gif(self, ctx, url, gif, name)

    '''
    @commands.command(pass_ctx=True, aliases=['Phil', 'insult', 'Insult'])
    async def phil(self, ctx):
        url = 'https://www.youtube.com/watch?v=HUbOYvpAh4U'
        gif = 'https://tenor.com/view/narcissistic-bitch-dr-phil-excuse-me-gif-13996756'
        name = 'Phil'
        await single_gif(self, ctx, url, gif, name)
    '''

    @commands.command(pass_context=True, aliases=['r2d2', 'r2scream', 'R2', 'R2d2', 'R2D2', 'R2scream'])
    async def r2(self, ctx):
        url = 'https://www.youtube.com/watch?v=D-0HbnyIMlY'
        gif = 'https://tenor.com/view/star-wars-r2d2-screaming-scream-panic-gif-4847617'
        name = 'R2'
        await single_gif(self, ctx, url, gif, name)

    @commands.command(pass_context=True, aliases=['Mission'])
    async def mission(self, ctx):
        url = 'https://www.youtube.com/watch?v=DQrUuRPDbwo'
        gif = 'https://tenor.com/view/fail-mission-failed-call-of-duty-ghost-gif-13071756'
        name = 'Mission failed'
        await single_gif(self, ctx, url, gif, name)

    @commands.command(pass_context=True, aliases=['Jeff'])
    async def jeff(self, ctx):
        url = 'https://www.youtube.com/watch?v=_nce9A5S5uM'
        gif = 'https://tenor.com/view/jeff-channing-tatum-22jump-street-disguise-gif-8025876'
        name = 'Jeff'
        await single_gif(self, ctx, url, gif, name)

    @commands.command(pass_context=True, aliases=['Hehe'])
    async def hehe(self, ctx):
        url = 'https://www.youtube.com/watch?v=EtCulrPSb3k'
        gif = 'https://tenor.com/view/he-hehe-boy-boi-boyi-gif-7890844'
        name = 'Hehe'
        await single_gif(self, ctx, url, gif, name)
    
    @commands.command(pass_context=True, aliases=['Simp'])
    async def simp(self, ctx):
        url = 'https://www.youtube.com/watch?v=TUEd7m_6VxA'
        gif = 'https://tenor.com/view/simping-simp-pewdiepie-you-are-pointing-gif-17092288'
        name = 'Simp'
        await single_gif(self, ctx, url, gif, name)
    
    @commands.command(aliases=['waz', 'wazz', 'wassup', 'wasssup', 'was', 'wass', 'wazzzup', 'wazzzzup', 'wassssup', 'wazzzzzup', 'wasssssup'])
    async def wazzup(self, ctx):
        url = 'https://www.youtube.com/watch?v=-J0v4tCPAao'
        gif = 'https://tenor.com/view/wazzup-on-the-phone-calling-screaming-gif-14915868'
        name = 'Wazzup'
        await single_gif(self, ctx, url, gif, name)

    @commands.command(aliases=['gd', 'Gd', 'Gdonkey'])
    async def gdonkey(self, ctx):
        url = 'https://www.youtube.com/watch?v=FVdjyIhg_bA'
        gif = 'https://tenor.com/view/gordon-ramsay-donkey-idiot-bitch-gif-4653529'
        name = 'Gdonkey'
        await single_gif(self, ctx, url, gif, name)

    @commands.command(aliases=['Chugjug'])
    async def chugjug(self, ctx):
        url = 'https://www.youtube.com/watch?v=gVVTBEvKILE'
        gif = 'https://tenor.com/view/peter-griffin-karaoke-family-guy-singing-reverb-gif-11412916'
        name = 'Chugjug'
        await single_gif(self, ctx, url, gif, name)

    @commands.command(aliases=['Familyguy'])
    async def familyguy(self, ctx):
        url = 'https://www.youtube.com/watch?v=eeNHV2C5m3w'
        gif = 'https://tenor.com/view/happy-dance-family-guy-gif-13301487'
        name = 'Family guy'
        await single_gif(self, ctx, url, gif, name)

    @commands.command()
    async def bs(self, ctx):
        url= 'https://www.youtube.com/watch?v=TwavkKJCd8E'
        gif = 'https://tenor.com/view/jack-jacksepticeye-bullshit-shit-bs-gif-21002469'
        name = 'Bullshit'
        await single_gif(self, ctx, url, gif, name)

    @commands.command()
    async def rave(self, ctx):
        url = 'https://www.youtube.com/watch?v=auAfDfZY7zI'
        gif = 'https://tenor.com/view/crab-safe-dance-gif-13211112'
        name = 'Rave'
        await single_gif(self, ctx, url, gif, name)

    @commands.command()
    async def wow(self, ctx):
        url = 'https://www.youtube.com/watch?v=TRIwAHX3aHM'
        gif = 'https://tenor.com/view/owen-wilson-owen-wilson-amazing-wonderful-gif-6103373'
        name = 'Wow'
        await single_gif(self, ctx, url, gif, name)

    @commands.command()
    async def didnot(self, ctx):
        url = 'https://www.youtube.com/watch?v=zLhoDB-ORLQ'
        gif = 'https://tenor.com/view/tommy-wiseau-i-did-not-hit-her-the-room-bullshit-gif-11523381'
        name = 'Did_Not'
        await single_gif(self, ctx, url, gif, name)

    @commands.command(aliases = ['uwelcom'])
    async def uwelcome(self, ctx):
        url = 'https://www.youtube.com/watch?v=nLmuLy1KfA8'
        gif = 'https://tenor.com/view/disney-moana-youre-welcome-maui-dance-gif-15810606'
        name = 'Uwelcom'
        await single_gif(self, ctx, url, gif, name)

    @commands.command()
    async def smonkey(self, ctx):
        url = 'https://www.youtube.com/watch?v=4NS0RQxojKY'
        gif = 'https://tenor.com/view/sniper-monkey-monke-sniper-monkey-king-kong-gif-20356254'
        name = 'SMonkey'
        await single_gif(self, ctx, url, gif, name)

    @commands.command()
    async def plan(self, ctx):
        url = 'https://www.youtube.com/watch?v=BI-iNE6zv90'
        gif = 'https://tenor.com/view/leonard-snart-captain-cold-wentworth-miller-legends-of-tomorrow-dcs-gif-17605180'
        name = 'Plan'
        await single_gif(self, ctx, url, gif, name)

    @commands.command()
    async def pgood(self, ctx):
        url = 'https://youtu.be/vjUqUVrXclE'
        gif = 'https://tenor.com/view/hey-thats-pretty-good-good-job-great-nice-gif-15704235'
        name = 'Pgood'
        await single_gif(self, ctx, url, gif, name)

    @commands.command()
    async def fbi(self, ctx):
        url = 'https://youtu.be/QQR7t712Mhg'
        gif = 'https://tenor.com/view/traffic-fbi-open-up-raid-gif-13450966'
        name = 'FBI'
        await single_gif(self, ctx, url, gif, name)

    @commands.command()
    async def bonk(self, ctx):
        url = 'https://www.youtube.com/watch?v=gwxTZaa3NgI'
        gif = 'https://tenor.com/view/horny-jail-go-to-horny-jail-bonk-doge-cheems-gif-17582752'
        name = 'Bonk'
        await single_gif(self, ctx, url, gif, name)

    @commands.command()
    async def hbn(self, ctx):
        url = 'https://www.youtube.com/watch?v=yhK6dPj-O-c'
        gif = 'https://tenor.com/view/no-drevil-gif-19685425'
        name = 'hbn'
        await single_gif(self, ctx, url, gif, name)

    @commands.command()
    async def wystm(self, ctx):
        url = 'https://www.youtube.com/watch?v=wUpBlFBLcRk'
        gif = 'https://tenor.com/view/ninja-rage-ninja-twitch-you-little-shit-the-fuck-you-say-the-fuck-you-said-gif-18318497'
        name = 'wystm'
        await single_gif(self, ctx, url, gif, name)

    @commands.command()
    async def box(self, ctx):
        url = 'https://youtu.be/N4IQjgXxZ-k'
        gif = 'https://tenor.com/view/hellraiser-pinhead-gif-15240203'
        name = 'box'
        await single_gif(self, ctx, url, gif, name)

    @commands.command()
    async def goofy(self, ctx):
        url = 'https://www.youtube.com/watch?v=0kAEthfslsE&ab_channel=cartoonvoicesguy'
        gif = 'https://tenor.com/view/goofy-laughing-ha-ha-ha-lol-lmao-gif-8614971'
        name = 'goofy'
        await single_gif(self, ctx, url, gif, name)

    @commands.command()
    async def shutup(self, ctx):
        url = 'https://www.youtube.com/watch?v=wFmYHGJf9KI'
        gif = 'https://tenor.com/view/smosh-shut-up-funny-lmao-cursed-ian-anthony-food-battle-gif-18751780'
        name = 'shutup'
        await single_gif(self, ctx, url, gif, name)

    @commands.command()
    async def sym(self, ctx):
        url = 'https://www.youtube.com/watch?v=yWWlaFxSC44'
        gif = 'https://tenor.com/view/deji-you-idiot-imbecile-gif-18416753'
        name = 'sym'
        await single_gif(self, ctx, url, gif, name)

    @commands.command()
    async def talent(self, ctx):
        url = 'https://www.youtube.com/watch?v=NyX5Qnj831M'
        gif = 'https://tenor.com/view/pure-talent-ashley-banjo-bgt-britains-got-talent-talented-gif-19871126'
        name = 'talent'
        await single_gif(self, ctx, url, gif, name)

    '''@commands.command()
    async def badass(self, ctx):
        url = 'https://www.youtube.com/watch?v=a5yzA-gi-fo'
        gif = 'https://tenor.com/view/badass-frank-suicide-gif-13827270'
        name = 'badass'
        await single_gif(self, ctx, url, gif, name)'''

    @commands.command(aliases=['ge'])
    async def exaggerated(self, ctx):
        url = 'https://www.youtube.com/watch?v=eBr_SasLrT4'
        gif = 'https://tenor.com/view/megamind-metroman-my-death-was-greatly-exaggerated-gif-19307347'
        name = 'exaggerated'
        await single_gif(self, ctx, url, gif, name)

    @commands.command(aliases=['blood'])
    async def bcontrol(self, ctx):
        url = 'https://youtu.be/_cUeUMxgUbI'
        gif = 'https://tenor.com/view/who-doctor-gif-5226137'
        name = 'Blood'
        await single_gif(self, ctx, url, gif, name)

    @commands.command(aliases=[])
    async def twitter(self, ctx):
        url = 'https://www.youtube.com/watch?v=gTJvG2UXGfk'
        gif = 'https://tenor.com/view/alec-hardy-bloody-twitter-broadchurch-twitter-david-tennant-gif-11484615'
        name = 'Twitter'
        await single_gif(self, ctx, url, gif, name)

    @commands.command(aliases=['yeahhh', 'YeahBaby', 'yeahbaby', 'Woohoo', 'woohoo'])
    async def Yeahhh(self, ctx):
        url = 'https://www.youtube.com/watch?v=sAXZbfLzJUg&ab'
        gif = 'https://tenor.com/view/cr1tikal-penguinz0-meme-woo-yeah-baby-gif-19316511'
        name = 'YeahBaby'
        await single_gif(self, ctx, url, gif, name)

    @commands.command(aliases=["Mercer"])
    async def mercer(self, ctx):
        url = 'https://youtu.be/sVSODL8cvSY'
        gif = 'https://tenor.com/view/travis-willingham-critical-role-fucking-mercer-matt-mercer-gif-27581806'
        name = 'Mercer'
        await single_gif(self, ctx, url, gif, name)

    @commands.command(aliases=["Mercerlong", "MercerLong", "mercerLong"])
    async def mercerlong(self, ctx):
        url = 'https://youtu.be/v0ODYsXLiaU'
        gif = 'https://tenor.com/view/travis-willingham-critical-role-fucking-mercer-matt-mercer-gif-27581806'
        name = 'MercerLong'
        await single_gif(self, ctx, url, gif, name)

    @commands.command(pass_context=True, aliases=['Meat'])
    async def meat(self, ctx):
        logging = discord.utils.get(ctx.guild.channels, name="logging")
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
            if 'https://www.youtube.com/watch?v=NC0s03q1THY' not in queu:
                queu.append('https://www.youtube.com/watch?v=NC0s03q1THY')
                print(queu)
            if 'https://www.youtube.com/watch?v=NC0s03q1THY' in queu[0]:
                pl = self.client.get_command('play2')
                try:
                    await ctx.invoke(pl)
                    ah = self.client.get_emoji(818226777645776979)
                    await ctx.message.add_reaction(ah)
                    await ctx.send('https://tenor.com/view/beat-my-meat-give-your-meat-rub-your-meat-random-gif-15095359')
                    await asyncio.sleep(3)
                    await ctx.channel.purge(limit=3)
                    await asyncio.sleep(1)
                    await logging.purge(limit=1)
                except:
                    print('meat play')
        except:
            print('meat, not in voicechannel {}'.format(ctx.author))

    @commands.command(pass_context=True, aliases=['Job'])
    async def job(self, ctx):
        sounds = ['https://www.youtube.com/watch?v=6jTsxWb2OZI', 'https://www.youtube.com/watch?v=nvVABjafCp0']
        gif = 'https://tenor.com/view/prettygoodjob-goodjob-dbd-deadbydaylight-mathieucote-gif-10764259'
        name = 'Job'
        await multi_sound(self, ctx, sounds, gif, name)

    @commands.command(aliases=['Tmo'])
    async def tmo(self, ctx):
        sound = 'https://www.youtube.com/watch?v=KGuWwakWaaw'
        gifs = ['https://tenor.com/view/take-me-out-date-show-irish-dance-paddy-aisling-costello-gif-14138189', 'https://tenor.com/view/james-take-me-out-dance-love-lift-gif-11117006', 'https://tenor.com/view/take-me-out-sjonnie-disapponted-gif-16826804']
        name = 'tmo'
        await multi_gif(self, ctx, sound, gifs, name)

    # @commands.command(pass_context=True)
    # async def mino(self, ctx):
    #     sounds = ['https://youtu.be/9rv6EALsI0s', 'https://youtu.be/7CLro-9Mw6M', 'https://youtu.be/n2Y_JOTryqk', 'https://youtu.be/YSNdU2q6eKg', 'https://youtu.be/AdKmSol6ALQ', 'https://youtu.be/b4S2pdIAVbU', 'https://youtu.be/QOM7ZvqAvGw', 'https://youtu.be/-DVS44hS_q0']
    #     gif = ''
    #     name = 'Mino'
    #     await multi_sound(self, ctx, sounds, gif, name)
    
    # @commands.command()
    # async def minotaur(self, ctx):
    #     url = 'https://youtu.be/8xM4hP4mjsM'
    #     gif = ''
    #     name = 'Minotaur'
    #     await single_gif(self, ctx, url, gif, name)

async def setup(client):
    await client.add_cog(soundboard_(client))
