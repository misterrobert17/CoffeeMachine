import discord
from discord.ext import commands
from discord.message import Message
import datetime
import json

with open('setting.json', 'r', encoding="utf8") as jFile:
    jdata = json.load(jFile)

bot = commands.Bot(command_prefix='c!')

@bot.event
async def on_ready():
    print(">> Coffee Machine starts working!! <<")

@bot.event
async def on_message_delete(msg: Message):
    channel = bot.get_channel(int(jdata['MonitorRoom']))
    embed = discord.Embed(
        title=f'A message from {msg.channel.name} was deleted!',
        color=0xff0000, 
        timestamp=datetime.datetime.utcnow()
    )
    embed.add_field(name='Original Author', value=msg.author, inline=False)
    embed.add_field(name='Contents', value=msg.content, inline=False)
    embed.set_footer(text=msg.guild.name)
    await channel.send(embed=embed)

@bot.event
async def on_message_edit(before: Message, after: Message):
    channel = bot.get_channel(int(jdata['MonitorRoom']))
    embed = discord.Embed(
        title=f'A message from {before.channel.name} was edited!',
        color=0xFFE400, 
        description=f"{before.author} [Check]({after.jump_url})", 
        timestamp=datetime.datetime.utcnow()
    )
    embed.add_field(name='Original Message', value=f"```{before.content}```", inline=False)
    embed.add_field(name='New Message', value=f"```{after.content}```", inline=False)
    embed.set_footer(text=before.guild.name)
    await channel.send(embed=embed)
    
@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms')

bot.run(jdata['TOKEN'])