import discord

with open("accessToken.txt","r") as f:
    token = f.read()[:-1]

bot = discord.Client()

@bot.event
async def on_ready():
    print("-"*40)
    print("login:",bot.user.name)
    print("ID:",bot.user.id)
    print("-"*40)











bot.run(token)
