import discord
from discord.ext import commands
import asyncio
import ast
#import nekos

#import ast
#import discord

#from discord.ext import commands


def insert_returns(body):
	# insert return stmt if the last expression is a expression statement
	if isinstance(body[-1], ast.Expr):
		body[-1] = ast.Return(body[-1].value)
		ast.fix_missing_locations(body[-1])

	# for if statements, we insert returns into the body and the orelse
	if isinstance(body[-1], ast.If):
		insert_returns(body[-1].body)
		insert_returns(body[-1].orelse)

	# for with blocks, again we insert returns into the body
	if isinstance(body[-1], ast.With):
		insert_returns(body[-1].body)


class Owner(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=["le", "load"])
	@commands.is_owner()
	async def load_extension(self, ctx, cog):
		try:
			self.bot.load_extension(f"Cogs.{cog}")
		except Exception as e:
			await ctx.send(f"**Error:** {type(e).__name__} - {e}")
		else:
			await ctx.send(f"Successfully loaded {cog}")

	@commands.command(aliases=["unload"])
	@commands.is_owner()
	async def unload_extension(self, ctx, cog):
		try:
			self.bot.unload_extension(f"Cogs.{cog}")
		except Exception as e:
			await ctx.send(f"**Error:** {type(e).__name__} - {e}")
		else:
			await ctx.send(f"Successfully unloaded {cog}")

	@commands.command(aliases=["reload"])
	@commands.is_owner()
	async def reload_extension(self, ctx, cog):
		try:

			self.bot.unload_extension(f"Cogs.{cog}")
			self.bot.load_extension(f"Cogs.{cog}")
		except Exception as e:

			await ctx.send(f"**Error:** {type(e).__name__} - {e}")
		else:
			await ctx.send(f"Successfully reloaded {cog}")

	@commands.command(aliases=["r"])
	@commands.guild_only()
	@commands.is_owner()
	async def repeat(self, ctx, *, msg):
		await ctx.message.delete()
		async with ctx.typing():
			await asyncio.sleep(3)
		await ctx.send(msg)

	"""@commands.command()
	@commands.is_owner()
	async def reload_all(self, ctx):
		for i in """

	@commands.command(aliases=["eval"])
	@commands.is_owner()
	async def ev(self, ctx, *, cmd):
		fn_name = "_eval_expr"
		cmd = cmd.strip("` py")
		cmd = "\n".join(f"    {i}" for i in cmd.splitlines())
		body = f"async def {fn_name}():\n{cmd}"
		parsed = ast.parse(body)
		body = parsed.body[0].body
		insert_returns(body)
		env = {
		    'bot': ctx.bot,
		    'discord': discord,
		    'commands': commands,
		    'ctx': ctx,
		    '__import__': __import__
		}
		res = exec(compile(parsed, filename="<ast>", mode="exec"), env)
		result = (await eval(f"{fn_name}()", env))
		#await ctx.send(f"```py\n{res}```")


def setup(bot):
	bot.add_cog(Owner(bot))
