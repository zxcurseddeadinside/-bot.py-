import discord
from discord.ext import commands
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord import member
from discord.utils import get
from discord.ext import slash
import random
from discord.ext import commands, tasks
import asyncio
from asyncio import sleep
from time import *
import qrcode
import json

from dislash import Option, OptionType
from dislash import InteractionClient, Option, OptionType
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)
from dislash import *
slash = InteractionClient(bot)


async def logger(id46):
    logs91 = bot.get_channel(1058925038864187482)
    await logs91.send(id46)




async def on_ready():   
    print("БОТ ЗАПУЩЕН И ГОТОВ ПРИНИМАТЬ ЗАПРОСЫ")
    

@slash.command(
    name="рандомка", # Defaults to function name
    description="даёт случайное число от 0 до 100",
    guild_ids="")
async def рандомку(inter):
    randomnumb = random.randint(0, 100)
    mess = await inter.reply('рандомка от 0 до сотки подана через')
    sleep(1)
    await mess.edit("3")
    sleep(1)
    await mess.edit("2")
    sleep(1)
    await mess.edit("1!")
    sleep(1)
    print("someone used randomnumb the result is", randomnumb)
    await mess.edit(f"получилось {randomnumb}!")



bot.run('MTE4MDg5NTg2Nzc1MDg1ODg3NA.GtJZ_t.oe2toj4F0QXiCkCf8mpIkT7N94utFStJogm0fY')










