from discord.ext import commands

class lb(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def lbpurge(self, ctx):
        if ctx.author.guild_permissions.administrator:
            guild = self.client.get_guild(761652116375994448)
            user = guild.get_member(747838795704959027)
            with open('./TextLogs/BotLog.txt', 'w') as file:
                file.write('Not Suspicious#7966\n')
                file.close()
            with open('./TextLogs/ActivityLog.txt', 'w') as file:
                file.write('{}\n'.format(ctx.author))
                file.close()
            await ctx.send('Both motwlb and the bot log has been cleared')

    @commands.command(pass_context=True, aliases=['motwlb'])
    async def MOTWLB(self, ctx):
        if ctx.guild.id == 761652116375994448:
            f = open('./TextLogs/ActivityLog.txt', 'r')
            d = dict()
            lb = []
            for line in f:
                line = line.strip()
                if line in d:
                    d[line] = d[line] + 1
                else:
                    d[line] = 1
            sorted_dict = {}
            sorted_keys = sorted(d, key=d.get)

            for w in sorted_keys:
                sorted_dict[w] = d[w]
            await ctx.send('''Member Of the Week Activity Leaderboard:
    **Member   :   Messages this week**''')
            limit = len(sorted_keys)
            for key in reversed(sorted_dict.keys()):
                lb.append('{}  :  {}'.format(key, d[key]))
            lb = ('\n'.join(lb))
            await ctx.send(lb)

    @commands.command()
    async def botlog(self, ctx):
        f = open('./TextLogs/BotLog.txt', 'r')
        d = dict()
        for line in f:
            line = line.strip()
            if line in d:
                d[line] = d[line] + 1
            else:
                d[line] = 1
        for key in list(d.keys()):
            await ctx.send('{}  :  {}'.format(key, d[key]))

def setup(client):
    client.add_cog(lb(client))
