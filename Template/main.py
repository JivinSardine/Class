#from typing import Any
import discord
#from discord.abc import _Undefined
#import requests
#import time
#import random
#import threading
#from threading import Timer
#from keep_alive import keep_alive #for 24/7


client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))





@client.event
async def on_message(message):
    print ("Client: " + str(client.user) + " Author: " + str(message.author) + " Message: " + message.content)
    if message.author == client.user:
        return
    
 

    if message.content == 'j.idle': 
      await message.channel.send("Spammer has started")#just an example
              
#keep_alive()  #for 24/7
client.run()#input bot id with ""