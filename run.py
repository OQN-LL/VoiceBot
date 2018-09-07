import discord
from discord.ext import commands

with open("accessToken.txt","r") as f:
    token = f.read()[:-1]



@bot.event
async def on_ready():
    print("-"*40)
    print("login:",bot.user.name)
    print("ID:",bot.user.id)
    print("-"*40)


#@bot.event
#async def on_message(message):
#    if bot.user != message.author:
#        await bot.send_message(message.channel, "1145148101919")











bot.run(token)
