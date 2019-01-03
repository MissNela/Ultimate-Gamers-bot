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


@client.command(pass_context = True)
async def ping(ctx):
    if ctx.message.author.bot:
      return
    else:
      channel = ctx.message.channel
      t1 = time.perf_counter()
      await client.send_typing(channel)
      t2 = time.perf_counter()
      await client.say("Ping: {}ms".format(round((t2-t1)*1000)))

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Pomoc!", color = 0x66BB6A)
    embed.add_field(name = "ping",value = "Bot ti ukáže jeho ping :joy:",inline=False)
    embed.add_field(name = "To je vse",value = "------------",inline=False)
    embed.set_footer(text="Pomoc potřeboval/a {}".format(ctx.message.author.display_name))
    embed.add_field(name="Pomohlo ti to?",value = "Ano :white_check_mark: Ne :x:
    dmmessage = await client.send_message(ctx.message.author, embed=embed)
    reaction1 = '✅'
    reaction2 = '❌'
    await client.add_reaction(dmmessage, reaction1)
    await client.add_reaction(dmmessage, reaction2)
     
    await client.send_message(ctx.message.author, embed=embed)
                              
    
client.run(os.getenv("BOT_TOKEN"))
