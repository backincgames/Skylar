# Skylar AP
# Codename Anonymous Prestige

import os

import discord
from colorama import Fore
from discord.ext import commands

import ai

print(Fore.BLUE+"Backincorporated Games Studio\nSkylar AP v0.7")
print(Fore.WHITE+"[BOT]: Connecting to Discord")
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='',intents=intents)

# Bot Startup
@bot.event
async def on_ready():
  print(Fore.GREEN +'[BOT]:'+Fore.GREEN+' Connected to Discord')
  bootexceptions = 0
  cmdbootexceptions = 0
  
  # Cogs
  print(Fore.WHITE +'[BOT]: Loading commands')
  for filename in os.listdir('cogs'):
    if filename.endswith(".py"):
        cog_name = filename[:-3]  # Remove the '.py' extension
        cog_module = f"cogs.{cog_name}"

        try:
            # Dynamically load the extension
            print(Fore.WHITE + f"[BOT]: Loading {cog_module}")
            await bot.load_extension(cog_module)
            print(Fore.GREEN + f"[BOT]: Loaded {cog_module}")
        except Exception as e:
            print(Fore.RED + f"[BOT]: Failed to load {cog_module}: {e}")
            cmdbootexceptions = cmdbootexceptions + 1
            bootexceptions = bootexceptions + 1

  if cmdbootexceptions == 0:
    print(Fore.GREEN +'[BOT]: Loaded all commands')
  else:
    print(Fore.YELLOW +f'[BOT]: Failed to load {cmdbootexceptions} cogs')

  # Syncing
  try:
    print(Fore.WHITE +'[BOT]: Syncing command tree')
    await bot.tree.sync()
    print(Fore.GREEN +'[BOT]: Commands synced')
  except Exception as e:
    print(Fore.RED + f"[BOT]: Failed to sync command tree: {e}")
    bootexceptions = bootexceptions + 1

  # Presence
  try:
    print(Fore.WHITE +'[BOT]: Updating presence')
    await bot.change_presence(activity=discord.Game(name="giving u a tickle :D"))
    print(Fore.GREEN +'[BOT]: Presence updated')
  except Exception as e:
    print(Fore.RED + f"[BOT]: Failed to update presence: {e}")
    bootexceptions = bootexceptions + 1

  # Skylar is booted!1!1!1
  if bootexceptions == 0:
    print(Fore.GREEN +f'[BOT]: Boot successful, Logged in as {bot.user}')
  else:
    print(Fore.YELLOW +f'[BOT]: Boot successful with {bootexceptions} exceptions, Logged in as {bot.user}')
 

### @mention to talk
@bot.event
async def on_message(message):
    if bot.user in message.mentions or isinstance(message.channel,discord.DMChannel):
      if message.author == bot.user:
        return
      else:
        str = message.content.replace('<@1207462122863198310> ','')
        await message.channel.send(ai.generate_ai_response(str))

bot.run(os.environ['RELEASE_BOT_SECRET'])