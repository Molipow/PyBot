import discord
from discord.ext import commands

class Voice(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Voice module loaded')

    @commands.command() 
    async def join(self, ctx):    
        channel = ctx.author.voice.channel
        self.vc_connection = await channel.connect()

    @commands.command()
    async def play(self, ctx, song_name):
        is_connected = False
        song = discord.FFmpegPCMAudio(executable = "D:\\Program Files\\ffmpeg-20200216-8578433-win64-static\\bin\\ffmpeg.exe", source = f"voice/{song_name.lower()}.mp3")
        for connection in self.client.voice_clients:
            if connection.channel.id == ctx.author.voice.channel.id:
                connection.play(song)
                is_connected = True
        if not is_connected:
            vc_connection = await ctx.author.voice.channel.connect()
            vc_connection.play(song)

    @commands.command()
    async def stop(self, ctx):
        for connection in self.client.voice_clients:
            if connection.channel.id == ctx.author.voice.channel.id:
                connection.stop()

    @commands.command()
    async def leave(self, ctx):
        for connection in self.client.voice_clients:
            if connection.channel.id == ctx.author.voice.channel.id:
                await connection.disconnect()

def setup(client):
    client.add_cog(Voice(client))