import disnake
from disnake.ext import commands
# -------------------------------
class Userinfoo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def user_info(self, ctx, arg=None):
        pass

def setup(bot):
    bot.add_cog(Userinfoo(bot)) 
    print("Получилось загрузить ког информации юзера!")