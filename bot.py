import discord
from discord.ext import commands
import random
import math

# https://discordapp.com/oauth2/authorize?client_id=677895248088662025&permissions=8&scope=bot              Add bot with Admin permission
# https://discordapp.com/api/oauth2/authorize?client_id=677895248088662025&permissions=518208&scope=bot     Add bot with Non-admin permissions

client = commands.Bot(command_prefix = '!p ')

@client.event
async def on_ready():
    print("Bot working")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("!p pomoc"))

@client.event
async def on_member_join(member):
    print(f'{member} dołączył')

@client.event
async def on_member_remove(member):
    print(f'{member} wyszedł')

@client.command()
async def ping(ctx):
    responses = [
        "Pong.",
        "Pong!",
        "Pong?"
    ]
    await ctx.send(responses[random.randint(0, 2)])

@client.command()
async def rzuć(ctx, max_roll):
    try:
        max_roll = int(max_roll)
    except ValueError:
        await ctx.send("```To nie jest liczba.```")
        return
    result = random.randint(1, max_roll)
    response = ""
    if result <= math.floor(max_roll/3):
        response = "Słabo."
    elif math.floor(max_roll / 3) < result <= math.ceil(max_roll / 3 * 2):
        response = "Całkiem nieźle."
    else:
        response = "Spoko jest."

    await ctx.send(f"```Wyrzuciłeś {result}. {response}```")

@client.command()
async def trigger(ctx):
    await ctx.send("//ping")

@client.command()
async def self_trigger(ctx):
    await ctx.send("!p self_trigger")

@client.command()
async def czyść(ctx, amount = 5):
    await ctx.channel.purge(limit = amount+1)

@client.command()
async def syntax(ctx, keyword = None):
    if keyword == None:
        await ctx.send("```!p syntax [wyrażenie]\nDostępne wyrażenia:\nif\nelif\nelse```")
    elif keyword == "if":
        await ctx.send("```py\nif warunek:\n    kod```\n`if - Służy do tworzenia instrukcji warunkowych.`\nPrzykład:\n```py\nif 2>1:\n    print('prawda')\nprint('poza ifem')``` ```WAŻNE! Przy porównywaniu wartości należy użyć '==' a nie '='.```")
    elif keyword == "elif":
        await ctx.send("```py\nif warunek:\n    kod\nelif inny_warunek:\n    inny_kod```\n`elif - Jeśli poprzedni warunek okazał się fałszywy, sprawdzamy inny. Jeśli jednak byl prawdziwy, pomijamy sprawdzanie tych.`\nPrzykłady:\n```py\nif False:\n    print('Tej wiadomości nie zobaczymy')\nelif True:\n    print('Tą wiadomość zobaczymy!')```\n```py\nif True:\n    print('Tą zobaczymy')\nelif True:\n    print('A tej nie')```\n```py\nif False:\n    print('Tej nie zobaczymy')\nelif False:\n    print('Tej też nie')```")
    elif keyword == "else":
        await ctx.send("```py\nif warunek:\n    kod\nelse:\n    inny_kod```\n`else - Jeśli poprzednie warunki są fałszywe, wykonujemy ten blok`\nPrzykład:\n```py\nif False:\n    print('To się nie wykona')\nelse:\n    print('To już tak')```\n```py\nif True:\n    print('To się wykona')\nelse:\n    print('To już nie')```")
    

@client.command()
async def pomoc(ctx, command_for_help = None):
    if command_for_help == None:
        await ctx.send("```Komendy:\n  czyść\n  ping\n  pomoc\n  rzuć\n  syntax\nNapisz `!p pomoc [komenda]` aby dostać dokładniejsze informacje.```")
    elif command_for_help == "czyść":
        await ctx.send("```Komenda czyść\n  czyść [liczba, domyślnie 5]\nCzyści n wiadomości z czatu.```")
    elif command_for_help == "ping":
        await ctx.send("```Komenda ping\n  ping\nPong!```")
    elif command_for_help == "pomoc":
        await ctx.send("```Komenda pomoc\n  pomoc\nWyświetla listę komend.```")
    elif command_for_help == "rzuć":
        await ctx.send("```Komenda rzuć\n  rzuć [liczba]\nRzuca kostką n-ścienną.```")
    elif command_for_help == "syntax":
        await ctx.send("```Komenda syntax\n  syntax [wyrażenie]\nWyświetla krótki opis wyrażenia. !p syntax aby wyświetlić listę wyrażeń```")
    else:
        await ctx.send("```Nie znaleziono komendy.```")

client.run('')