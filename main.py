# Skylar
# The uwufied egirl Discord Bot
# Backincorporated Games Studio 2024
import os
import sys

import discord
from colorama import Fore
from discord.ext import commands

import ai
from eventlogger import passfail, printmsg

print(Fore.BLUE+"Backincorporated Games Studio\nSkylar AP v0.7")
printmsg('sys','Connecting to Discord')
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='',intents=intents)

# Bot Startup
@bot.event
async def on_ready():
  printmsg('sys','Connected to Discord','pass')
  
  # Cogs
  printmsg('sys','Loading commands')
  for filename in os.listdir('cogs'):
    if filename.endswith(".py"):
        cog_name = filename[:-3] 
        cog_module = f"cogs.{cog_name}"

        try:
            # Dynamically load the extension
            printmsg('cogs','Loading '+cog_module)
            await bot.load_extension(cog_module)
            printmsg('cogs','Loaded '+cog_module,'pass')
        except Exception as e:
            printmsg('cogs',f'Failed to load {cog_module} {e}','fail')
            printmsg('bot','Failed to complete boot sequence due to exception','fail')
            sys.exit('Failed to complete boot sequence due to exception')

  printmsg('cogs','Loaded all commands','pass')

  # Load AI File
  try:
    printmsg('ai','Loading AI')
    await bot.load_extension('ai')
    printmsg('ai','Loaded AI','pass')
  except Exception as e:
    printmsg('ai',f'Failed to load ai {e}','fail')
    printmsg('sys','Failed to complete boot sequence due to exception','fail')
    sys.exit('Failed to complete boot sequence due to exception')
  
  # Syncing
  try:
    printmsg('bot','Syncing command tree')
    await bot.tree.sync()
    printmsg('bot','Commands synced','pass')
  except Exception as e:
    printmsg('bot',f'Failed to sync command tree {e}','fail')
    printmsg('sys','Failed to complete boot sequence due to exception','fail')
    sys.exit('Failed to complete boot sequence due to exception')

  # Presence
  try:
    printmsg('bot','Setting presence')
    await bot.change_presence(activity=discord.Game(name="giving u a tickle :D"))
    printmsg('bot','Presence set','pass')
  except Exception as e:
    printmsg('bot',f'Failed to set presence {e}','fail')
    printmsg('sys','Failed to complete boot sequence due to exception','fail')
    sys.exit('Failed to complete boot sequence due to exception')

  # Skylar is booted!1!1!1
  printmsg('bot',f'Boot successful, Logged in as {bot.user}')
 

# @mention to talk
# to be moved to a cog
@bot.event
async def on_message(message):
    if bot.user in message.mentions or isinstance(message.channel,discord.DMChannel):
      if message.author == bot.user:
        return
      else:
        if message.guild.id == 1198226747053846528:
          await message.channel.send('This server is banned from using AI')
          return
        msg = message.content.replace('<@1207462122863198310> ','')
        msg = 'user:'+str(message.author)+'msg:'+msg
        msg = "Skylar's AI capability has been shut down temporarily until the AI script has been completed, this is to ensure everyone can use the bot without any issues. Thank you for your patience."
        await message.channel.send(msg)
        #await message.channel.send(ai.botai.generate_ai_response(ai.botai,msg))

bot.run(os.environ['RELEASE_BOT_SECRET'])
