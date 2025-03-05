import discord.voice_client
from pytube import YouTube
from random import randint
from discord.ext import commands
from discord.utils import find, get
import urllib.request
import re
import json


class dnd(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.dmSpeaking = False

    @commands.command()
    async def dmspeaking(self, ctx):
        if ctx.author.id == 230442733234421760 and self.dmSpeaking == False:
            self.dmSpeaking = True
            for member in ctx.author.voice.channel.members:
                if member.id != 230442733234421760:
                    await member.edit(mute=True)
            await ctx.send('https://tenor.com/view/alastor-hazbin-hotel-gif-26763497')

        elif ctx.author.id == 230442733234421760 and self.dmSpeaking == True:
            self.dmSpeaking = False
            for member in ctx.author.voice.channel.members:
                if member.id != 230442733234421760:
                    await member.edit(mute=False)
            await ctx.send('https://tenor.com/view/hazbin-hotel-alastor-pfp-gif-1879653440911491019')

    @commands.command()
    async def roll(self, ctx, *, args=""):
        if not re.match(r"[^dD\d\s]", args) and len(args) < 1000:
            dicePattern = r"(\d[\d]?[\d]?[\d]?[\d]?[\d]?[dD]\d[\d]?[\d]?[\d]?[\d]?[\d]?)"
            multPattern = r"[dD]"
            string = re.split(dicePattern, args)
            rolls = ''

            ind = 0
            for f in string:
                number = 0
                if re.match(dicePattern, f):
                    a = re.split(multPattern, f)
                    try:  
                        a[0] = int(a[0])
                        a[1] = int(a[1])
                        for e in range(0, a[0]):
                            rand = randint(1, a[1])
                            number += rand
                            if len(rolls) < 500:
                                rolls += f"{rand} "
                        string[ind] = str(number)
                    except:
                        continue

                ind += 1
            equation = ''.join(string)
            try:
                total = eval(equation)
                if total < 240:
                    embed = discord.Embed(title=f'Request: {args}')
                else:
                    embed = discord.Embed(title=f'Request:')
                if len(rolls) < 500:
                    embed.add_field(name='Rolls:', value=f'{rolls}', inline=False)
                else:
                    embed.add_field(name='Rolls:', value=f'Not enough space on the table', inline=False)
                if len(rolls) < 500:
                    embed.add_field(name='Results:', value=f'{equation}', inline=False)
                else:
                    embed.add_field(name='Results:', value=f'See above', inline=False)
                embed.add_field(name="Total", value=f"{total}")
                await ctx.send(embed=embed)
            except:
                await ctx.send("https://tenor.com/view/nouns-nounish-nounsdao-abacus-counting-gif-16562575250327679873")
        else:
            await ctx.send("https://tenor.com/view/blocked-nope-do-not-stop-ksi-gif-13628205")
    


    
    
    class CoreBastion(discord.ui.View):
        # Thia

        # class ThiaBastion(discord.ui.View):
        #     @discord.ui.button(label="Garden")
        #     async def first_button_callback(self, interaction, button):
        #         embed = discord.Embed(title=f'Garden Information:')
        #         embed.add_field(name="General Information:", value="A Bastion can have more than one Garden. Each time you add a Garden to your Bastion, choose its type from the options in the Garden Types table. While in your Bastion, you can instruct the facility’s hireling to change the Garden from one type to another. This work takes 21 days, during which time no other activity can occur in this facility.", inline=False)
        #         embed.add_field(name="Harvest: Garden Growth.", value="When you issue the Harvest order to this facility, you commission the facility’s hireling to collect items from the Garden as noted in the Garden Types table. The work takes 5 days and costs no money.", inline=False)
        #         embed.add_field(name="Enlarging the Facility", value="You can enlarge your Garden to a Vast facility by spending 2,000 GP. A Vast Garden is equivalent to two Roomy Gardens and can include two of the same type of Garden or two different types. When you issue the Harvest order to a Vast Garden, each component garden produces its own harvest. A Vast Garden gains one additional hireling.", inline=False)
        #         embed.add_field(name="Garden Types", value="", inline=False)
        #         embed.add_field(name="Decorative", value="Aesthetically pleasing garden full of flowers and topiaries.   Harvest: Ten exquisite floral bouquets (worth 5 GP each), ten vials of Perfume, or ten Candles")
        #         embed.add_field(name="Food", value="Garden of delicious mushrooms or vegetables.   Harvest: 100 days worth of Rations")
        #         embed.add_field(name="Herb", value="Garden of rare herbs, some of which have medicinal uses.   Harvest: Herbs that are used to create either ten Healer’s Kits or one Potion of Healing")
        #         embed.add_field(name="Poison", value="Garden stocked with plants and fungi from which poisons and antitoxin can be extracted.  Harvest: Plants that are used to create either two vials of Antitoxin or one vial of Basic Poison")
        #         await interaction.response.send_message(embed=embed, ephemeral=True)

        #     @discord.ui.button(label="Laboratory")
        #     async def second_button_callback(self, interaction, button):
        #         embed = discord.Embed(title=f'Garden Information:')
        #         embed.add_field(name="Craft: Alchemist’s Supplies", value="The facility’s hireling crafts anything that can be made with Alchemist’s Supplies using the rules in the Player’s Handbook and chapter 7 of this book.", inline=False)
        #         embed.add_field(name="Craft: Poison", value=" You commission the facility’s hireling to craft a vial containing one application of a poison. The poison must be one of the following: Burnt Othur Fumes, Essence of Ether, or Torpor. This work takes 7 days, and you must pay half the poison’s cost. See “Poison” in chapter 3 for descriptions and costs of poisons.", inline=False)
        #         await interaction.response.send_message(embed=embed, ephemeral=True)
            
        #     @discord.ui.button(label="Unknown", disabled=True)
        #     async def third_button_callback(self, interaction, button):
        #         await interaction.response.send_message(embed=embed, ephemeral=True)
            
        #     @discord.ui.button(label="Unknown", disabled=True)
        #     async def fourth_button_callback(self, interaction, button):
                # await interaction.response.send_message(embed=embed, ephemeral=True)

        # Ausenic

        class AusenicBastion(discord.ui.View):
            @discord.ui.button(label="Training Area")
            async def first_button_callback(self, interaction, button):                
                embed = discord.Embed(title=f'Training Area Information:')
                embed.add_field(name="Empower: Training", value="When you issue the Empower order to this facility, the facility’s hirelings conduct training exercises for the next 7 days. Any character who trains here for at least 8 hours on each of those days gains a benefit at the end of the training period. The benefit depends on which trainer is present in the facility, as noted in the Expert Trainers table. The benefit lasts for 7 days.", inline=False)
                embed.add_field(name="Expert Trainers:", value="", inline=False)
                embed.add_field(name="Battle Expert", value="When you take damage from an attack made with an Unarmed Strike or a weapon, you can take a Reaction to reduce this damage by 1d4.")
                embed.add_field(name="Skills Expert", value="You gain proficiency in one of the following skills of your choice: Acrobatics, Athletics, Performance, Sleight of Hand, or Stealth.")
                embed.add_field(name="Tools Expert", value="You gain proficiency in one tool of your choice")
                embed.add_field(name="Unarmed Combat Expert", value="When you hit with your Unarmed Strike and deal damage, the attack deals an extra 1d4 Bludgeoning damage.")
                embed.add_field(name="Weapon Expert", value="Choose a kind of Simple or Martial weapon, such as Spear or Longbow. If you aren’t proficient with the weapon, you gain proficiency with it. If you already have proficiency with the weapon, you can use its mastery property.")
                await interaction.response.send_message(embed=embed, ephemeral=True)

            @discord.ui.button(label="Smithy")
            async def second_button_callback(self, interaction, button):
                embed = discord.Embed(title=f'Smithy Information:')
                embed.add_field(name="Craft: Smith’s Tools", value="The facility’s hirelings craft anything that can be made with Smith’s Tools, using the rules in the Player’s Handbook.", inline=False)
                embed.add_field(name="Craft: Magic Item (Armament)", value="If you are level 9+, can you commission the facility’s hirelings to craft a Common or an Uncommon magic item chosen by you from the Armaments tables in chapter 7. The facility has the tool required to craft the item, and the hirelings have proficiency with that tool as well as proficiency in the Arcana skill. See the “Crafting Magic Items” section in chapter 7 for the time and money that must be spent to craft the item. If the item allows its user to cast any spells from it, you must craft the item yourself (the facility’s hirelings can assist), and you must have all those spells prepared every day you spend crafting the item.", inline=False)
                embed.add_field(name="Crafting Costs:", value="(Halved when consumable)", inline=False)
                embed.add_field(name="Common", value="5 days/50 GP")
                embed.add_field(name="Uncommon", value="10 days/200 GP")
                embed.add_field(name="Rare", value="50 days/2,000 GP")
                embed.add_field(name="Very Rare", value="125 days/20,000 GP")
                embed.add_field(name="Legendary", value="250 days/100,000 GP")
                await interaction.response.send_message(embed=embed, ephemeral=True)
            
            @discord.ui.button(label="Library")
            async def third_button_callback(self, interaction, button):
                embed = discord.Embed(title=f'Library Information:')
                embed.add_field(name="Research: Topical Lore", value="When you issue the Research order to this facility, you commission the facility’s hireling to research a topic. The topic can be a legend, a known event or location, a person of significance, a type of creature, or a famous object. The work takes 7 days. When the research concludes, the hireling obtains up to three accurate pieces of information about the topic that were previously unknown to you and shares this knowledge with you the next time you speak with them. The DM determines what information you learn.")
                await interaction.response.send_message(embed=embed, ephemeral=True)
            
            @discord.ui.button(label="Arcane Study")
            async def fourth_button_callback(self, interaction, button):
                embed = discord.Embed(title=f'Arcane Study Information:')
                embed.add_field(name="Arcane Study Charm", value="After spending a Long Rest in your Bastion, you gain a magical Charm (see “Supernatural Gifts” in chapter 3) that lasts for 7 days or until you use it. The Charm allows you to cast Identify without expending a spell slot or using Material components. You can’t gain this Charm again while you still have it.", inline=False)
                embed.add_field(name="Craft: Arcane Focus", value="You commission the facility’s hireling to craft an Arcane Focus. The work takes 7 days and costs no money. The Arcane Focus remains in your Bastion until you claim it.", inline=False)
                embed.add_field(name="Craft: Book", value="You commission the facility’s hireling to craft a blank book. The work takes 7 days and costs you 10 GP. The book remains in your Bastion until you claim it.", inline=False)
                embed.add_field(name="Craft: Magic Item (Arcana)", value="If you are level 9+, you can commission the facility’s hireling to craft a Common or an Uncommon magic item chosen by you from the Arcana tables in chapter 7. The facility has the tool required to craft the item, and the hireling has proficiency with that tool as well as proficiency in the Arcana skill. See the “Crafting Magic Items” section in chapter 7 for the time and money that must be spent to craft the item. If the item allows its user to cast any spells from it, you must craft the item yourself (the facility’s hireling can assist), and you must have all those spells prepared every day you spend crafting the item.", inline=False)
                await interaction.response.send_message(embed=embed, ephemeral=True)

        # Ophelia

        class OpheliaBastion(discord.ui.View):
            @discord.ui.button(label="Greenhouse")
            async def first_button_callback(self, interaction, button):
                embed = discord.Embed(title=f'Greenhouse Information:')
                embed.add_field(name='Fruit of Restoration', value="One plant in your Greenhouse has three magical fruits growing on it. Any creature that eats one of these fruits gains the benefit of a Lesser Restoration spell. Fruits that aren’t eaten within 24 hours of being picked lose their magic. The plant replaces all picked fruits daily at dawn, and it can’t be transplanted without killing it.")
                embed.add_field(name='Harvest: Healing Herbs', value="You commission the facility’s hireling to create a Potion of Healing (greater) made from healing herbs. The work takes 7 days and costs no money.", inline=False)
                embed.add_field(name='Harvest: Poison', value="You commission the facility’s hireling to extract one application of a poison from rare plants or fungi. Choose the type of poison from the following options: Assassin’s Blood, Malice, Pale Tincture, or Truth Serum. See “Poison” in chapter 3 for each poison’s effect. Once harvested, the poison can be contained in a vial. The work takes 7 days and costs no money.", inline=False)
                await interaction.response.send_message(embed=embed, ephemeral=True)

            @discord.ui.button(label="Storehouse")
            async def second_button_callback(self, interaction, button):
                embed = discord.Embed(title=f'Storehouse Information:')
                embed.add_field(name='General Info', value="A Storehouse is a cool, dark space meant to contain trade goods objects from the Trade Goods table in chapter 7 and from chapter 6 of the Player's Handbook.", inline=False)
                embed.add_field(name='Trade: Goods', value="When you issue the Trade order to this facility, its hireling spends the next 7 days procuring nonmagical items that have a total value of 500  GP or less and stores them in the Storehouse, or the hireling uses those 7 days to sell goods in the Storehouse. You bear the total cost of any purchases, and the maximum value of the items purchased increases to 2,000 GP when you reach level 9 and 5,000 GP when you reach level 13. When you sell goods from your Storehouse, the buyer pays you 10 percent more than the standard price; this profit increases to 20 percent when you reach level 9, 50 percent when you reach level 13, and 100 percent when you reach level 17")
                await interaction.response.send_message(embed=embed, ephemeral=True)
            
            @discord.ui.button(label="Pub")
            async def third_button_callback(self, interaction, button):
                embed = discord.Embed(title=f'Pub Information:')
                embed.add_field(name="Research: Information Gathering", value="When you issue the Research order to this facility, you commission the Pub’s bartender to gather information from spies who are aware of all important events happening within 10 miles of your Bastion over the next 7 days. During that time, these spies can divulge the location of any creature that is familiar to you, provided the creature is within 50 miles of your Bastion and not hidden by magic or confined to a location that the DM deems is beyond the spy network’s ability to locate. If the spies learn the target’s location, they also learn where that creature has been for the previous 7 days.", inline=False)
                embed.add_field(name="Pub Special:", value="The Pub has one magical beverage on tap", inline=False)
                embed.add_field(name="Bigby's Burden", value="Drinking a pint of this beverage grants you the “enlarge” effect of an Enlarge/Reduce spell that has a duration of 24 hours (no saving throw allowed).")
                embed.add_field(name="Kiss of the Spider Queen", value="Drinking a pint of this beverage grants you the effect of a Spider Climb spell that has a duration of 24 hours.")
                embed.add_field(name="Moonlight Serenade", value="Drinking a pint of this beverage gives you Darkvision out to 60 feet for 24 hours. If you already have Darkvision, its range is extended by 60 feet for the same duration")
                embed.add_field(name="Positive Reinforcement", value="Drinking a pint of this beverage gives you Resistance to Necrotic damage for 24 hours.")
                embed.add_field(name="Sterner Stuff", value="""For 24 hours after drinking a pint of this beverage, you automatically succeed on saving throws to avoid or end the Frightened condition.
At the start of a Bastion turn, you can switch to one of the other options. Your DM may create new options. A pint of this magical beverage loses its magic 24 hours after it’s poured.""")
                embed.add_field(name="Enlarging the Facility", value="You can enlarge your Pub to a Vast facility by spending 2,000 GP. If you do so, the Pub can have two magical beverages from the Pub Special list on tap at a time. A Vast Pub gains three additional hirelings, for a total of four. These new hirelings are servers. Assign names and personalities to them as you see fit.", inline=False)
                await interaction.response.send_message(embed=embed, ephemeral=True)
            
            @discord.ui.button(label="Trophy Room")
            async def fourth_button_callback(self, interaction, button):
                embed = discord.Embed(title=f'Trophy Room Information:')
                embed.add_field(name='Research: Lore', value="You commission the facility’s hireling to research a topic of your choice. The topic can be a legend, any kind of creature, or a famous object. The topic need not be directly related to items on display in the room, as the trophies provide clues to research a wide variety of other subjects. The work takes 7 days. When the research concludes, the hireling obtains up to three accurate pieces of information about the topic that were previously unknown to you and shares this knowledge with you the next time you speak with them. The DM determines what information is learned.", inline=False)
                embed.add_field(name='Research: Trinket Trophy', value="You commission the facility’s hireling to search for a trinket that might be of use to you. The work takes 7 days. When the research concludes, roll any die. If the number rolled is odd, the hireling finds nothing useful. If the number rolled is even, the hireling finds a magic item. Roll on the Implements—Common table in chapter 7 to determine what it is.", inline=False)
                await interaction.response.send_message(embed=embed, ephemeral=True)
        
        # # Nadine

        # class NadineBastion(discord.ui.View):
        #     @discord.ui.button(label="Archive")
        #     async def first_button_callback(self, interaction, button):
        #         embed = discord.Embed(title=f'Archive Information:')
        #         embed.add_field(name='Research: Helpful Lore', value="When you issue the Research order to this facility, you commission the facility’s hireling to search the Archive for helpful lore. The work takes 7 days. The hireling gains knowledge as if they had cast the Legend Lore spell, then shares this knowledge with you the next time you speak with them.", inline=False)
        #         embed.add_field(name="Reference Book", value="Your Archive contains one copy of a rare and valuable reference book, which gives you a benefit while you and the book are in your Bastion. You can choose one of the following options (your DM might make more options available):", inline=False)
        #         embed.add_field(name="The Old Faith and Other Religions", value="You have Advantage on any Intelligence (Religion) check you make when you take the Study action to recall lore about deities, rites and prayers, hierarchies, holy symbols, and the practices of secret cults.", inline=False)
        #         embed.add_field(name="Enlarging the Facility", value="You can enlarge your Archive to a Vast facility by spending 2,000 GP. If you do so, you gain two additional reference books chosen from the list above.", inline=False)
        #         await interaction.response.send_message(embed=embed, ephemeral=True)

        #     @discord.ui.button(label="Library")
        #     async def second_button_callback(self, interaction, button):
        #         embed = discord.Embed(title=f'Library Information:')
        #         embed.add_field(name="Research: Topical Lore", value="When you issue the Research order to this facility, you commission the facility’s hireling to research a topic. The topic can be a legend, a known event or location, a person of significance, a type of creature, or a famous object. The work takes 7 days. When the research concludes, the hireling obtains up to three accurate pieces of information about the topic that were previously unknown to you and shares this knowledge with you the next time you speak with them. The DM determines what information you learn.")
        #         await interaction.response.send_message(embed=embed, ephemeral=True)
            
        #     @discord.ui.button(label="Sacristy")
        #     async def second_button_callback(self, interaction, button):
        #         embed = discord.Embed(title=f'Sacristy Information:')
        #         embed.add_field(name="Craft: Holy Water", value="You commission the facility’s hireling to craft a flask of Holy Water. The work takes 7 days and costs no money. You can spend GP during the creation process to increase the potency of the Holy Water. For every 100 GP you spend, up to a maximum of 500 GP, the damage dealt by the Holy Water increases by 1d8.", inline=False)
        #         embed.add_field(name="Craft: Magic Item (Relic)", value="You commission the facility’s hireling to craft a Common or an Uncommon magic item chosen by you from the Relics tables in chapter 7. The facility has the tool required to craft the item, and the hireling has proficiency with that tool as well as proficiency in the Arcana skill. See the “Crafting Magic Items” section in chapter 7 for the time and money that must be spent to craft the item. If the item allows its user to cast any spells from it, you must craft the item yourself (the facility’s hireling can assist), and you must have all those spells prepared every day you spend crafting the item.", inline=False)
        #         embed.add_field(name="Spell Refreshment", value="Having a Sacristy allows you to regain one expended spell slot of level 5 or lower after spending an entire Short Rest in your Bastion. You can’t gain this benefit again until you finish a Long Rest.", inline=False)
        #         await interaction.response.send_message(embed=embed, ephemeral=True)
            
        #     @discord.ui.button(label="Training Area")
        #     async def fourth_button_callback(self, interaction, button):
                embed = discord.Embed(title=f'Training Area Information:')
                embed.add_field(name="Empower: Training", value="When you issue the Empower order to this facility, the facility’s hirelings conduct training exercises for the next 7 days. Any character who trains here for at least 8 hours on each of those days gains a benefit at the end of the training period. The benefit depends on which trainer is present in the facility, as noted in the Expert Trainers table. The benefit lasts for 7 days.", inline=False)
                embed.add_field(name="Expert Trainers:", value="", inline=False)
                embed.add_field(name="Battle Expert", value="When you take damage from an attack made with an Unarmed Strike or a weapon, you can take a Reaction to reduce this damage by 1d4.")
                embed.add_field(name="Skills Expert", value="You gain proficiency in one of the following skills of your choice: Acrobatics, Athletics, Performance, Sleight of Hand, or Stealth.")
                embed.add_field(name="Tools Expert", value="You gain proficiency in one tool of your choice")
                embed.add_field(name="Unarmed Combat Expert", value="When you hit with your Unarmed Strike and deal damage, the attack deals an extra 1d4 Bludgeoning damage.")
                embed.add_field(name="Weapon Expert", value="Choose a kind of Simple or Martial weapon, such as Spear or Longbow. If you aren’t proficient with the weapon, you gain proficiency with it. If you already have proficiency with the weapon, you can use its mastery property.")
                await interaction.response.send_message(embed=embed, ephemeral=True)

        # Atarum

        class AtarumBastion(discord.ui.View):
            @discord.ui.button(label="Gambling")
            async def first_button_callback(self, interaction, button):
                embed = discord.Embed(title=f'Storehouse Information:')
                embed.add_field(name='Trade: Gambling Hall', value="When you issue the Trade order to this facility, the facility’s hirelings turn the Gaming Hall into a gambling den for 7 days. At the end of the seventh day, roll 1d100 and consult the following table to determine your portion of the house’s winnings.", inline=False)
                embed.add_field(name='01–50', value="1d6 × 10 GP")
                embed.add_field(name='51-85', value="2d6 × 10 GP")
                embed.add_field(name='86-95', value="4d6 × 10 GP")
                embed.add_field(name='96-100', value="10d6 × 10 GP")
                await interaction.response.send_message(embed=embed, ephemeral=True)

            @discord.ui.button(label="Library")
            async def second_button_callback(self, interaction, button):
                embed = discord.Embed(title=f'Library Information:')
                embed.add_field(name="Research: Topical Lore", value="When you issue the Research order to this facility, you commission the facility’s hireling to research a topic. The topic can be a legend, a known event or location, a person of significance, a type of creature, or a famous object. The work takes 7 days. When the research concludes, the hireling obtains up to three accurate pieces of information about the topic that were previously unknown to you and shares this knowledge with you the next time you speak with them. The DM determines what information you learn.")
                await interaction.response.send_message(embed=embed, ephemeral=True)
            
            # @discord.ui.button(label="Unknown", disabled=True)
            # async def third_button_callback(self, interaction, button):
            #     await interaction.response.send_message(embed=embed, ephemeral=True)
            
            # @discord.ui.button(label="Unknown", disabled=True)
            # async def fourth_button_callback(self, interaction, button):
            #     await interaction.response.send_message(embed=embed, ephemeral=True)




        ## Main
        # @discord.ui.button(label="Thia", style=discord.ButtonStyle.success)
        # async def first_button_callback(self, interaction, button):
        #     embed = discord.Embed(title=f'Bastion Information:')
        #     file = discord.File("./Images/ThiaBastion.webp", filename="ThiaBastion.webp")
        #     embed.set_image(url="attachment://ThiaBastion.webp")
        #     await interaction.response.send_message(embed=embed, file=file, view=self.ThiaBastion(), ephemeral=True)

        @discord.ui.button(label="Ausenic", style=discord.ButtonStyle.primary)
        async def second_button_callback(self, interaction, button):
            embed = discord.Embed(title=f'Bastion Information:')
            file = discord.File("./Images/AusenicBastion.jpg", filename="AusenicBastion.jpg")
            embed.set_image(url="attachment://AusenicBastion.jpg")
            await interaction.response.send_message(embed=embed, file=file, view=self.AusenicBastion(), ephemeral=True)
        
        @discord.ui.button(label="Ophelia", style=discord.ButtonStyle.danger)
        async def third_button_callback(self, interaction, button):
            embed = discord.Embed(title=f'Bastion Information:')
            file = discord.File("./Images/OpheliaBastion.webp", filename="OpheliaBastion.webp")
            embed.set_image(url="attachment://OpheliaBastion.webp")
            await interaction.response.send_message(embed=embed, file=file, view=self.OpheliaBastion(), ephemeral=True)
        
        @discord.ui.button(label="Atarum", style=discord.ButtonStyle.secondary)
        async def fourth_button_callback(self, interaction, button):
            embed = discord.Embed(title=f'Bastion Information:')
            file = discord.File("./Images/AtarumBastion.webp", filename="AtarumBastion.webp")
            embed.set_image(url="attachment://AtarumBastion.webp")
            await interaction.response.send_message(embed=embed, file=file, view=self.AtarumBastion(), ephemeral=True)

    

    @commands.command()
    async def bastion(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(title=f'Bastion Information:')
        file = discord.File("./Images/Bastion.webp", filename="Bastion.webp")
        embed.set_image(url="attachment://Bastion.webp")
        await ctx.send(file=file, embed=embed, view=self.CoreBastion(), ephemeral=True)

    @commands.command()
    async def foundry(self, ctx):
        external_ip = urllib.request.urlopen('https://api.ipify.org?format=json').read().decode('utf8')
        json_decoded = json.loads(external_ip)

        foundry_ip = 'http://' + json_decoded['ip'] + ':30000/'
        embed = discord.Embed(title=f'Foundry IP:')
        embed.add_field(name='', value=foundry_ip, inline=False)

        await ctx.send(embed=embed)
        


async def setup(client):
    await client.add_cog(dnd(client))