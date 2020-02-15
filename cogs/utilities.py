import discord
import random
import math
import time
import json
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
    @commands.has_permissions(manage_messages = True)
    async def czyść(self, ctx, amount = 5):
        await ctx.channel.purge(limit = amount+1)
        
    @commands.command()
    async def pomoc(self, ctx, command_for_help = None):
        if command_for_help == None:
            await ctx.send("```Komendy:\n  czyść\n  ping\n  pong\n  pomoc\n  remindme\n  rzuć\n  operator\n  syntax\nNapisz `!py pomoc [komenda]` aby dostać dokładniejsze informacje.```")
        elif command_for_help == "czyść":
            await ctx.send("```Komenda czyść\n  czyść <liczba>\nCzyści n(domyślnie 5) wiadomości z czatu.```")
        elif command_for_help == "ping":
            await ctx.send("```Komenda ping\n  ping\nPong!```")
        elif command_for_help == "pong":
            await ctx.send("```Komenda pong\n  pong\nPing!```")
        elif command_for_help == "pomoc":
            await ctx.send("```Komenda pomoc\n  pomoc\nWyświetla listę komend.```")
        elif command_for_help == "remindme":
            await ctx.send("```Komenda remindme\n  remindme [czas] [wiadomość] <kanał>\nUstawia przypomnienie wraz z wiadomością. Jeśli wiadomość zawiera więcej niż jedno słowo, nalezy ją umieścić w cudzysłowie. Jeśli kanał nie zostanie wybrany, przypomnienie zostanie wysłane na kanale z którego została wykonana komenda.```")
        elif command_for_help == "rzuć":
            await ctx.send("```Komenda rzuć\n  rzuć [liczba]\nRzuca kostką n-ścienną.```")
        elif command_for_help == "operator":
            await ctx.send("```Komenda operator\n  operator [operator]\nWyświetla krótki opis operatora. !py operator aby wyświetlić listę operatorów```")
        elif command_for_help == "syntax":
            await ctx.send("```Komenda syntax\n  syntax [wyrażenie]\nWyświetla krótki opis wyrażenia. !py syntax aby wyświetlić listę wyrażeń```")
        else:
            await ctx.send("```Nie znaleziono komendy.```")

    @commands.command()
    async def github(self, ctx):
        await ctx.send("https://github.com/Molipow/PyBot")

    @commands.command()
    async def remindme(self, ctx, remind_time, message, channel = None):
        unit = remind_time[-1:]
        time_to_add_raw = int(remind_time[:-1])
        if unit == 's' or unit == 'S':
            time_to_add = time_to_add_raw
        elif unit == 'm' or unit == 'M':
            time_to_add = time_to_add_raw * 60
        elif unit == 'h' or unit == 'H':
            time_to_add = time_to_add_raw * 60 * 60
        elif unit == 'd' or unit == 'D':
            time_to_add = time_to_add_raw * 60 * 60 * 24
        else:
            time_to_add = time_to_add_raw
            
        remind_date = time.time() + time_to_add

        with open("remind.json", "r") as f:
            reminds = json.load(f)

        if channel == None:
            channel = ctx.channel
        else:
            channel = channel[2:]
            channel = channel[:-1]
            channel = self.client.get_channel(int(channel))
            
        reminds[str(remind_date)] = message, str(channel.id), str(ctx.author.id)

        with open("remind.json", "w") as f:
            json.dump(reminds, f, indent=4)

        await ctx.send(f"Przypomne za {remind_time} na kanale {channel.mention}. Wiadomość: {message}")
    
def setup(client):
    client.add_cog(Utilities(client))