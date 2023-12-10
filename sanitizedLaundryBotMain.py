# bot.py
import os
import time
import discord
import nacl
import asyncio
import ffmpeg
import random
import sys
def toSec(hours,mins,secs):
    sec=hours*3600 +mins*60 +secs
    print (sec)
    return sec
compliments = [Your phrases go here]
soundsDict={"yoursoundsgohere":"yoursoundsgohere.mp3"}
wisdom=[Your phrases go here]
pickup=[Your phrases go here]
intents = discord.Intents().all()
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    channel = client.get_channel(Put Channel you want to send messages to here) 
    await channel.send("On startup message")
@client.event
async def on_message(message):
    channel = client.get_channel(Put Channel you want to send messages to here) 
    if message.author == client.user:
        return
    if message.content.lower().startswith(('!laundry','@laundry','/laundry')):
        x=message.content.split (" ")
        try:
            hours= x[1]
            mins=x[2]
            sec=x[3]
        except:
            await channel.send("Not valid")
            return
        if (not hours.isdigit() or not mins.isdigit() or not sec.isdigit()):
            await channel.send("Not valid")
            return
        secs=toSec(int(hours),int(mins),int(sec))
        await channel.send("Laundry timer started")
        while True:
            await asyncio.sleep(5)
            secs -= 5
            if (secs<=0):
                await channel.send(f"{message.author.mention} Your laundry is done!")
                voice=client.get_channel(Put The ID of the voice channel you want to connect to here)
                vc=await voice.connect()
                vc.play(discord.FFmpegPCMAudio("laundry.mp3"))
                while (vc.is_playing()):
                    await asyncio.sleep(0.1)
                await vc.disconnect()
                break
    if message.content.lower().startswith(('!food','@food','/food')):
        x=message.content.split (" ")
        try:
            hours= x[1]
            mins=x[2]
            sec=x[3]
        except:
            await channel.send("Not valid")
            return
        if (not hours.isdigit() or not mins.isdigit() or not sec.isdigit()):
            await channel.send("Not valid")
            return
        secs=toSec(int(hours),int(mins),int(sec))
        await channel.send("Food timer started")
        while True:
            await asyncio.sleep(5)
            secs -= 5
            if (secs<=0):
                await channel.send(f"{message.author.mention} Your Food is done!")
                voice=client.get_channel(Put The ID of the voice channel you want to connect to here)
                vc=await voice.connect()
                vc.play(discord.FFmpegPCMAudio("food.mp3"))
                while (vc.is_playing()):
                    await asyncio.sleep(0.1)
                await vc.disconnect()
                break
    if message.content.lower().startswith(('!compliment','@compliment','/compliment')):
        comp=random.choice(compliments)
        await channel.send(comp)
    if message.content.lower().startswith(('!wisdom', '@wisdom','/wisdom')):
        wis=random.choice(wisdom)
        await channel.send(wis)
    if message.content.lower().startswith(('!pickup', '@pickup','/pickup')):
        pick=random.choice(pickup)
        await channel.send(pick)
    if message.content.lower().startswith('<@'):
        if (message.author.display_name.startswith('sound')):
            x=message.author.display_name.split (" ")
            try:
                sound=x[1].lower()
            except:
                return
            if (not sound in soundsDict):
                return
            voice=client.get_channel(Put The ID of the voice channel you want to connect to here)
            vc=await voice.connect()
            print (sound)
            vc.play(discord.FFmpegPCMAudio(soundsDict[sound]))
            while (vc.is_playing()):
                    await asyncio.sleep(0.1)
            await vc.disconnect()
    if message.content.lower().startswith(('!random', '@random','/random')):
        key="random"
        while key=="random":
            key,value=random.choice(list(soundsDict.items()))
        voice=client.get_channel(Put The ID of the voice channel you want to connect to here)
        vc=await voice.connect()
        vc.play(discord.FFmpegPCMAudio(soundsDict[key]))
        while (vc.is_playing()):
                await asyncio.sleep(0.1)
        await vc.disconnect()
    if message.content.lower().startswith(('!sound', '@sound','/sound')):
        x=message.content.split (" ")
        try:
            sound=x[1].lower()
        except:
            await channel.send("Not valid")
            return
        if (not sound in soundsDict):
            await channel.send("Not valid")
            return
        voice=client.get_channel(Put The ID of the voice channel you want to connect to here)
        vc=await voice.connect()
        vc.play(discord.FFmpegPCMAudio(soundsDict[sound]))
        while (vc.is_playing()):
                await asyncio.sleep(0.1)
        await vc.disconnect()
    if message.content.lower().startswith(('!goodnight', '@goodnight','/goodnight')):
        await channel.send("Goodnight!")
        sys.exit()
    if message.content.lower().startswith(('!list', '@list','/list')):
        await channel.send(List your available sounds and commands here)
client.run(Put Key Here)
