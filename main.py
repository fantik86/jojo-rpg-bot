import disnake
import configparser
import json
import pymongo
import os
import time
import asyncio
import random
# --------------------------------
from disnake.ext import commands, tasks

cooogs = {
    'starting',
    'utils',
    'generate_stand',
    'dev',
    'user_info',
    'stand_cmds',
    'events',
    'other'
}
# -------------------------------
config = configparser.ConfigParser()
config.read("config.ini")
token = config.get("Config", "Token")
developers = json.loads(config.get("Config", "Developers"))
bot = commands.Bot(command_prefix="$", 
                intents = disnake.Intents.all(),
                case_insensitive=True,
                status=disnake.Status.online, 
                activity=disnake.Game("65% | Beta"))
bot.remove_command('help')
# -------------------------------
client = pymongo.MongoClient("mongodb+srv://Fantik86:fxD4QqGZ9lmUMMo5@cluster0.oidce.mongodb.net/DatabaseJoJoRPGBot?retryWrites=true&w=majority")
db = client['DatabaseJoJoRPGBot']
collection_name_UserData = db['UserData']
collection_name_TestData = db['TestData']
channel_id_logs = 903703988225052762
# -------------------------------
for cog in cooogs:
    bot.load_extension(cog)

bot.run(token)

