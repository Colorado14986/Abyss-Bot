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




##///////////////////////////////////////////////////////////////////////








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

    async with ctx.typing():
        player = await YTDLSource.from_url(queu[0], loop=client.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('**Now playing:** {}'.format(player.title))
    del(queu[0])
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
        ctx.send('Music resumed')
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
