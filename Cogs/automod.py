import discord
from discord.ext import commands
import sqlite3



class Automod(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


    #adding soon
    
    
def setup(bot):
  bot.add_cog(Automod(bot))
