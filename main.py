import disnake, time, aeval, configparser, json, sqlite3
from disnake.ext import commands
config = configparser.ConfigParser()
config.read("config.ini")
token = config.get("Config", "Token")
developers = json.loads(config.get("Config", "Developers"))
bot = commands.Bot(command_prefix="$$")

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}')

@bot.command(aliases = ['eval', 'aeval', 'evaulate', 'выполнить', 'exec', 'execute'])
async def __eval(ctx, *, content):
    code = "\n".join(content.split("\n")[1:])[:-3] if content.startswith("```") and content.endswith("```") else content
    standart_args = { 
        "disnake": disnake,
        "commands": commands,
        "bot": bot,
        "ctx": ctx,
        "time": time,
        "config": config
    }
    if ctx.message.author.id in developers:
        await aeval.aeval(f"""{code}""", standart_args, {})
    else:
        await ctx.send("Вы не разработчик ")

bot.run(token)
