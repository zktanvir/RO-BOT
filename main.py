import discord
from discord.ext import commands
import os
from colorama import Fore,Back,Style



DEFAULT_PREFIX = "Ro "


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(
    command_prefix=DEFAULT_PREFIX,
    intents=intents,
    case_insensitive=True)


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

"""
create a ".env" file with the following
```
TOKEN="YOUR TOKEN HERE"
```
"""


token = os.environ.get('TOKEN')
bot.run(token, reconnect=True)
