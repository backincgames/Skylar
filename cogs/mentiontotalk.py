import discord
from discord.ext import commands

import embeds as embeds
from eventlogger import printmsg, warn

class mentiontotalk(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self._last_member = None

def setup(client):
  return client.add_cog(mentiontotalk(client))