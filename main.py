import discord
from discord.ext import commands
import time
import os

default_prefix = "Ro "

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(
    command_prefix=default_prefix, intents=intents, case_insensitive=True)
#bot.remove_command("help")


@bot.event
async def on_ready():
	await bot.change_presence(
	    activity=discord.Activity(
	        type=discord.ActivityType.listening, name="Ro help"))


for filename in os.listdir('./Cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f"Cogs.{filename[:-3]}")


token = os.environ.get('TOKEN')
bot.run(token)
