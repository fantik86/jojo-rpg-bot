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
    'events',
}
# -------------------------------
config = configparser.ConfigParser()
config.read("config.ini")
token = config.get("Config", "Token")
developers = json.loads(config.get("Config", "Developers"))
bot = commands.Bot(command_prefix=["$"], intents = disnake.Intents.all(), pass_context=True, chunk_guilds_at_startup=False)
bot.remove_command('help')
# -------------------------------
client = pymongo.MongoClient("mongodb+srv://Fantik86:fxD4QqGZ9lmUMMo5@cluster0.oidce.mongodb.net/DatabaseJoJoRPGBot?retryWrites=true&w=majority")
db = client['DatabaseJoJoRPGBot']
collection_name_UserData = db['UserData']
collection_name_TestData = db['TestData']
channel_id_logs = 903703988225052762
# ------------------------------- 
@bot.event
async def on_message(message):
    if message.content == f"<@!{896108733275439165}>":
        await message.channel.send(embed=disnake.Embed(title="Бонджорно!", description="Я тут, если что, вызывай меня через *$*.", color=0xFFFF00))
    await bot.process_commands(message)
@bot.event
async def on_guild_join(guild):
    try:
        channel = bot.get_channel(903703988225052762)
        joinguild = bot.get_guild(guild)
        await channel.send(embed=disnake.Embed(title='Бот был приглашён на сервер', description=f"`ID Сервера`: {joinguild.id}\n`Ник Автора`: {joinguild.owner_id}\n`Количество юзеров`: {joinguild.member_count}\n`Название Сервера`: {ctx.guild}"))
    except Exception as rrr: # пробуй
        print("Send error:", rrr)
    for chan in guild.text_channels: # так это ссылка на сервер чтобы текст отправляла
        if chan.permissions_for(guild.me).send_messages:
            return await chan.send(embed=disnake.Embed(title="Я Джорно Джованна, и у меня есть мечта!", description="Бон-джорно! Меня зовут Джорно Джованна, и у меня есть мечта.\nСпасибо что вы пригласили меня на сервер, я постараюсь представить себя в лучшей красе!\nЯ являюсь RPG ботом, где вы сможете получить свой стенд, развиваться и бороться с другими.\n\nКоманды - `$help`\nМой префикс - **$**", color=0xffff00))
@bot.event
async def on_guild_leave(guild):
    try:
        channel = bot.get_channel(903703988225052762)
        joinguild = bot.get_guild(guild)
        await channel.send(embed=disnake.Embed(title='Бот был удалён с сервера', description=f"`ID Сервера`: {joinguild.id}\n`Ник Автора`: {joinguild.owner_id}\n`Количество юзеров`: {joinguild.member_count}\n`Название Сервера`: {ctx.guild}"))
    except Exception as rrrr:
        print("Send error:", rrrr)
    return
    # тут будет форма удаления из бд
# -------------------------------
for cog in cooogs:
    bot.load_extension(cog)

bot.run(token)

