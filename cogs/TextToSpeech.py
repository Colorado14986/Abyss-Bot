import os
# import youtube_dl
import yt_dlp
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import discord
import datetime
import asyncio
import time
import discord.voice_client
from pytube import YouTube
from random import randint
from discord.ext import commands
from discord.utils import find, get
from gtts import gTTS
import pyttsx3
import re

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


class text_to_speech(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_ctx=True, aliases=[';'])
    async def say(self, ctx, *, args):
        role = discord.utils.find(lambda r: r.name == 'TTS Perms', ctx.message.guild.roles)
        try:
            role2 = discord.utils.find(lambda r: r.name == 'Peeps', ctx.message.guild.roles)
        except:
            pass
        if role in ctx.author.roles or ctx.author.guild_permissions.administrator or role2 in ctx.author.roles or ctx.channel.id == 1052354451836502088:
            if ctx.author.id != 689876697918865421:
                sentence = ''
                args = re.sub(r"<:", "", args)
                args = re.sub(r":\d+>", "", args)
                args = re.sub(r"<a:", "", args)
                for word in args:
                    sentence += word
                if ctx.author.nick is not None:
                    print(f'{ctx.author.nick} says: {sentence}')
                else:
                    print(f'{ctx.author} says: {sentence}')
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
                    print('tts no vc join')
                guild = ctx.guild
                voice_client: discord.VoiceClient = discord.utils.get(self.client.voice_clients, guild=guild)
                engine = pyttsx3.init()
                engine.setProperty('rate', 130)
                engine.save_to_file(sentence, f'./Audio/TTS/{ctx.guild.id}[Male].mp3')
                engine.runAndWait()

                audio_source = discord.FFmpegPCMAudio(f'./Audio/TTS/{ctx.guild.id}[Male].mp3')
                if not voice_client.is_playing():
                    voice_client.play(audio_source, after=None)

    @commands.command(pass_ctx=True, aliases=[';f'])
    async def fsay(self, ctx, *, args):
        role = discord.utils.find(lambda r: r.name == 'TTS Perms', ctx.message.guild.roles)
        try:
            role2 = discord.utils.find(lambda r: r.name == 'Peeps', ctx.message.guild.roles)
        except:
            pass
        if role in ctx.author.roles or ctx.author.guild_permissions.administrator or role2 in ctx.author.roles or ctx.channel.id == 1052354451836502088:
            if ctx.author.id != 689876697918865421:
                sentence = ''
                args = re.sub(r"<:", "", args)
                args = re.sub(r":\d+>", "", args)
                args = re.sub(r"<a:", "", args)
                for word in args:
                    sentence += word
                if ctx.author.nick is not None:
                    print(f'{ctx.author.nick} fsays: {sentence}')
                else:
                    print(f'{ctx.author} fsays: {sentence}')
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
                    print('tts no vc join')
                guild = ctx.guild
                voice_client: discord.VoiceClient = discord.utils.get(self.client.voice_clients, guild=guild)
                engine = pyttsx3.init()
                engine.setProperty('rate', 130)
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[1].id)
                engine.save_to_file(sentence, f'./Audio/TTS/{ctx.guild.id}[Female].mp3')
                engine.runAndWait()

                audio_source = discord.FFmpegPCMAudio(f'./Audio/TTS/{ctx.guild.id}[Female].mp3')
                if not voice_client.is_playing():
                    voice_client.play(audio_source, after=None)

async def setup(client):
    await client.add_cog(text_to_speech(client))
