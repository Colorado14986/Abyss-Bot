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



#//////////////////////////////////////////////////////////////





# @client.command()
# async def play(ctx, url : str):
#     song_there = os.path.isfile('song.mp3')
#     try:
#         if song_there:
#             os.remove('song.mp3')
#     except PermissionError:
#         await ctx.send('Please wait for the current playing music to end or use the ``;stop`` command')
#     voiceChannel = ctx.message.author.voice.channel
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     connected = ctx.author.voice
#     if not voice and voiceChannel:
#         await voiceChannel.connect()
#     if voice:
#         await voice.disconnect()
#         await voiceChannel.connect()
#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#     }
#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])
#     for file in os.listdir("./"):
#         if file.endswith('.mp3'):
#             os.rename(file, 'song.mp3')
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     voice.play(discord.FFmpegPCMAudio('song.mp3'))
#
#
# @client.command()
# async def dc(ctx):
#     channel = ctx.message.author.voice.channel
#     voice = get(client.voice_clients, guild=ctx.guild)
#     if voice and voice.is_connected():
#         await voice.disconnect()
#     else:
#         await ctx.send("I'm not in a voice channel.")
#
# @client.command()
# async def pause(ctx):
#     voice = get(client.voice_clients, guild=ctx.guild)
#     if voice and voice.is_playing():
#         voice = get(client.voice_clients, guild=ctx.guild)
#         voice.pause()
#     else:
#         await ctx.send('Nothing is being played at the moment')
#
# @client.command()
# async def resume(ctx):
#     voice = get(client.voice_clients, guild=ctx.guild)
#     if voice.is_paused:
#         voice.resume()
#     else:
#         await ctx.send('Nothing is paused at this time')
#
# @client.command()
# async def stop(ctx):
#     voice = get(client.voice_clients, guild=ctx.guild)
#     voice.stop()
