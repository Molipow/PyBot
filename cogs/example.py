import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Example module loaded')

    @commands.command()
    async def riddle1(self, ctx):
        await ctx.send(file=discord.File(fp="1.png" \
        # , filename="1.png" \
        ))

def setup(client):
    client.add_cog(Example(client))