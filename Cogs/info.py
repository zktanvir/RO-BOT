import discord
from discord.ext import commands
import wikipedia
import requests
import math
import json


class Info(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=["c", "calc"])
	@commands.guild_only()
	async def calculate(self, ctx, *, equation):
		eq = (equation.replace("×", "*")).replace("÷", "/")
		ans = eval(eq)
		await ctx.send(ans)

	@commands.command(aliases=["ducksearch", "dsearch"])
	@commands.guild_only()
	async def duckduckgo(self, ctx, *, query):
		response = requests.get(
		    f"https://api.duckduckgo.com/?q={query}&format=json&pretty=1")
		result = json.loads(response.text)
		topics = result["RelatedTopics"]
		if len(topics) == 0:
			await ctx.send("Sorry! duckduckgo returned 0 results")
		else:
			for i in range(len(topics)):
				image = topics[i]["Icon"]["URL"]
				text = topics[i]["Text"]
				url = topics[i]["FirstURL"]
				d = discord.Embed(
				    title="duckduckgo",
				    description=text,
				    color=discord.Color.blue(),
				    url=url)
				d.set_image(url=f"https://duckduckgo.com/{image}")
				msg = await ctx.send(embed=d)
				emojis = [
				    "<:arrowleft:762542689425555486>", 
				    "<:arrowright:762542086788349964>"
				]
				for j in emojis:
					await msg.add_reaction(j)
				async def page(i):
				  await d.description()
				def check(reaction, user):
					return user == ctx.author and reaction.message.id == msg.id
				no = 0
				while len(topics) > i:
					try:
						reaction, user = await self.bot.wait_for(
						    "reaction_add", check=check, timeout=30)
						emoji = str(reaction.emoji)
						if emoji == "<:arrowright:762542086788349964>":
							no += 1
						elif emoji == "<:arrowleft:762542689425555486>":
							no -= 1
						await reaction.remove(user)

					except asyncio.TimeoutError:
						await msg.clear_reactions()
					#reaction, user = await self.bot.wait_for("reaction_add", check=check, timeout=30)


def setup(bot):
	bot.add_cog(Info(bot))
