from discord.ext import commands

class randoms(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('Skyra'):
            guild = self.client.get_guild(761652116375994448)
            bots = guild.get_channel(761676002366586881)
            if message.channel.id not in [806531215762653204, 761676002366586881, 803255421606952965]:
                await message.channel.send("That can't be used here, please go to {}".format(bots.mention))

        elif message.content.startswith('skyra'):
            guild = self.client.get_guild(761652116375994448)
            bots = guild.get_channel(761676002366586881)
            print(message.channel)
            if message.channel.id not in [806531215762653204, 761676002366586881, 803255421606952965]:
                await message.channel.send("That can't be used here, please go to {}".format(bots.mention))

        elif message.content.startswith('S!'):
            guild = self.client.get_guild(761652116375994448)
            bots = guild.get_channel(761676002366586881)
            if message.channel.id not in [806531215762653204, 761676002366586881, 803255421606952965]:
                await message.channel.send("That can't be used here, please go to {}".format(bots.mention))

        elif message.content.startswith('s!'):
            guild = self.client.get_guild(761652116375994448)
            bots = guild.get_channel(761676002366586881)
            if message.channel.id not in [806531215762653204, 761676002366586881, 803255421606952965]:
                await message.channel.send("That can't be used here, please go to {}".format(bots.mention))


        elif 'Clean <Num:Whole number>' in message.content:
            await message.delete()

        #if message.author.id == 747838795704959027 and message.guild.id == 761652116375994448:
            #await message.channel.send('Praise him')
            #await message.channel.send('Praise him')

async def setup(client):
    await client.add_cog(randoms(client))
