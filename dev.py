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
        if ctx.author.id in developers:
            try:
                channel = self.bot.get_channel(903703988225052762)
                await channel.send(embed=disnake.Embed(title='Вызвана команда: "stand_inv"', description=f"`ID Автора`: {ctx.author.id}\n`Ник Автора`: {ctx.author}\n`ID Сервера`: {ctx.guild.id}\n`Название Сервера`: {ctx.guild}"))
            except Exception:
                pass
            if collection_name_UserData.count_documents({"_id": f"{ctx.author.id}"}) != 0:
                arrows_len = collection_name_UserData.find_one({"_id": f"{ctx.author.id}"})["arrows"]
                money_len = collection_name_UserData.find_one({"_id": f"{ctx.author.id}"})["money"]
                await ctx.send(embed=disnake.Embed(title="Инвентарь", description=f"Количество стрел:{arrows_len}\nБаланс: {money_len}$"))
            else:
                await ctx.send("У вас нет стенда, используйте команду `get_stand` чтобы получить свой первый стенд!")
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
# ------------------------------
def setup(bot):
    bot.add_cog(Devs(bot))
    print("Получилось загрузить ког разработчиков!")
