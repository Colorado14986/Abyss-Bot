import discord.voice_client
from random import randint
from discord.ext import commands

class fightCommandstester(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.p1 = None
        self.client.p1_Member = None
        self.client.p2 = None
        self.client.p2_Member = None
        self.client.gameStarted = False
        self.client.winner = None
        self.client.gameTurn = None
        self.client.perp = None
        self.client.target = None
        def hpcheck(self):
            if self.client.p1.health < 0:
                self.client.winner = self.client.p2_Member
                self.client.gameStarted = False

            if self.client.p2.health < 0:
                self.client.winner = self.client.p1_Member
                self.client.gameStarted = False
        def playerCheck(self, ctx):
            if ctx.author.id == self.client.p1.id:
                self.client.perp = self.client.p1
                self.client.target = self.client.p2
            if ctx.author.id == self.client.p2.id:
                self.client.perp = self.client.p2
                self.client.target = self.client.p1
    
    @commands.command(pass_context=True)
    async def ftest(self, ctx, choice):
        self.client.playerCheck()

        if choice == 'attack':
            self.client.gameTurn = self.client.target.id
            damage = randint(0, self.client.perp)
            truedamage = damage - self.client.target.defense
            if truedamage > 0 and damage != self.client.perp.max_attack:
                self.client.target.health = self.client.target.health - truedamage
            if damage == self.client.p2.max_attack:
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
            if damage == self.client.p1.max_attack:
                await ctx.send('''You dealt a critical blow of {} dealing full damage and bypassing {}'s defences leaving them with {} health
    {} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(damage, self.client.p2_Member.mention, self.client.p2.health, self.client.p2_Member.mention))

            hpcheck()
        
        if ctx.author.id == self.client.p2_Member.id:
            self.client.gameTurn = self.client.p1_Member.id
            damage = randint(0, self.client.p2.max_attack)
            truedamage = damage - self.client.p1.defense
            if self.client.p1.defense > 0 and damage != self.client.p2.max_attack:
                if truedamage > 0:
                    await ctx.send('''You attempted to land a hit of {}, but after {} defended you only dealt {} leaving them with {} health
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(damage, self.client.p1_Member.mention, truedamage, self.client.p1.health, self.client.p1_Member.mention))
                if truedamage <= 0:
                    await ctx.send('''You tried to attack but were blocked with ease by {}
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(self.client.p1_Member.mention, self.client.p1_Member.mention))
            if self.client.p2.defense == 0 and truedamage > 0:
                await ctx.send('''You dealt a perfect hit of {} as {} has no defense leaving them with {} health
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(damage,
                                                                                                self.client.p1_Member.mention,
                                                                                                self.client.p1.health,
                                                                                                self.client.p1_Member.mention))
            if damage == self.client.p2.max_attack:
                await ctx.send('''You dealt a critical blow of {} dealing full damage and bypassing {}'s defences leaving them with {} health
{} it is now your turn, please run ``;move`` along with either attack, train or fortify'''.format(damage, self.client.p1_Member.mention, self.client.p1.health, self.client.p1_Member.mention))
            
            hpcheck()
    
    
def setup(client):
    client.add_cog(fightCommandstester(client))