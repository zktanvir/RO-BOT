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

	"""@commands.command()
	@commands.has_permissions(mute_members=True)
	async def mute(self, ctx, member: discord.Member = None, dur, reason):
		try:
		  role = discord.utils.get(ctx.guild.roles, name="muted"
		  await member.add_roles(role)
		except:
		  msg = await ctx.send("There's no muted role for this server. Should I create one?[reply with yes or no]")
		  reply = await bot.wait_for('message',check=lambda message: message.author == ctx.author, timeout=30)
		  if reply.strip().lower() == 'yes' or reply.strip().lower() == 'y':
		    role = await ctx.guild.create_role(name="Shamelessly muted")
		    for channel in ctx.guild.channels:
		      await channel.set_permissions(muted, send_messages=False,read_message_history=False,read_messages=False)
		      await member.add_roles(role)"""

def setup(bot):
	bot.add_cog(Moderation(bot))
