import discord
from discord.ext import commands
import asyncio
import ast
from datetime import datetime
from colorama import Fore,Back,Style

def insert_returns(body):
	if isinstance(body[-1], ast.Expr):
		body[-1] = ast.Return(body[-1].value)
		ast.fix_missing_locations(body[-1])

	if isinstance(body[-1], ast.If):
		insert_returns(body[-1].body)
		insert_returns(body[-1].orelse)

	if isinstance(body[-1], ast.With):
		insert_returns(body[-1].body)


class Owner(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@commands.Cog.listener()
	async def on_ready(self):
		print(Back.BLUE,f"{datetime.now()}Owner cog loaded")
	
	
	@commands.command(aliases=["le", "load"],hidden=True)
	@commands.is_owner()
	async def load_extension(self, ctx, cog):
		try:
			self.bot.load_extension(f"Cogs.{cog}")
		except Exception as e:
			await ctx.send(f"**Error:** {type(e).__name__} - {e}")
		else:
			await ctx.send(f"Successfully loaded {cog}")

	@commands.command(aliases=["unload"], hidden=True)
	@commands.is_owner()
	async def unload_extension(self, ctx, cog):
		try:
			self.bot.unload_extension(f"Cogs.{cog}")
		except Exception as e:
			await ctx.send(f"**Error:** {type(e).__name__} - {e}")
		else:
			await ctx.send(f"Successfully unloaded {cog}")

	@commands.command(aliases=["reload"],hidden=True)
	@commands.is_owner()
	async def reload_extension(self, ctx, cog):
		try:

			self.bot.unload_extension(f"Cogs.{cog}")
			self.bot.load_extension(f"Cogs.{cog}")
		except Exception as e:

			await ctx.send(f"**Error:** {type(e).__name__} - {e}")
		else:
			await ctx.send(f"Successfully reloaded {cog}")

	@commands.command(aliases=["r"], hidden=True)
	@commands.guild_only()
	@commands.is_owner()
	async def repeat(self, ctx, *, msg):
		await ctx.message.delete()
		async with ctx.typing():
			await asyncio.sleep(3)
		await ctx.send(msg)

	

	@commands.command(aliases=["eval"], hidden=True)
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
		try:
			res = exec(compile(parsed, filename="<ast>", mode="exec"), env)
			result = (await eval(f"{fn_name}()", env))
			await ctx.send(f"```py\n{result}```")
			await ctx.send(f"```py\n{res}```")
		except Exception as e:
			await ctx.send(f"```py\n**Error:** {type(e).__name__} - {e}```")


def setup(bot):
	bot.add_cog(Owner(bot))
