import discord
from discord.ext import commands
import youtube_dl

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, url: str):
        if ctx.author.voice is None:
            await ctx.send("Bạn cần tham gia voice channel trước!")
            return
        channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await channel.connect()
        voice_client = ctx.voice_client
        with youtube_dl.YoutubeDL({'format': 'bestaudio'}) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2)
        voice_client.stop()
        voice_client.play(source)
        await ctx.send(f"Đang phát: {info['title']}")

def setup(bot):
    bot.add_cog(Music(bot))
