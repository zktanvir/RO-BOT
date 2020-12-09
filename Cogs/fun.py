import discord
from discord.ext import commands
import requests
import json
import os
import wolframalpha
import aiohttp
import asyncio
import tenorpy
try:
	import pokepy
except:
	os.system("pip install pokepy")
	import pokepy
try:
	import nekos
except:
	os.system('pip install nekos.py')
	import nekos


apikey= os.environ.get("TENOR")
nasa = os.environ.get("NASA")

class Fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.app = wolframalpha.Client(token)

	@commands.command(aliases=["rjoke", "randomjoke"])
	@commands.guild_only()
	@commands.cooldown(3, 30, commands.BucketType.user)
	async def joke(self, ctx):
		response = requests.get(
		    "https://official-joke-api.appspot.com/random_joke")
		data = json.loads(response.text)
		joke = data["setup"]
		ans = data["punchline"]
		jem = discord.Embed(
		    title="Random Joke",
		    color=discord.Color.blue(),
		    description=f"{joke}\n||{ans}||")
		jem.set_footer(text=f"Requested by {ctx.author.name}")
		await ctx.send(embed=jem)



	
	@commands.command(aliases=['av'])
	@commands.guild_only()
	async def avatar(self, ctx, member: discord.Member = None):
		if member is None:
			member = ctx.author
		em = discord.Embed(title=f'{member.name}', color=discord.Colour.blue())
		pfp = member.avatar_url
		em.set_image(url=pfp)
		await ctx.send(embed=em)

	
	@commands.command()
	async def cat(self, ctx):
		url = nekos.cat()
		em = discord.Embed(title="Meow! 😺", color=discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(text="Powered by nekos.life")
		await ctx.send(embed=em)

	@commands.command()
	async def neko(self, ctx):
		url = nekos.img('neko')
		em = discord.Embed(title="nya! 😸", color=discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(text="Powered by nekos.life")
		await ctx.send(embed=em)

	@commands.command()
	async def waifu(self, ctx):
		url = nekos.img('waifu')
		em = discord.Embed(title="→", color=discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(text="Powered by nekos.life")
		await ctx.send(embed=em)

	@commands.command()
	async def hug(self, ctx, member: discord.Member = None):
		if member == None:
			await ctx.send("*hugs air*")
			return False
		url = nekos.img('hug')
		em = discord.Embed(title="→", color=discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(text="Powered by nekos.life")
		await ctx.send(embed=em)

	@commands.command(aliases=["foxy"])
	async def foxgirl(self, ctx):
		url = nekos.img('fox_girl')
		em = discord.Embed(title="→", color=discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(text="Powered by nekos.life")
		await ctx.send(embed=em)

	@commands.command()
	async def pat(self, ctx, member: discord.Member = None):
		if member == None:
			await ctx.send("*pats air*")
			return False
		url = nekos.img('pat')
		em = discord.Embed(title="→", color=discord.Color.blue())
		em = discord.Embed(title="→", color=discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(text="Powered by nekos.life")
		await ctx.send(embed=em)

	@commands.command(aliases=["tickles"])
	async def tickle(self, ctx, member: discord.Member = None):
		if member == None:
			await ctx.send("*tickles air*")
			return False
		url = nekos.img('tickle')
		em = discord.Embed(title="→", color=discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(
		    icon_url=
		    'https://avatars2.githubusercontent.com/u/34457007?s=200&v=4',
		    text="Powered by nekos.life")
		await ctx.send(embed=em)

	@commands.command(aliases=["owo", "ofy"])
	async def owoify(self, ctx, *, text: str):
		await ctx.message.delete()
		ntext = nekos.owoify(text)
		em = discord.Embed(
		    title='owoified text',
		    color=discord.Color.blue(),
		    description=ntext)
		em.set_footer(text=f"@{ctx.author.name}")
		await ctx.send(embed=em)

	@commands.command()
	async def kiss(self, ctx, member: discord.Member = None):
		if member == None:
			return False
		url = nekos.img('kiss')
		em = discord.Embed(title="→", color=discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(
		    text="Powered by nekos.life",
		    icon_url=
		    'https://avatars2.githubusercontent.com/u/34457007?s=200&v=4')
		await ctx.send(embed=em)

	@commands.command()
	async def slap(self, ctx, member: discord.Member = None):
		if member is None:
			return False
		url = nekos.img('slap')
		em = discord.Embed(title="→", color=discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(
		    text="Powered by nekos.life",
		    icon_url=
		    'https://avatars2.githubusercontent.com/u/34457007?s=200&v=4')
		await ctx.send(embed=em)

	@commands.command()
	async def goose(self, ctx):
		url = nekos.img('goose')
		em = discord.Embed(title="→",color= discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(text="Powered by nekos.life",icon_url="https://avatars2.githubusercontent.com/u/34457007?s=200&v=4")
		await ctx.send(embed=em)
		
	@commands.command()
	async def cuddle(self, ctx, member:discord.Member=None):
		if member is None:
			await ctx.send("*Cuddles air*")
			return False
		url = nekos.img('cuddle')
		em = discord.Embed(title="→",color=discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(text="Powered by nekos.life",icon_url="https://avatars2.githubusercontent.com/u/34457007?s=200&v=4")
		await ctx.send(embed=em)
		
	@commands.command(aliases=["rfact", "fact"])
	async def randomfact(self, ctx):
		fact = nekos.fact()
		em = discord.Embed(title="Random Facts",color=discord.Color.blue(), description=fact)
		em.set_footer(text="Powered by nekos.life",icon_url="https://avatars2.githubusercontent.com/u/34457007?s=200&v=4")
		await ctx.send(embed=em)
		
	@commands.command(aliases=["ask","question"])
	async def why(self, ctx):
		why = nekos.why()
		await ctx.send(why)
		
	@commands.command(aliases=["tcat","asciicat"])
	async def textcat(self, ctx):
		text = nekos.textcat()
		await ctx.send(text)
		
		
		
	@commands.command()
	async def gif(self, ctx, *, query:str):
		q = list(query)
		query = "-".join(q)
		t = tenorpy.Tenor()
		url = t.random(query)
		em = discord.Embed(title="",color=discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(text="Powered by tenor")
		await ctx.send(embed=em)
			
	
		
	@commands.command()
	async def fox(self, ctx):
		response = requests.get("https://randomfox.ca/floof")
		data = json.loads(response.text)
		image = data["image"]
		em = discord.Embed(title="", color=discord.Color.blue())
		em.set_image(url=image)
		em.set_footer(text="Powered by randomfox.ca")
		await ctx.send(embed=em)
		
	@commands.command()
	async def apod(self, ctx):
		url = f"https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
		response = requests.get(url)
		data = json.loads(response.text)
		image = data["hdurl"]
		#obj = Client(nasa)
		#print(obj.apod())
		#res = requests.get(key)
		#data = json.loads(res.text)
		ex = data["explanation"]
		date = data["date"]
		em = discord.Embed(title=data["title"],color=discord.Color.blue())
		em.set_image(url=image)
		em.add_field(name="Date", value=date)
		em.add_field(name="Explanation", value=ex)
		await ctx.send(embed=em)

	@commands.command()
	async def dog(self, ctx):
		url = nekos.img('woof')
		em = discord.Embed(color=discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(text="Powered by nekos.life",icon_url="https://avatars2.githubusercontent.com/u/34457007?s=200&v=4")
		await ctx.send(embed=em)
		


def setup(bot):
	bot.add_cog(Fun(bot))
