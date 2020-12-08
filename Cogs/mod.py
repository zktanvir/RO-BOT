import discord
from discord.ext import commands


class Moderation(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.has_permissions(kick_members=True)
	@commands.bot_has_permissions(kick_members=True)
	@commands.guild_only()
	async def kick(self,
	               ctx,
	               member: discord.Member = None,
	               *,
	               reason="I don't know the reason"):
		if member != None:
			await member.kick(reason=reason)
			await ctx.send(
			    f"{member.name} was successfully kicked by {ctx.author.name}")
		else:
			await ctx.send(f"I can't kick air :expressionless:")

	@kick.error
	async def kick_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send(f"You're missing the `Kick Members` permission")

	@commands.command()
	@commands.guild_only()
	@commands.has_permissions(ban_members=True)
	@commands.bot_has_permissions(ban_members=True)
	async def ban(self,
	              ctx,
	              member: discord.Member = None,
	              *,
	              reason="I don't know the reason"):
		if member != None:
			await member.ban(reason=reason)
			await ctx.send(f"{member.name} was banned by {ctx.author.name}")
		else:
			await ctx.send("Should I ban air? :face_with_raised_eyebrow:")

	@ban.error
	async def ban_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send(f"You're missing the `Ban Members` permission")

	@commands.command()
	@commands.guild_only()
	@commands.has_permissions(kick_members=True, ban_members=True)
	@commands.bot_has_permissions(kick_members=True, ban_members=True)
	async def warn(self, ctx, member: discord.Member = None, *, reason):
		if member != None and reason != None:
			warn = discord.Embed(
			    title=f"Warning!",
			    color=discord.Color.blue(),
			    description=
			    f"{member.name} was warned by {ctx.author.name} because {reason}"
			)

			await ctx.send(embed=warn)

			warning = discord.Embed(
			    title=f"Warning!",
			    color=discord.Color.red(),
			    description=
			    f"You have been warned by {ctx.author.name} because {reason}")
			await member.send(embed=warning)

		else:
			if member == None:
				await ctx.send(f"I can't warn air :expressionless:")
			elif reason == None:
				await ctx.send(f"Please provide a reason")

	@warn.error
	async def warn_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send(
			    f"Seems that you don't have permission to warn anyone")


def setup(bot):
	bot.add_cog(Moderation(bot))
