import discord
from discord.ext import commands
from replit import db

import embeds

# Currency Utilities
async def transfer(ctx,id1,id2,amount,item,silent): # From ID1 to ID2
  if (item != None): # Item Transfer
    pass
  else: # Money Transfer
    if (id1 == 'bot'): # Bot gives U$ to user (daily etc)
      try:
        await db["821243680396279831bal"] == await db["821243680396279831bal"] - amount
        await db[f"{id2}bal"] == db[f"{id2}bal"] + amount
      except:
        print(f'Transaction error from Skylar to {id2} of {amount}U$')
        await ctx.send(f'Unable to add {amount}U$ to your wallet, Please contact Backincorporated Games Studio for assistance, this will be logged')
        return 2
      else:
        if (silent == True):
          return 1
        else:
          await ctx.send(f'Transaction Completed from Skylar to <@{id2}> ')
          return 1
    else: # Transfering money from user to user
      s = await IDCheck(ctx,id2,False)
      if (s == 1):
        try:
          db[f"{id1}bal"] = db[f"{id1}bal"] - amount
          db[f"{id2}bal"] = db[f"{id2}bal"] + amount
        except:
          print(f'Transaction error from {id1} to {id2} of {amount}U$')
          await ctx.send(f'Unable to add {amount}U$ to your wallet, Please contact Backincorporated Games Studio for assistance, this will be logged')
          return 2
        else:
          if (silent == True):
            return 1
          else:
            await ctx.send(f'Transaction Completed from <@{id1}> to <@{id2}>')
            return 1
      elif (s == 2):
        await ctx.send('This user is banned and is unable to use the bot')
      else:
        await ctx.send(f'This user has not tried mee outt yet! Tell <@{id2}> to try mee outtt^^')
        
# Checks user status
# If they dont exist in DB they will be added with 1K U$
async def IDCheck(ctx,id,setup):
  if f'{id}status' in db.keys():
    if (db[f'{id}status'] == 1): # Existing user
      return 1
    elif (db[f'{id}status'] == 2): # Banned user
      if (setup == True):
        await ctx.send('You are banned and are unable to use the bot')
      return 2
  else:
    if (setup == True):
      try:
        db[f"{id}status"] = 1
        db[f"{id}bal"] = 1000
        db[f"{id}donated"] = 0
        db[f"{id}raised"] = 0
      except:
        await ctx.send('Error setting up your user, Contact Backincorporated Games Studio for assistance, this will be logged')
      else:  
        await ctx.send(embed=embeds.LoadEmbedData('WelcomeEmbed'))
        return 1
    else:
      return 3

class currencycmds(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self._last_member = None

  # Balance
  # Check yours or someone elses balance
  @commands.hybrid_command(name="balance", description="Check your balance ;)")
  async def balance(self,ctx, user: discord.Member=None):
    if (user == None):
      user = ctx.author
      s = await IDCheck(ctx,user.id,True)
    else:
      s = await IDCheck(ctx,user.id,False)
    if (s==1):
      await ctx.send(f'You have `{db[f"{user.id}bal"]}U$`, woaw nice pookie<3 ')
    elif (s==2): # Banned user
      pass
    else:
      await ctx.send('An error has occured')

  # Donate
  # Give U$ to another user and add to your raised/donated
  @commands.hybrid_command(name="donate", description='Donate U$ to others^^')
  async def donate(self,ctx, user: discord.Member, amount: int):
    s = await IDCheck(ctx,ctx.message.author.id,True)
    if (s==1):
      t = await transfer(ctx,ctx.message.author.id,user.id,amount,None,True)
      if (t==1):
        try:
          db[f'{ctx.author.id}donated'] = db[f'{ctx.author.id}donated'] + amount
          db[f'{user.id}raised'] = db[f'{user.id}raised'] + amount
        except:
          await ctx.send('Unable to add U$ to raised/donated')
        await ctx.send(f'You have donated {amount}U$ to {user.mention}!1!11!!!')
      else:
        pass
    elif (s==2): # Banned user
      pass
    else:
        await ctx.send('An error has occured')
    
def setup(client):
  return client.add_cog(currencycmds(client))