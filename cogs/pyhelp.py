import discord
from discord.ext import commands

class PyHelp(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('PyHelp module loaded')

    @commands.command()
    async def syntax(self, ctx, keyword = None):
        if keyword == None:
            await ctx.send("```!py syntax [wyrażenie]\nDostępne wyrażenia:\nif\nelif\nelse```")
        elif keyword == "if":
            await ctx.send("```py\nif warunek:\n    kod```\n`if - Służy do tworzenia instrukcji warunkowych.`\nPrzykład:\n```py\nif 2>1:\n    print('prawda')\nprint('poza ifem')``` ```WAŻNE! Przy porównywaniu wartości należy użyć '==' a nie '='.```")
        elif keyword == "elif":
            await ctx.send("```py\nif warunek:\n    kod\nelif inny_warunek:\n    inny_kod```\n`elif - Jeśli poprzedni warunek okazał się fałszywy, sprawdzamy inny. Jeśli jednak byl prawdziwy, pomijamy sprawdzanie tych.`\nPrzykłady:\n```py\nif False:\n    print('Tej wiadomości nie zobaczymy')\nelif True:\n    print('Tą wiadomość zobaczymy!')```\n```py\nif True:\n    print('Tą zobaczymy')\nelif True:\n    print('A tej nie')```\n```py\nif False:\n    print('Tej nie zobaczymy')\nelif False:\n    print('Tej też nie')```")
        elif keyword == "else":
            await ctx.send("```py\nif warunek:\n    kod\nelse:\n    inny_kod```\n`else - Jeśli poprzednie warunki są fałszywe, wykonujemy ten blok`\nPrzykład:\n```py\nif False:\n    print('To się nie wykona')\nelse:\n    print('To już tak')```\n```py\nif True:\n    print('To się wykona')\nelse:\n    print('To już nie')```")

def setup(client):
    client.add_cog(PyHelp(client))