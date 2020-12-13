import discord
from discord.ext import commands
import time
import os
from colorama import Fore,Back,Style
from datetime import datetime
from Cogs.utils import db



default_prefix = "Ro "


async def get_prefix(bot,message):
	guild_id = message.guild.id
	prefix = await db.prefix(guild_id)
	return prefix
	




intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(
    command_prefix=get_prefix,
    intents=intents,
    case_insensitive=True)
#bot.remove_command("help")


@bot.event
async def on_ready():
	print(Fore.BLUE,"""
  ____   ___        ____   ___ _____
 |  _ \ / _ \      | __ ) / _ \_   _|
 | |_) | | | |_____|  _ \| | | || |
 |  _ <| |_| |_____| |_) | |_| || |
 |_| \_\\\___/      |____/ \___/ |_|

""")

	await bot.change_presence(
	    activity=discord.Activity(
	        type=discord.ActivityType.listening, name="Ro help"))


for filename in os.listdir('./Cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f"Cogs.{filename[:-3]}")


token = os.environ.get('TOKEN')
bot.run(token, reconnect=True)
