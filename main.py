import disnake
import configparser
import json
import pymongo
import os
import time
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
}
# --------------------------------
config = configparser.ConfigParser()
config.read("config.ini")
token = config.get("Config", "Token")
developers = json.loads(config.get("Config", "Developers"))
bot = commands.Bot(command_prefix=["$"], intents = disnake.Intents.all(), pass_context=True)
bot.remove_command('help')
# -------------------------------
client = pymongo.MongoClient("mongodb+srv://Fantik86:fxD4QqGZ9lmUMMo5@cluster0.oidce.mongodb.net/DatabaseJoJoRPGBot?retryWrites=true&w=majority")
db = client['DatabaseJoJoRPGBot']
collection_name_UserData = db['UserData']
collection_name_TestData = db['TestData']
# ------------------------------- 
@bot.event
async def on_message(message):
    if message.content == f"<@!{896108733275439165}>":
        await message.channel.send(embed=disnake.Embed(title="Бонджорно!", description="Я тут, если что, вызывай меня через *$*.", color=0xFFFF00))
    await bot.process_commands(message)
@bot.event
async def on_guild_join(guild):
    counter = 0
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            counter += 1
            await channel.send(embed=disnake.Embed(title="Я Джорно Джованна, и у меня есть мечта!", description="Бон-джорно! Меня зовут Джорно Джованна, и у меня есть мечта.\nСпасибо что вы пригласили меня на сервер, я постараюсь представить себя в лучшей красе!\nЯ являюсь RPG ботом, где вы сможете получить свой стенд, развиваться и бороться с другими.\n\nКоманды - `$help`\nМой префикс - **$**", color=0xffff00))
        break
    if counter == 1: pass
# ----------------------------------
for cog in cooogs:
    bot.load_extension(cog)

bot.run(token)

