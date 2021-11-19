from typing import Any
import discord
from discord.abc import _Undefined
import requests
import time
import random
import threading
from threading import Timer
from keep_alive import keep_alive 

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))





@client.event
async def on_message(message):
    print ("Client: " + str(client.user) + " Author: " + str(message.author) + " Message: " + message.content)
    if message.author == client.user:
        return
    
 

    if message.content == 'pls start': 
      await message.channel.send("Berry has started")#just an example

    if message.content == 'b.owner': 
      await message.channel.send("Emperor RBK is the owner of this server.")#just an example 

    if message.content == 'b.serverbuilder': 
      await message.channel.send("Anthony07 is the server builder.")#just an example
      
    if message.content == 'b.administrator': 
      await message.channel.send("Beryl is the administrator.")#just an example     
              
keep_alive()  
client.run("")#input bot id with ""