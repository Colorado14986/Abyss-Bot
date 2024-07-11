import discord
import discord.voice_client
from discord.ext import commands
from discord_components import *

class help_embed(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx, *branch):
        if branch:
            branch2 = []
            for word in branch:
                branch2.append(word.lower())
            branch = branch2
        if not branch:
            # print('empty')
            embed = discord.Embed(title='Help:', description='Here are the current categories for help commands\nPlease run the command again with the category typed afterwards:')
            embed.add_field(name='Setup:', value='This is the required setup information for the bot', inline=False)
            embed.add_field(name='Categories:', value='\u200b', inline=False)
            embed.add_field(name='Fun:', value='These are the more fun commands')
            embed.add_field(name='Music:', value='These are the music commands')
            embed.add_field(name='Admin:', value='These are the admin specific commands')
            embed.add_field(name='Soundboards:', value='These are voice channel based soundboard commands')
            embed.add_field(name='\u200b', value='\u200b')
            embed.add_field(name='Other commands without categories:', value='\u200b', inline=False)
            embed.add_field(name=';reviews', value="A link to our resident film critic Glider's website")
            embed.add_field(name=';abusereport <Report>', value='Allows you to report mod abuse')
            embed.add_field(name=';suggest <Suggestion>', value='Allows you to make a suggestion for this bot')
            embed.add_field(name=';motwlb', value='Shows the activity leaderboard for the past week, may not be available in your server')

            embed.add_field(name='Text to Speech', value='Both of these commands say your message in the voice call (Provided you have either admin perms or or the role TTS Perms)', inline=False)
            embed.add_field(name=';; <message>', value='This will play your message in a male voice, please make sure you have a space after the prefix or the command will not run')
            embed.add_field(name=';;f <message>', value='This will play your message in a female voice(Same use as the male varient)')
            await ctx.send(embed=embed, components=[
                Button(label="test")
                ]
            )
            
            interaction = await self.client.wait_for("button_click", check = lambda i: i.component.label.startswith("test"))
            embed = discord.Embed(title='General Setup:', description='Here you will find the relavant information for setting up this bot when it first joins your server.')
            embed.add_field(name="Join/Leave messages", value="These will send to any channel nammed 'general', to change the destination, the message it self or disable them completely, please message TheColoradoKid#5302 and I'll sort it out for you", inline=False)
            embed.add_field(name="Admin logging", value="By default this will send to any channel named either 'logging' or 'logs', if you would like a differnt name plese message TheColoradoKid#5302 and I'll sort it out for you", inline=False)
            await interaction.send(embed=embed)
            

        if branch and 'setup' in branch:
            #print('setup')
            embed = discord.Embed(title='General Setup:', description='Here you will find the relavant information for setting up this bot when it first joins your server.')
            embed.add_field(name="Join/Leave messages", value="These will send to any channel nammed 'general', to change the destination, the message it self or disable them completely, please message TheColoradoKid#5302 and I'll sort it out for you", inline=False)
            embed.add_field(name="Admin logging", value="By default this will send to any channel named either 'logging' or 'logs', if you would like a differnt name plese message TheColoradoKid#5302 and I'll sort it out for you", inline=False)
            await ctx.send(embed=embed)

        if branch and 'fun' in branch:
            # print('fun')
            embed = discord.Embed(title='Fun Commands:', description='Here are all the current commands that aim to be fun:')
            embed.add_field(name=';feeling', value='Run this command to find how the bot is feeling')
            embed.add_field(name=';wyr', value='Provides a would you rather question with a voting system below it')
            embed.add_field(name=';8ball <Question> or ;8b <Question>', value='Ask the bot a question and see what fate decides')
            embed.add_field(name=';def <Search> or ;define <Search>', value='Searches for a term on urban dictionary and returns a definition and example (if a vailable)')
            embed.add_field(name=';gif <search>', value='Searches for a gif')
            embed.add_field(name=';pfp', value='This will display your current profile picture')
            embed.add_field(name=';afk', value='Mutes you and lists you as AFK in the sidebar')
            embed.add_field(name='Pokemon commands', value='Commands relating to the pokemon franchise', inline=False)
            embed.add_field(name=';pokemon <name> <m/f>(Gender) <y/n>(Shiny or not)', value='Gives information on the selected pokemon, you can choose between gender and shiny for the sprite provided')
            embed.add_field(name=';pmove <name> or ;pm <name>', value='Gives information on the move selected(Some moves will not have an english description, my apologies)')  

            embed.add_field(name='Dead by Daylight/Other', value='Commands designed for use in dbd custom games, but can be utilised elsewhere', inline=False)
            embed.add_field(name=';killer or ;killer <mention player>', value='Server mutes and deafens either yourself or the mentioned player')
            embed.add_field(name=';roll <Spaced names or else>', value='This chooses the killer for a custom game from a group of names you provide')            
            # embed.add_field(name=';quote', value='(in dev) Responds with a random quote')

            embed.add_field(name='Fight Game:(Still in development)', value='\u200b', inline=False)
            embed.add_field(name=';fight <mention>', value='This will initiate a fight with the mentioned person and both begin at 100 health')
            embed.add_field(name=';move <choice>', value='Here you choose your move for this turn:\n-attack(attempts to damage the opponent)\n-train(adds to the maximum attack damage you can deal on the random chance)\n-fortify(Increases your defense rating)')
            await ctx.send(embed=embed)

        elif branch and 'music' in branch:
            # print('music')
            embed = discord.Embed(title='Music Commands:', description='Here are all the commands relating to the music function of the bot:\nPlease be aware in advance there is no auto play atm:')
            embed.add_field(name=';join', value="Always run this command first if bot isn't connected:\nRun this command to make the bot join the channel")
            embed.add_field(name=';play', value='This is your generic play command, either adds the url to the queue, searches for a song, or plays the next item in the queue if no song is playing')
            #embed.add_field(name=';auto <on/off>', value='(Broken at the moment, please do not run as it breaks the bot) This command will turn on auto play for the duration of the queue')
            embed.add_field(name=';next', value='This command will either skip to the next song, or just play the next song if nothing is playing')
            embed.add_field(name=';stop', value='This command will stop the current track from playing')
            embed.add_field(name=';pause', value='This command will pause the current track')
            embed.add_field(name=';resume', value='This command will continue playing the paused track')
            embed.add_field(name=';remove <num>', value='This command will remove the specified track from the queue')
            #embed.add_field(name=';queue', value="This command will show the current queue")
            embed.add_field(name=';empty', value='This command will clear the queue')
            embed.add_field(name=';dc', value='This command will make the bot leave the channel')
            await ctx.send(embed=embed)
        elif branch and 'admin' in branch:
            # print('admin')
            embed = discord.Embed(title='Admin Commands:', description='Here are all the current admin-related commands\nYou must have the "administrator" perm to run these:')
            embed.add_field(name=';purge <num>', value='Your standard message clearing command')
            embed.add_field(name=';ban <@user> <Reason>', value='Bans the mentioned member and supplies a reason if included (It can be run without a reason given)')
            embed.add_field(name=';kick <@user> <Reason>', value='Kicks the mentioned member and supplies a reason if included (It can be run without a reason given)')
            embed.add_field(name=';mute <@user>', value='Mutes the mentioned user until the ;unmute command is ran or the role is removed manually')
            embed.add_field(name=';unmute <@user>', value='Removes the muted role from the mentioned member')
            embed.add_field(name=';endfight', value='Ends the current fight game, used in the event it breaks or is left half completed')
            embed.add_field(name=';reports', value='Shows all of the recent mod abuse reports')
            embed.add_field(name=';quote <name> <quote>', value="Adds a quote to the named person's best hits")
            await ctx.send(embed=embed)

        elif branch and 'soundboards' in branch:
            embed = discord.Embed(title='Soundboard Commands:', value='Here are a list of the current voice channel soundboard commands.')
            embed.add_field(name=';ht or ;hellothere', value='Obi-Wan says hello...')
            embed.add_field(name=';hg or ;highground', value='Now he has the highground...')
            embed.add_field(name=';fy or ;failedyou', value='Now he has failed you')

            embed.add_field(name=';brb', value='Arnold informs you of his intention to return...', inline=False)
            embed.add_field(name=';giggity', value='Quagmire, nuff said...', inline=True)
            embed.add_field(name=';dwarf', value='They like to do the diggy diggy of the holes...', inline=True)
            embed.add_field(name=';phil or ;insult', value="You're ugly...You're disgusting...and he will kill you")
            embed.add_field(name=';door', value='Phil makes some threats')
            embed.add_field(name=';ahoy', value="aHoY LaDiEs...Didn't see you there")
            embed.add_field(name=';gae', value='Why are you gay?')
            embed.add_field(name=';gay', value='Guy from community shouts "hah gayyy"')
            embed.add_field(name=';r2', value='R2-D2 does a big scream')
            embed.add_field(name=';jeff', value='You already know his name but here we are again...')
            embed.add_field(name=';gdonkey', value='Gordon calls you a donkey')
            embed.add_field(name=';mission', value='It has failed...')
            embed.add_field(name=';hehe', value='The legend Ainsley Harriot')
            embed.add_field(name=';simp', value='Simp, nuff said')
            embed.add_field(name=';family', value='Welcome...')
            embed.add_field(name=';wazzup', value='WAZZZZZUP!!!')
            embed.add_field(name=';job', value="I do think we've done a...pretty good *j-job so far*")

            embed.add_field(name=';13', value='This will play the song 13 Country and Western Greats by Montana Joe', inline=False)

            await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(colour = 0xFF0000)
        embed.add_field(name='If you would like to invite me to your server here is the link:', value='[Click Here:](https://discord.com/api/oauth2/authorize?client_id=796467856677142530&permissions=8&scope=bot)')
        await ctx.send(embed=embed)

    @commands.command()
    async def button(self, ctx):
        await ctx.send(
            "Hello, World!",
            components = [
                Button(label = "WOW button!", custom_id = "button1")
            ]
        )

        interaction = await self.client.wait_for("button_click", check = lambda i: i.custom_id == "button1")
        await interaction.send(content = "Button clicked!")



def setup(client):
    client.add_cog(help_embed(client))
