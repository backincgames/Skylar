import discord
from colorama import Fore
from discord.ext import commands

import embeds as embeds


class cutecmds(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self._last_member = None

  # Hug command
  # Hug another user in the server (or put a userid in lol)
  @commands.hybrid_command(name="hug", description="Hug someone :3")
  async def hug(self,ctx, user: discord.Member):
    if (user.id == ctx.author.id):
      await ctx.send(f'{ctx.author.mention} lol you cant hug yourself')
    else:
      await ctx.send(f'*You walk up to {user.mention}, then slowly you slide your soft arms around them. {user.mention} gives you a smile and hugs you back* [awwwwwwww^^](https://tenor.com/view/sending-hugs-virtual-hugs-sending-virtual-hugs-gif-22729029)')

  # Kiss command
  # Kiss another user in the server (or put a userid in lol)
  @commands.hybrid_command(name="kiss", description="Kiss someone :3")
  async def kiss(self,ctx, user: discord.Member):
    if (user.id == ctx.author.id):
      await ctx.send(f'{ctx.author.mention} lol you cant kiss yourself')
    else:
      await ctx.send(f'*You walk up to {user.mention}, you slowly lay your mouth on {user.mention}. {user.mention} is filled with love and immediately kisses u back* soo cute^^')

def setup(client):
  return client.add_cog(cutecmds(client))