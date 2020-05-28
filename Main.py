from chatterbot import ChatBot
from subprocess import call
import sys
import os
import requests
import asyncio
import discord
import threading

TOKEN = ('token goes here')

from discord.ext import commands

client = discord.Client()

                                   
#Creates new ChatBot class named "bob"
bot = ChatBot('bob')


bot = ChatBot(
  'bob',
  storage_adapter='chatterbot.storage.SQLStorageAdapter',
  logic_adapters=[
   {
    'import_path': 'nameadapter.Adapter1'
   },

   {
    'import_path': 'nameadapter.Adapter2'
   },

   {
    'import_path': 'nameadapter.Adapter3'
   },

   {
    'import_path': 'nameadapter.Adapter4'
   },

    'chatterbot.logic.BestMatch',

   {
    'import_path': 'chatterbot.logic.BestMatch',
    'default_response': "I'm not sure I understand",
    'maximum_similarity_threshold': 0.90
   }
   
  ],
  database_uri='sqlite:///db.sqlite3'
 )


@client.event
async def on_ready():
    print(f'{client.user.name} is online')
       
      


@client.event
async def on_message(message):
    if message.author == client.user:
            return
        
    if message.content.startswith("."):
        messy = str(message.content)
        lost = messy.replace('.', '')
        last = lost.lower()

        bot_input = bot.get_response(last)
        response = (bot_input)
        await message.channel.send(response)
       

client.run(TOKEN)


   
      



 


