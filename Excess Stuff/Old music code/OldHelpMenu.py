@client.command()
async def help(cxt):
    await cxt.send('''
Here is the current list of commands:
(I would suggest sticking to the bot channel of your respective server, but what do I know I'm just a bot)

__**Basic Commands:**__
;suggest [your suggestion] - Helps me with development of the bot and make your ideas known for future additions
;MOTWLB - View the current leader board for the activity based component of the MOTW selection
(Spammed messages, and tts will not be counted. However in the case of tts time in vc will still be counted by moderators)


;feeling - Run this command to find how the bot is feeling
;gif - (in dev and currently disabled) Supplies random gif
;quote - (in dev) Responds with a random quote


__**Administrator Commands:**__
__(Must have the Administrator permission to run):__
;purge [number] - Deletes messages in current channel between 1 and 100\nOnly available to those with the Administrator permission
;kick [member]
;ban [member]
;mute [member]
;unmute [member]
    ''')
