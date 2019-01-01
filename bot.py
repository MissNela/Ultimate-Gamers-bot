
import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time
import datetime
import requests
import json
import praw
import aiohttp

client = commands.Bot(command_prefix = commands.when_mentioned_or("Ug!"))

client.remove_command('help')


@client.event
async def on_ready():
    print('Jsem tu :D')

@client.command()
async def help():
  
  
  
  
