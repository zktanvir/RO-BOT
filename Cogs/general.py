import discord
from discord.ext import commands
import time
import psutil
import sys

before = time.monotonic()


def convert(seconds):
	seconds = seconds % (24 * 3600)
	hour = seconds // 3600
	seconds %= 3600
	minutes = seconds // 60
	seconds %= 60
	day = hour // 24
	uptime = "`%2d`d:`%d`h:`%2d`m:`%02d`s" % (day, hour, minutes, seconds)
	return uptime

def gconvert(t):
	hour = ["h","hour","hours"]
	minute = ["m","min","mins","minutes","minute"]
	second = ["s","second","seconds","sec","secs"]
	return True

class General(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.guild_only()
	async def ping(self, ctx):
		t1 = time.monotonic()
		msg = await ctx.send(
		    f"<a:pong:785137638427721728> Pong! (bot latency: {round(self.bot.latency * 1000)})")
		t2 = time.monotonic()
		await msg.edit(
		    content=
		    f"<a:pong:785137638427721728> Pong! (bot latency: {round(self.bot.latency * 1000)} ms, latency: {round((t2-t1) * 1000)} ms)"
		)

	@commands.command()
	@commands.guild_only()
	async def stats(self, ctx):
		after = time.monotonic()
		uptime = after - before
		users = 0
		for guild in self.bot.guilds:
			users += len(guild.members)

		stats = discord.Embed(
		    title=f"{self.bot.user.name}", color=discord.Color.blue())
		stats.add_field(
		    name="RAM/CPU Usage",
		    value=
		    f"CPU → `{psutil.cpu_percent(interval=1)}%`\nRAM → `{psutil.virtual_memory().percent}%`"
		)
		stats.add_field(name='Uptime', value=f"{convert(uptime)}")
		stats.add_field(
		    name='Statistics',
		    value=
		    f"Guilds → {len(self.bot.guilds)}\nUsers → {users}\nDiscord.py → v{discord.__version__}\nPython → v{((sys.version).split(' '))[0]}"
		)
		stats.set_footer(text=f"Requested by {ctx.author.name}")
		await ctx.send(embed=stats)

	

def setup(bot):
	bot.add_cog(General(bot))
