import discord
from discord.ext import commands
from discord.message import Message
import datetime
import json

with open('setting.json', 'r', encoding="utf8") as jFile:
    jdata = json.load(jFile)