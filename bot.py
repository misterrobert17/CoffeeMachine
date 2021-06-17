import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='c!')

@bot.event
async def on_ready():
    print(">> Coffee Machine starts working! <<")

bot.run('ODU0OTEyMzA5NTU4MjQ3NDU0.YMq1Ig.kH2eDvDHm_JMyeX2gCMNyFmrE7Y')