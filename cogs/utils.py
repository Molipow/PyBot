import discord
import random
import math
from discord.ext import commands

class Utilities(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Utilities module loaded')

    @commands.command()
    async def pong(self, ctx):
        await ctx.send("Ping.")

    @commands.command()
    async def ping(self, ctx):
        responses = [
            "Pong.",
            "Pong!",
            "Pong?"
        ]
        await ctx.send(responses[random.randint(0, 2)])
        
    @commands.command()
    async def rzuć(self, ctx, max_roll):
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
        

    @commands.command()
    async def czyść(self, ctx, amount = 5):
        await ctx.channel.purge(limit = amount+1)
        
    @commands.command()
    async def pomoc(self, ctx, command_for_help = None):
        if command_for_help == None:
            await ctx.send("```Komendy:\n  czyść\n  ping\n  pong\n  pomoc\n  rzuć\n  syntax\nNapisz `!py pomoc [komenda]` aby dostać dokładniejsze informacje.```")
        elif command_for_help == "czyść":
            await ctx.send("```Komenda czyść\n  czyść [liczba, domyślnie 5]\nCzyści n wiadomości z czatu.```")
        elif command_for_help == "ping":
            await ctx.send("```Komenda ping\n  ping\nPong!```")
        elif command_for_help == "pong":
            await ctx.send("```Komenda pong\n  pong\nPing!```")
        elif command_for_help == "pomoc":
            await ctx.send("```Komenda pomoc\n  pomoc\nWyświetla listę komend.```")
        elif command_for_help == "rzuć":
            await ctx.send("```Komenda rzuć\n  rzuć [liczba]\nRzuca kostką n-ścienną.```")
        elif command_for_help == "syntax":
            await ctx.send("```Komenda syntax\n  syntax [wyrażenie]\nWyświetla krótki opis wyrażenia. !py syntax aby wyświetlić listę wyrażeń```")
        else:
            await ctx.send("```Nie znaleziono komendy.```")



def setup(client):
    client.add_cog(Utilities(client))