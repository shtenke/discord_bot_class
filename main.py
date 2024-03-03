import discord
from discord.ext import commands
from random import choice
import requests 
from random import choice
from ai_logic import lepigion
import numpy as np
from keras import models 
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image, ImageOps

hello_help = '!hello'




intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            await attachment.save(f'./images/{file_name}')
            await ctx.send(lepigion(f'./images/{file_name}'))
    else:
        await ctx.send(f'Привет! Я бот {bot.user}!')






















bot.run("token")
