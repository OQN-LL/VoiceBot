import discord
from discord.ext import commands

with open("accessToken.txt","r") as f:
    token = f.read()[:-1]

bot = commands.Bot(command_prefix=commands.when_mentioned_or('/'))

@bot.event
async def on_ready():
    print("-"*40)
    print("login:",bot.user.name)
    print("ID:",bot.user.id)
    print("-"*40)

@commands.command(pass_context=True, no_pm=True)
async def summon(ctx):
    summoned_channel = ctx.message.author.voice_channel
    if summoned_channel is None:
        await bot.say('You are not in a voice channel.')
        return False

    state = get_voice_state(ctx.message.server)
    if state.voice is None:
        state.voice = await bot.join_voice_channel(summoned_channel)
    else:
        await state.voice.move_to(summoned_channel)
    return True

#@bot.event
#async def on_message(message):
#    if bot.user != message.author:
#        await bot.send_message(message.channel, "1145148101919")











bot.run(token)
