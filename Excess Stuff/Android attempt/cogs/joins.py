import os
import youtube_dl
import discord
import asyncio
import discord.voice_client
from pytube import YouTube
from discord.ext import commands
from discord.utils import find, get
#import cogs.music

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


class join_effects(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if self.client.onjoins and member.guild.id == 761652116375994448:
            if after.channel != before.channel:
                try:
                    if after.channel.name != 'The Void':
                        '''
                        c = self.client.get_command('hehe')
                        await self.client.invoke(c(member=member))
                        '''

                        '''
                        channel = discord.utils.get(member.guild.channels, name="server-commands")
                        #message = await channel.fetch_message(channel.last_message)
                        #ctx = await channel.last_message.guild.get_context(channel.last_message)
                        await channel.invoke(self.client.get_command('joins'), member=member)
                        '''

                        global queu
                        song = None
                        try:
                            song = self.client.joins[member.id]
                        except:
                            pass
                        if song != None and hasattr(member.voice, 'channel'):
                            global queu
                            await asyncio.sleep(1)

                            # try:
                            voiceChannel = member.voice.channel
                            voice = get(self.client.voice_clients, guild=member.guild)
                            if not member.voice:
                                pass
                            if not voice and voiceChannel:
                                await voiceChannel.connect()
                            if voice and voiceChannel != voice.channel:
                                await voice.disconnect()
                                await voiceChannel.connect()
                            if song not in queu:
                                queu.append(song)
                            if song in queu[0]:
                                voice = get(self.client.voice_clients, guild=member.guild)
                                if not voice.is_playing():
                                    server = member.guild
                                    voice_channel = server.voice_client
                                    if queu:
                                        player = await YTDLSource2.from_url(queu[0], loop=self.client.loop)
                                        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
                                        return

                        # except:
                        #     return
                except:
                    return

    @commands.command(pass_context=True)
    async def joins(self, ctx, *member):
        #if not member:
        #member = ctx.author
        global queu
        song = None
        try:
            song = self.client.joins[ctx.author.id]
        except:
            pass
        if song != None:
            global queu
            await asyncio.sleep(1)

            try:
                voiceChannel = ctx.voice.channel
                voice = get(self.client.voice_clients, guild=ctx.guild)
                if not member.voice:
                    pass
                if not voice and voiceChannel:
                    await voiceChannel.connect()
                if voice and voiceChannel != voice.channel:
                    await voice.disconnect()
                    await voiceChannel.connect()
            except:
                pass
            if song not in queu:
                queu.append(song)
            if song in queu[0]:
                voice = get(self.client.voice_clients, guild=ctx.guild)
                if not voice.is_playing():
                    server = member.guild
                    voice_channel = server.voice_client
                    if queu:
                        player = await YTDLSource2.from_url(queu[0], loop=self.client.loop)
                        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)


def setup(client):
    client.add_cog(join_effects(client))
