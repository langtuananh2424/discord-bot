import discord
from discord.ext import commands

class Echo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx, *, message: str):
        """Nhắc lại nội dung người dùng gửi."""
        await ctx.send(message)

def setup(bot):
    bot.add_cog(Echo(bot))
