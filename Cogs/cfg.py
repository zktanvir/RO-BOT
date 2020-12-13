import discord
from discord.ext import commands
import sqlite3
import os
import pymongo
from Cogs.utils import db



class Config(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(aliases=["setprefix"])
	@commands.guild_only()
	@commands.has_permissions(administrator=True)
	async def prefix(self, ctx, prefix):
		
		await db.set_prefix(ctx.guild.id,prefix)
		await ctx.send(f"Changed bot prefix to {prefix}")
	

def setup(bot):
	bot.add_cog(Config(bot))
