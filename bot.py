import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Load all cogs in modules folder
def load_cogs():
    for filename in os.listdir('./modules'):
        if filename.endswith('.py'):
            bot.load_extension(f'modules.{filename[:-3]}')

@bot.event
async def on_ready():
    print(f'Bot đã đăng nhập với tên: {bot.user}')

if __name__ == '__main__':
    load_cogs()
    bot.run('YOUR_BOT_TOKEN_HERE')
