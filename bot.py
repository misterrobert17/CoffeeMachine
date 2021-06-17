import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='c!')

@bot.event
async def on_ready():
    print(">> Coffee Machine starts working! <<")

bot.run('ODU0OTEyMzA5NTU4MjQ3NDU0.YMq1Ig.A11cOpf--jB_YUWzhgLMA3y8AqM')