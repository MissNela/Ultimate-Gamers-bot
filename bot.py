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

left = '⏪'
right = '⏩'
r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
general1=discord.Embed(title = "Příkazy pro všechny!", color = discord.Color((r << 16) + (g << 8) + b))
general1.add_field(name = "Ug!ping", value = "Ukáže ti ping bota!",inline=False)
general2=discord.Embed(title = "Připravuje se!", color = discord.Color((r << 16) + (g << 8) + b))
mod1=discord.Embed(title="Připravuje se!", color = discord.Color((r << 16) + (g << 8) + b))
mod2=discord.Embed(title="Připravuje se!", color = discord.Color((r << 16) + (g << 8) + b))

gen_cmd = (general1, general2)
mod_cmd = (mod1, mod2)


def predicate(message, l, r):
    def check(reaction, user):
        if reaction.message.id != message.id or user == client.user:
            return False
        if l and reaction.emoji == left:
            return True
        if r and reaction.emoji == right:
            return True
        return False

    return check

@client.event
async def on_ready():
    print('Jsem tu :D')

@client.event
async def on_reaction_add(reaction, user):
  if reaction.message.server is None:
      if reaction.emoji == '🇬':
          index = 0
          while True:
              msg = await client.send_message(message.author, embed=gen_cmd[index])
              l = index != 0
              r = index != len(gen_cmd) - 1
              if l:
                  await client.add_reaction(msg, left) 
              if r:
                  await client.add_reaction(msg, right)
              react, user = await client.wait_for_reaction(check=predicate(msg, l, r))
              if react.emoji == left:
                  index -= 1
              elif react.emoji == right:
                  index += 1
              await client.delete_message(msg)
      if reaction.emoji == '🇲':
          index = 0
          while True:
              msg = await client.send_message(message.author, embed=mod_cmd[index])
              l = index != 0
              r = index != len(mod_cmd) - 1
              if l:
                  await client.add_reaction(msg, left) 
              if r:
                  await client.add_reaction(msg, right)
              react, user = await client.wait_for_reaction(check=predicate(msg, l, r))
              if react.emoji == left:
                  index -= 1
              elif react.emoji == right:
                  index += 1
              await client.delete_message(msg)
    
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
    embed.add_field(name = "Přidej reakci 🇲",value = "Pro pomoc s moderátorskýmy příkazy!",inline=False)
    embed.add_field(name = "Přidej reakci 🇬",value = "Pro pomoc s přílazy pro všechny!",inline=False)
    embed.set_footer(text="Pomoc potřeboval/a {}".format(ctx.message.author.display_name))
    dmmessage = await client.send_message(author,embed=embed)
    reaction1 = '🇲'
    reaction2 = '🇬'
    await client.add_reaction(dmmessage, reaction1)
    await client.add_reaction(dmmessage, reaction2)
     
    await client.send_message(ctx.message.author, embed=embed)
                              
    
client.run(os.getenv("BOT_TOKEN"))
