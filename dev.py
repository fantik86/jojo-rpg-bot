import disnake
from disnake.ext import commands
from main import collection_name_TestData, collection_name_UserData
from main import developers
import time
import random as rnd
from stand_list import stands_lst
# -------------------------------
class Devs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def test_cmd1(self,ctx):
        ...
    @commands.command()
    async def test_cmd2(self, ctx, arg=1):
        ...
    @commands.command(aliases=["reload", "rel"])
    async def reload_cog(self, ctx, extension):
        if ctx.author.id in developers:
            try:
                self.bot.reload_extension(extension)
                await ctx.send(f"Ког `{extension}` перезагружен")
            except Exception as eee:
                print("error cog:", eee)
        else:
            pass
# -------------------------------
def setup(bot):
    bot.add_cog(Devs(bot))
    print("Получилось загрузить ког разработчиков!")