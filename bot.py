import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

hug=['ok','lol','stfu']

Client = discord.Client()
client = commands.Bot (command_prefix = "f!")

@client.event
async def on_ready():
    print ("Bot is ready!")

@client.event
async def on_message(message):
    if message.content.upper().startswith("!PING"):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong! :ping_pong: x3" % (userID))
    if message.content.upper().startswith("!PONG"):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Ping! :ping_pong: x3" % (userID))
    if message.content.upper().startswith("!SAY"):
        if message.author.id == "142764278582214656":
            args = message.content.split(" ")
            #!say Hey There
            #args [0] = !SAY
            #args [1] = Hey
            #args [2] = There
            #arhs [1:] = Hey There
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> You do not have permission to this command :disappointed_relieved:" % (userID))
    if message.content.upper().startswith("F!GENERAL"):
        if "237631849650847745" in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, ":ok_hand: ALL HEIL GENERAL FOX!:ok_hand: ")
        else:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> You do not have permission to this command :disappointed_relieved:" % (userID))
    if message.content.upper().startswith("F!FLIP"):
        hello=random.randint(1,2)
        if hello == 1:
            tails="Tails"
            userID=message.author.id
            await client.send_message(message.channel,"<@%s> You have gotten... "%(userID))
            await client.send_message(message.channel,(tails)+":dog:")
        else:
            heads="Heads"
            userID=message.author.id
            await client.send_message(message.channel,"<@%s> You have gotten... "%(userID))
            await client.send_message(message.channel,(heads)+":speaking_head:")
    if message.content.upper().startswith("F!HUG"):
        args = message.content.split(" ")
        userID = message.author.id
        connection=(str(" ".join(args[2:])))
        await client.send_message(message.channel,("<@%s> sent")%(userID),(connection))
        await client.send_message(message.channel,(random.choice(hug)))
        
    
client.run("Client ID")
