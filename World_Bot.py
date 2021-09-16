import discord
import asyncio
import random

from discord import message



client = discord.Client()

token = "ODg3NjM1MDE4ODkyMDY2ODQ2.YUHAhw.lUqXyEtyxefxAIhzIvIIGnBVaSk"

@client.event
async def on_ready():
    
    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다')
    game = discord.Game('World')
    await client.change_presence(staus=discord.Status.online, activity=game)
    


@client.event
async def on_message(message) :
    if message.content == "필준이" :
        await message.channel.send("꿀꿀")
   
    elif message.content == "서준이" :
        await message.channel.send("섹스")

    elif message.content == "아람이" :
        await message.channel.send("김시....라고 할뻔")
    



#---------------------------------명령어-------------------------------------#
    if message.content == "!명령어" :
        await message.channel.send("필준이\n서준이\n아람이")
        





client.run(token)


