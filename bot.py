import discord
import os
import json
import time
from discord.ext import commands, tasks

# https://discordapp.com/oauth2/authorize?client_id=677895248088662025&permissions=8&scope=bot              Add bot with Admin permission
# https://discordapp.com/api/oauth2/authorize?client_id=677895248088662025&permissions=518208&scope=bot     Add bot with Non-admin permissions

client = commands.Bot(command_prefix = '!py ')

@client.event
async def on_ready():
    check_reminds.start()
    print("Bot working")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("!py pomoc"))

@client.event
async def on_member_join(member):
    print(f'{member} dołączył')

@client.event
async def on_member_remove(member):
    print(f'{member} wyszedł')

@client.command(aliases=["reset","restart", "reboot"])
@commands.has_permissions(administrator = True)
async  def _reset(ctx):
    await ctx.send("Restartowanie bota")
    await client.close()
    os.system("cls")
    os.system("echo Bot restarting")
    os.system("python bot.py")

@tasks.loop(seconds = 1)
async def check_reminds():
    to_pop=[]
    with open('remind.json', 'r') as f:
        reminds = json.load(f)
    for item in reminds:
        if float(item) <= float(time.time()):
            channel = client.get_channel(int(reminds[item][1]))
            author = client.get_user(int(reminds[item][2]))
            message = str(reminds[item][0])
            to_pop.append(item)
            await channel.send(f"RemindMe! przez {author.mention}. Wiadomość: {message}")
    for i in to_pop:
        reminds.pop(i)
    with open('remind.json', 'w') as f:
        json.dump(reminds, f, indent=4)

@check_reminds.after_loop
async def check_reminds_restart():
    print('done!')
    print(check_reminds.failed())
    check_reminds.restart()

@client.command()
@commands.has_permissions(administrator = True)
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Włączono moduł {extension}")

@client.command()
@commands.has_permissions(administrator = True)
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Wyłączono moduł {extension}")

@client.command()
@commands.has_permissions(administrator = True)
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Przeładowano moduł {extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")

file = open("D:/PROGRAMOWANIE/Python/token.txt") # change to your token file
token = file.readline()
file.close()
client.run(token)