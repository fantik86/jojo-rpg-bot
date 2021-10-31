import disnake
from disnake.ext import commands
# -------------------------------
class Userinfoo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Userinfoo(bot)) 
    print("Получилось загрузить ког информации юзера!")