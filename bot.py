# bot.py
"""
__TOSEARCH__
await keyword
async keyword
@ keyword
raise keyword
__IDEA__

__NOTES__
updates each time I run it
"""

import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)

bot = commands.Bot(command_prefix='ye')

@bot.event
async def on_ready():
	print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(
		f'Hi {member.name}, welcome fatass'
	)

@bot.event
async def on_error(event, *args, **kwargs):
	with open('logs/err.log', 'a') as f:
		if event == 'on_message':
			f.write(f'Unhandled Message: {args[0]}\n')
		else:
			raise
#
# COMMANDS
#
@bot.command(name="fatass", help="literally fatass")
async def on_message(ctx):
	await ctx.send("im a fatass")

@bot.command(name="1v1", help="sends a 1v1")
async def on_message(ctx):
	await ctx.send(file=discord.File("1v1 me noob.png"))

bot.run(TOKEN)