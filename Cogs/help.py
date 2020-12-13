import discord
from discord.ext import commands

prefix = "Ro "


class Help(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def testhelp(self, ctx, *,arg=None):
		if arg is None:
			em = discord.Embed(title=f"{self.bot.user.name}'s help",color=discord.Color.blue())
			em.add_field(name="General",value=f"`{prefix}help general`")
			em.add_field(name="Fun",value=f"`{prefix}help fun`")
			em.add_field(name="Info",value=f"`{prefix}help info`")
			#em.add_field(name="",value=f"`{prefix}help general`")
			
			
			
			
			
			
			em.set_footer(text=f"Requested by {ctx.author.name}")
			await ctx.send(embed=em)
			
		else:
			for command in self.bot.commands:
				if ((arg == command) or (arg in command.aliases)) and command.help != None:
					em = discord.Embed(title=f"{command}", color=discord.Color.blue(), description= command.help)
					await ctx.send(embed=em)
					break
				else:
					await ctx.send("None")
					break


def setup(bot):
	bot.add_cog(Help(bot))
