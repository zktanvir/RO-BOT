import discord
from discord.ext import commands
import requests
import json
import os
import random
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
	import giphypop
except:
	os.system('pip install nekos.py')
	os.system("pip install giphypop")
	import nekos
	import giphypop


TENOR_API_KEY= os.environ.get("TENOR")
NASA_API_KEY = os.environ.get("NASA_API_KEY")

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
		em = discord.Embed(title="Nya! 😸", color=discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(text="Powered by nekos.life")
		await ctx.send(embed=em)

	@commands.command()
	async def waifu(self, ctx):
		url = nekos.img('waifu')
		em = discord.Embed(color=discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(text="Powered by nekos.life")
		await ctx.send(embed=em)

	@commands.command()
	async def hug(self, ctx, member: discord.Member = None):
		if member == None:
			await ctx.send("*hugs air*")
			return False
		url = nekos.img('hug')
		em = discord.Embed(title="", color=discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(text="Powered by nekos.life")
		await ctx.send(embed=em)

	@commands.command(aliases=["foxy"])
	async def foxgirl(self, ctx):
		url = nekos.img('fox_girl')
		em = discord.Embed(title="", color=discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(text="Powered by nekos.life")
		await ctx.send(embed=em)

	@commands.command()
	async def pat(self, ctx, member: discord.Member = None):
		if member == None:
			await ctx.send("*pats air*")
			return False
		url = nekos.img('pat')
		em = discord.Embed(title="", color=discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(text="Powered by nekos.life")
		await ctx.send(embed=em)

	@commands.command(aliases=["tickles"])
	async def tickle(self, ctx, member: discord.Member = None):
		if member == None:
			await ctx.send("*tickles air*")
			return False
		url = nekos.img('tickle')
		em = discord.Embed(title="", color=discord.Color.blue())
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
		em = discord.Embed(title="", color=discord.Color.blue())
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
		em = discord.Embed(title="", color=discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(
		    text="Powered by nekos.life",
		    icon_url=
		    'https://avatars2.githubusercontent.com/u/34457007?s=200&v=4')
		await ctx.send(embed=em)

	@commands.command()
	async def goose(self, ctx):
		url = nekos.img('goose')
		em = discord.Embed(title="",color= discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(text="Powered by nekos.life",icon_url="https://avatars2.githubusercontent.com/u/34457007?s=200&v=4")
		await ctx.send(embed=em)
		
	@commands.command()
	async def cuddle(self, ctx, member:discord.Member=None):
		if member is None:
			await ctx.send("*Cuddles air*")
			return False
		url = nekos.img('cuddle')
		em = discord.Embed(title="",color=discord.Color.blue())
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
		g = tenorpy.Tenor()
		
		url = g.random(query)
		
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
		url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
		response = requests.get(url)
		data = json.loads(response.text)
		image = data["hdurl"]
		
		ex = data["explanation"]
		date = data["date"]
		em = discord.Embed(title=data["title"],color=discord.Color.blue())
		em.set_image(url=image)
		em.add_field(name="Date", value=date)
		em.add_field(name="Explanation", value=ex)
		await ctx.send(embed=em)
		
		
		
	@commands.command()
	async def bird(self, ctx):
		
		response = requests.get("https://shibe.online/api/birds")
		response = response.json()
		
		url = response[0]
		em = discord.Embed(title="", color=discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(text="Powered by shibe.online")
		await ctx.send(embed=em)
		
	@commands.command()
	async def shibe(self, ctx):
		response = requests.get("https://shibe.online/api/shibes")
		response = response.json()
		url = response[0]
		em = discord.Embed(title="",color=discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(text="Powered by shibe.online")
		await ctx.send(embed=em)
		
	@commands.command()
	async def kemonomimi(self, ctx):
		url = nekos.img('kemonomimi')
		em = discord.Embed(color=discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(text="Powered by nekos.life",icon_url="https://avatars2.githubusercontent.com/u/34457007?s=200&v=4")
		await ctx.send(embed=em)
		
	@commands.command()
	async def baka(self, ctx, member:discord.Member=None):
		url = nekos.img('baka')
		em = discord.Embed(color=discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(text="Powered by nekos.life",icon_url="https://avatars2.githubusercontent.com/u/34457007?s=200&v=4")
		await ctx.send(embed=em)
		
	@commands.command()
	async def smug(self, ctx, member:discord.Member=None):
		url = nekos.img('smug')
		em = discord.Embed(color=discord.Color.blue())
		em.set_image(url=url)
		em.set_footer(text="Powered by nekos.life",icon_url="https://avatars2.githubusercontent.com/u/34457007?s=200&v=4")
		await ctx.send(embed=em)
		
		
    	@commands.command()
	@commands.cooldown(5, 30, commands.BucketType.user)
	async def feed(self, ctx, member: discord.Member = None):
		if member is None:
			await ctx.send('*feeds air*')
			return False
		url = nekos.img('feed')
		em = embeds.fun_embed(img=url, footer="Powered by nekos.life")
		await ctx.send(embed=em)


	@commands.command(aliases=["cmm"])
	async def changemymind(self, ctx, *, text=None):
		if text is None:
			await ctx.send("Provide some text")
			return False
		api = NekoBotAsync()
		img = (await api.changemymind(text)).message
		em = embeds.fun_embed(img=img, footer="")
		await ctx.send(embed=em)

	@commands.command()
	async def magik(self, ctx, member:discord.Member=None):
		async with ctx.typing():
			if member is None:
				member = ctx.author
			img = f"https://cdn.discordapp.com/avatars/{member.id}/{member.avatar}.jpg?size=1024"
			async with aiohttp.ClientSession().get(f"https://nekobot.xyz/api/imagegen?type=magik&image={img}") as resp:
				data = json.loads(await resp.text())
			url = data["message"]
			em = embeds.fun_embed(title="Magik",footer="Powered by nekobot.xyz",img=url)
		await ctx.send(embed=em)

	@commands.command()
	async def ship(self, ctx, user1:discord.Member, user2:discord.Member=None):
		if user2 is None:
			user2 = ctx.author
		user1av = f"https://cdn.discordapp.com/avatars/{user1.id}/{user1.avatar}.jpg?size=1024"
		user2av = f"https://cdn.discordapp.com/avatars/{user2.id}/{user2.avatar}.jpg?size=1024"
		async with ctx.typing():
			async with aiohttp.ClientSession().get(f"https://nekobot.xyz/api/imagegen?type=ship&user1={user1av}&user2={user2av}") as resp:
				data = json.loads(await resp.text())
			img = data["message"]
			name1 = user1.name
			name2 = user2.name
			len1 = round(len(name1)/2)
			len2 = round(len(name2)/2)
			name1 = name1[:len1]
			name2 = name2[len2:]
			name = name1 + name2
			em = embeds.fun_embed(title=f"Shipped {user1.name} & {user2.name}", des=f"We call it {name.title()}", img=img, footer="Powered by nekobot.xyz")
		await ctx.send(embed=em)


	@commands.command()
	async def deepfry(self, ctx, user:discord.Member=None):
		if user is None:
			user = ctx.author
		async with ctx.typing():
			async with aiohttp.ClientSession().get(f"https://nekobot.xyz/api/imagegen?type=deepfry&image=https://cdn.discordapp.com/avatars/{user.id}/{user.avatar}.jpg?size=1024") as resp:
				data = await resp.json()
			img = data["message"]
			em = embeds.fun_embed(title="",img=img,footer="Powered by nekobot.xyz")
		await ctx.send(f"Deepfried {user.name}",embed=em)


	@commands.command(aliases=['randomquote','rquote'])
	async def quote(self, ctx):
		resp = requests.get("https://type.fit/api/quotes")
		data = resp.json()
		one = random.choice(data)
		author = one["author"]
		text = one["text"]
		em = embeds.fun_embed(title="Random Quotes", des=f'{text}\n{author:>40}')
		await ctx.send(embed=em)




def setup(bot):
	bot.add_cog(Fun(bot))
