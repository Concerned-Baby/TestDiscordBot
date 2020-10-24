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
@bot.command(name="votekick", help="kicks someone")
async def on_message(ctx, arg): #needs random chance, needs to get @'s, needs to disconnect someone
#needs to get a @'d person
#guild --> voice channels --> people

#TODO:
#match channel members to args
#make sure that the vc's are being iterated throught
#make sure args are correct, and sent a message if not

	#print(ctx)
	#print(ctx.author.display_name)
	#print(ctx.guild)
	print(ctx.guild.voice_channels)
	for vc in ctx.guild.voice_channels:
		print("VC Found: " + str(vc))
		print("Members: " + str(vc.members)) #not recognizing members for some reason
		for member in vc.members:
			print("Member display: " + str(member.display_name))
			print("Member: " + str(member.id))
			print("Arg: " + str(ctx.args[1])[4:-1])
			print("Is member: " + str(arg == member))
		print(vc.members)
	#print(ctx.args[1])


	await ctx.send(str(ctx.args[1]) + " was the Imposter")
"""
else:
	person @'d + 1
	send (num / <needed>)
if <people in senders vc> / 2 + 1 < amountL:
	if person in vc
		if *chacne*
			is imposter
		is not imposter
		kick
"""


bot.run(TOKEN)