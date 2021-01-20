# bot.py
"""
__TOSEARCH__
await keyword
async keyword
@ keyword
raise keyword

__IDEA__
need to give prompt on error
except
random person generator
clear logs on startup

__NOTES__
updates each time I run it from command time
"""

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import datetime
import __options
import random
import time

def log(string):
	t = time.localtime()
	current_time = time.strftime("%H:%M:%S", t)
	log = open("logs/runtimelog.txt", "a")
	log.write("[%s] %s\n" % (str(current_time), string))
	log.close()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

log(f"open on token {TOKEN}")

bot = commands.Bot(command_prefix='ye ')

@bot.event
async def on_ready():
	print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_member_join(member):
	log(f"Member join {member.name}")
	await member.create_dm()
	await member.dm_channel.send(
		f"Hi {member.name}, welcome nerd"
	)

@bot.event
async def on_error(event, *args, **kwargs):
	with open('logs/errlog.txt', 'a') as file:
		if event == 'on_message':
			file.write(f'Unhandled Error: {args[0]}\n')
		else:
			raise
#
#Beating Daniel
#
"""
@bot.event
async def on_message(message):
	
	if message.author == bot:
		return
	print(message.content)
	#if message.content[-2:] == "68":
	#	await message.channel.send(message.content[:-2] + "69")
	if message.content.count("fuck") != 0 or message.content.count("shit") != 0:
		old = 0
		with open('swearjar/%s' % message.author, 'r') as file:
			old = int(file.read())
			old += message.content.count("fuck") + message.content.count("shit") != 0
		with open('swearjar/%s' % message.author, 'w') as file:
			file.write(old)
"""

#
# COMMANDS
#
@bot.command(name="fatshame", help="literally bullying")
async def on_message(ctx, who="", times=1):
	log("CMD: fatshame")
	log("From: " + str(ctx.guild))
	if who == "":
		await ctx.send("Please Specify Who Is Fat [ye fatshame @ye boi]")
	if times > 20:
		await ctx.send("Fat shame them a little less would ya?")
	else:
		await ctx.send(__options.fatgenerate(str(who)) * times)

@bot.command(name="1v1", help="[n/a] sends a 1v1")
async def on_message(ctx, attendee=""):
	log("CMD: 1v1")
	if attendee == "":
		await ctx.send("Please Specify Who Is 1v1ing [ye 1v1 @ye boi]")
	else:
		await ctx.send("its not working. please don't try again")



@bot.command(name="k", help="please dont use this")
async def on_message(ctx):
	log("CMD: k")
	log("From: " + str(ctx.guild))
	await ctx.send("read the help menu")

@bot.command(name="logscore", help="sets a new score for count")
async def on_message(ctx, arg=0):
	log("CMD: setscore")
	log("From: " + str(ctx.guild))
	if arg == 0:
		await ctx.send("Please Enter A Score [ye logscore 69]")
	else:
		file = open("scorecounter/%sscores.txt" % str(ctx.guild), "a")
		file.write(str(arg) + "\n")
		file.close()
		await ctx.send("New Score: " + str(arg) + " Logged")

@bot.command(name="topscore", help="Gets the top count score for this server")
async def on_message(ctx):
	log("CMD: setscore")
	log("From: " + str(ctx.guild))
	file = open("scorecounter/%sscores.txt" % str(ctx.guild), "r")
	best = 0
	for line in file.readlines():
		best = max(best, int(line))
	file.close()
	await ctx.send("Best Score: " + str(best))

@bot.command(name="topscores", help="Gets the top 10 count score for this server")
async def on_message(ctx, arg=10):
	log("CMD: setscore")
	log("From: " + str(ctx.guild))
	file = open("scorecounter/%sscores.txt" % str(ctx.guild), "r")
	bests = []
	for line in file.readlines():
		bests.append(int(line))
	file.close()
	bests.sort()
	text = ("Best %d Scores for %s: \n" % (arg, str(ctx.guild)))
	for i in range(1, arg + 1):
		try:
			text += ("%d)\t%d\n" % (i, bests[-1 * i]))
		except IndexError:
			text += ("%d)\t0\n" % (i))
	await ctx.send(text)

@bot.command(name="THICC", help="teehee")
async def on_message(ctx):
	log("CMD: thicc")
	log("From: " + str(ctx.guild))
	files = os.listdir("res/thicc/")
	await ctx.send(file=discord.File("res/thicc/" + files[random.randint(0, len(files)) - 1]))

@bot.command(name="blame", help="blames a random person")
async def on_message(ctx):
	log("CMD: blame")
	log("From: " + str(ctx.guild))
	await ctx.send(__options.blamegenerate([user for user in ctx.guild.members if user.presence.status != "offline"]))

@bot.command(name="votekick", help="[n/a] votes for them")
async def on_message(ctx, arg): #needs random chance, needs to get @'s, needs to disconnect someone
#needs to get a @'d person
#guild --> voice channels --> people

#TODO:
#match channel members to args
#make sure that the vc's are being iterated throught
#make sure args are correct, and sent a message if not
	log("CMD: votekick")
	for vc in ctx.guild.voice_channels:
		print("VC Found: " + str(vc)) #look for different attributes
		print("Members: " + str(vc.members)) #not recognizing members for some reason
		for member in vc.members:
			print("Member display:\t " + str(member.display_name))
			print("Member: \t" + str(member.id))
			print("Arg: \t" + str(ctx.args[1])[3:-1])
			print("Is Node: \t" + str(str(ctx.args[1])[3:-1] == str(member.id)))
			print("Is Author: \t" + str(ctx.author))
	await ctx.send(str(ctx.args[1]) + " was not an Imposter")
"""
else:
	person @'d + 1
	send (num / <needed>)
if <people in senders vc> / 2 + 1 < amountL:
	if person in vc
		if *chance*
			is imposter
		is not imposter
		kick
"""


bot.run(TOKEN)