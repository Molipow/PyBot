import discord
import random
import math
import os
from discord.ext import commands

# https://discordapp.com/oauth2/authorize?client_id=677895248088662025&permissions=8&scope=bot              Add bot with Admin permission
# https://discordapp.com/api/oauth2/authorize?client_id=677895248088662025&permissions=518208&scope=bot     Add bot with Non-admin permissions

client = commands.Bot(command_prefix = '!py ')

@client.event
async def on_ready():
    print("Bot working")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("!py pomoc"))

@client.event
async def on_member_join(member):
    print(f'{member} dołączył')

@client.event
async def on_member_remove(member):
    print(f'{member} wyszedł')

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Załadowano moduł {extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Rozładowano moduł {extension}")

@client.command()
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