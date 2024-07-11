import discord.voice_client
from random import randint
from discord.ext import commands

class fightCommands(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.p1 = None
        self.client.p1_Member = None
        self.client.p2 = None
        self.client.p2_Member = None
        self.client.gameStarted = False
        self.client.winner = None
        self.client.gameTurn = None
        
    
    '''@commands.command(pass_context=True)
    async def ftest(self, ctx):
        print(self.client.p1, self.client.p1_Member, self.client.p2, self.client.p2_Member, self.client.gameStarted, self.client.winner)'''

    @commands.command(pass_context=True, aliases=['fight'])
    async def startfight(self, ctx, member: discord.Member):
        class playerData:
            user = ''
            health = 50
            max_attack = 5
            defense = 0
        self.client.winner = None
        if not self.client.gameStarted:
            self.client.p1 = playerData()
            self.client.p2 = playerData()
            self.client.p1.user = ctx.author.id
            self.client.p1_Member = ctx.author
            self.client.p2.user = member.id
            self.client.p2_Member = member
            if self.client.p1_Member.id != self.client.p2_Member.id:
                print('\nFight Started:')
                print(self.client.p1_Member)
                print(self.client.p2_Member)
                await ctx.send('''Fight Started:
                {} vs {}'''.format(self.client.p1_Member.mention, self.client.p2_Member.mention))
                self.client.gameStarted = True
                self.client.gameTurn = self.client.p2_Member.id
                await ctx.send('{} it is your turn:\nPlease run ``;move`` along with attack, fortify, or train'.format(
                    self.client.p2_Member.mention))
            if self.client.p1_Member.id == self.client.p2_Member.id:
                await ctx.send("You don't need my help to fight yourself")
        else:
            await ctx.send('A fight has already been started, please wait until it is completed and try again')

    @commands.command()
    async def move(self, ctx, choice):
        def hpcheck(self):
            if self.client.p1.health < 0:
                self.client.winner = self.client.p2_Member
                self.client.gameStarted = False

            if self.client.p2.health < 0:
                self.client.winner = self.client.p1_Member
                self.client.gameStarted = False

        print('\n{}\nhp:{}\nattack:{}\ndefense:{}'.format(self.client.p1_Member, self.client.p1.health, self.client.p1.max_attack, self.client.p1.defense))
        print('\n{}\nhp:{}\nattack:{}\ndefense:{}'.format(self.client.p2_Member, self.client.p2.health, self.client.p2.max_attack, self.client.p2.defense))
        self.client.currentPlayer = ctx
        if self.client.gameTurn != ctx.author.id and self.client.gameStarted is True:
            await ctx.send('Please wait for your turn')
        if self.client.gameTurn == ctx.author.id and self.client.gameStarted:
            if choice == 'train':
                increase = randint(1, 5)
                if self.client.currentPlayer.author.id == self.client.p1_Member.id:
                    self.client.gameTurn = self.client.p2_Member.id
                    self.client.p1.max_attack = self.client.p1.max_attack + increase
                    await ctx.send('''{} You trained your skills for a bit and gained {} attack\nYou now have a maximum attack of {}
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(self.client.currentPlayer.author.mention, increase, self.client.p1.max_attack, self.client.p2_Member.mention))
                if self.client.currentPlayer.author.id == self.client.p2_Member.id:
                    self.client.gameTurn = self.client.p1_Member.id
                    self.client.p2.max_attack = self.client.p2.max_attack + increase
                    await ctx.send('''{} You trained your skills for a bit and gained {} attack\nYou now have a maximum attack of {}
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(self.client.currentPlayer.author.mention, increase, self.client.p2.max_attack, self.client.p1_Member.mention))

            if choice == 'fortify':
                increase = randint(1, 5)
                if self.client.currentPlayer.author.id == self.client.p1_Member.id:
                    self.client.gameTurn = self.client.p2_Member.id
                    self.client.p1.defense = self.client.p1.defense + increase
                    await ctx.send('''{} You have flexed really hard and gained {} defense\nYou now have a defense of {}
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(self.client.currentPlayer.author.mention, increase, self.client.p1.defense, self.client.p2_Member.mention))
                if self.client.currentPlayer.author.id == self.client.p2_Member.id:
                    self.client.gameTurn = self.client.p1_Member.id
                    self.client.p2.defense = self.client.p2.defense + increase
                    await ctx.send('''{} You have flexed really hard and gained {} defense\nYou now have a defense of {}
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(self.client.currentPlayer.author.mention, increase, self.client.p2.defense, self.client.p1_Member.mention))

            if choice == 'attack':
                if ctx.author.id == self.client.p1_Member.id:
                    self.client.gameTurn = self.client.p2_Member.id
                    damage = randint(0, self.client.p1.max_attack)
                    truedamage = damage - self.client.p2.defense
                    if truedamage > 0 and damage != self.client.p1.max_attack:
                        self.client.p2.health = self.client.p2.health - truedamage
                    if damage == self.client.p1.max_attack:
                        self.client.p2.health = self.client.p2.health - damage

                    if self.client.p2.defense > 0 and damage != self.client.p1.max_attack:
                        if truedamage > 0:
                            await ctx.send('''You attempted to land a hit of {}, but after {} defended you only dealt {} leaving them with {} health
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(damage, self.client.p2_Member.mention, truedamage, self.client.p2.health, self.client.p2_Member.mention))
                        if truedamage <= 0:
                            await ctx.send('''You tried to attack but were blocked with ease by {}
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(self.client.p2_Member.mention, self.client.p2_Member.mention))
                    if self.client.p2.defense == 0 and truedamage > 0:
                        await ctx.send('''You dealt a perfect hit of {} as {} has no defense leaving them with {} health
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(damage, self.client.p2_Member.mention, self.client.p2.health, self.client.p2_Member.mention))
                    if damage == self.client.p1.max_attack and self.client.p2.defense != 0:
                        await ctx.send('''You dealt a critical blow of {} dealing full damage and bypassing {}'s defences leaving them with {} health
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(damage, self.client.p2_Member.mention, self.client.p2.health, self.client.p2_Member.mention))

                    hpcheck(self)

                if ctx.author.id == self.client.p2_Member.id:
                    self.client.gameTurn = self.client.p1_Member.id
                    damage = randint(0, self.client.p2.max_attack)
                    truedamage = damage - self.client.p1.defense
                    if truedamage > 0 and damage != self.client.p2.max_attack:
                        self.client.p1.health = self.client.p1.health - truedamage
                    if damage == self.client.p2.max_attack:
                        self.client.p1.health = self.client.p1.health - damage

                    if self.client.p1.defense > 0 and damage != self.client.p2.max_attack:
                        if truedamage > 0:
                            await ctx.send('''You attempted to land a hit of {}, but after {} defended you only dealt {} leaving them with {} health
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(damage, self.client.p1_Member.mention, truedamage, self.client.p1.health, self.client.p1_Member.mention))
                        if truedamage <= 0:
                            await ctx.send('''You tried to attack but were blocked with ease by {}
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(self.client.p1_Member.mention, self.client.p1_Member.mention))
                    if self.client.p1.defense == 0 and truedamage > 0:
                        await ctx.send('''You dealt a perfect hit of {} as {} has no defense leaving them with {} health
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(damage,
                                                                                                      self.client.p1_Member.mention,
                                                                                                      self.client.p1.health,
                                                                                                      self.client.p1_Member.mention))
                    if damage == self.client.p1.max_attack and self.client.p1.defense != 0:
                        await ctx.send('''You dealt a critical blow of {} dealing full damage and bypassing {}'s defences leaving them with {} health
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(damage, self.client.p1_Member.mention, self.client.p1.health, self.client.p1_Member.mention))
                    hpcheck(self)

        if not self.client.gameStarted:
            if self.client.winner is None:
                await ctx.send('You must start a fight with ``;startfight <mention>`` before running this command')
            if self.client.winner.id == self.client.p1.user:
                await ctx.send('{} has won the fight with {} health remaining, better luck next time {}'.format(self.client.p1_Member.mention, self.client.p1.health, self.client.p2_Member.mention))
            if self.client.winner.id == self.client.p2.user:
                await ctx.send('{} has won the fight with {} health remaining, better luck next time {}'.format(self.client.p2_Member.mention, self.client.p2.health, self.client.p1_Member.mention))

    @commands.command()
    async def endfight(self, ctx):
        if ctx.author.guild_permissions.administrator:
            self.client.gameStarted = False
            await ctx.send('The active fight has been stopped')

async def setup(client):
    await client.add_cog(fightCommands(client))
