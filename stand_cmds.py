import disnake
import random as rnd
import time
from disnake.ext import commands
from main import collection_name_UserData
from stand_list import stands_lst
from stand_list import variations
# -------------------------------
class Standinfo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=["info_stand"])
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def stand_info(self, ctx, arg=1):
            try:
                channel = self.bot.get_channel(903703988225052762)
                await channel.send(embed=disnake.Embed(title='Вызвана команда: "stand_info"', description=f"`ID Автора`: {ctx.author.id}\n`Ник Автора`: {ctx.author}\n`ID Сервера`: {ctx.guild.id}\n`Название Сервера`: {ctx.guild}"))
            except Exception:
                pass
            if collection_name_UserData.count_documents({"_id": f"{ctx.author.id}"}) != 0:
                if arg < 1 or arg > 3:
                    return await ctx.send("Номером стенда может быть только число от 1 до 3.")
                else:
                    get_st = collection_name_UserData.find_one({"_id": f"{ctx.author.id}"})["stands"]
                    try:
                        get_st = get_st[arg-1]
                        await ctx.send(embed=disnake.Embed(title="Информация о стенде", description=f"Ваш стенд: **{stands_lst[get_st]}**", color=0xffff00))
                    except IndexError:
                        if arg == 2:
                            await ctx.send("Вы можете указать только 1 номер стенда!")
                        elif arg == 3:
                            await ctx.send("Вы можете указать только 1 или 2 номер стенда!")
            else:
                await ctx.send("У вас нет стенда используйте команду `get_stand` чтобы получить свой первый стенд!")
    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def stand_list(self, ctx):
        cnt = 0
        try:
            channel = self.bot.get_channel(903703988225052762)
            await channel.send(embed=disnake.Embed(title='Вызвана команда: "stand_list"', description=f"`ID Автора`: {ctx.author.id}\n`Ник Автора`: {ctx.author}\n`ID Сервера`: {ctx.guild.id}\n`Название Сервера`: {ctx.guild}"))
        except Exception:
            pass
        if collection_name_UserData.count_documents({"_id": f"{ctx.author.id}"}) != 0:
            lst = collection_name_UserData.find_one({"_id": f"{ctx.author.id}"})["stands"]
            await ctx.send(embed=disnake.Embed(title="Список стендов", description=f"\n".join([stands_lst[i] for i in lst]), color=0xffff00))
        else:
            return ctx.send("Вам нужно иметь хотя бы 1 стенд, используйте команду `get_stand`!")

    @commands.command()
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def stand_adventure(self, ctx):
        try:
            channel = self.bot.get_channel(903703988225052762)
            await channel.send(embed=disnake.Embed(title='Вызвана команда: "stand_adventure"', description=f"`ID Автора`: {ctx.author.id}\n`Ник Автора`: {ctx.author}\n`ID Сервера`: {ctx.guild.id}\n`Название Сервера`: {ctx.guild}"))
        except Exception:
            pass
        if collection_name_UserData.count_documents({"_id": f"{ctx.author.id}"}) != 0:
            get_num = rnd.randint(10, 75)
            random_num = [i for i in range(1, 4+1)]; random_num = rnd.choice(random_num)
            try:
                await ctx.send(embed=disnake.Embed(title="Приключения", description=f"{variations[str(random_num)].format(str(get_num))}", color=0xffff00))
                collection_name_UserData.update_one({"_id": f"{ctx.author.id}"}, {"$inc": {"money": get_num}})
            except Exception as ee:
                print("Error:", ee)
            collection_name_UserData.update_one({"_id": f"{ctx.author.id}"}, {"$inc": {"money": get_num}})
        else: # а теперь?
            await ctx.send("Вам нужен хотя бы 1 стенд чтобы использовать эту команду!\nпропишите команду `stand_get` чтобы получить стенд.")
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
             await ctx.send(f'{ctx.author.mention} Подождите {round(error.retry_after)} секунд перед использованием команды!')
# -------------------------------
def setup(bot):
    bot.add_cog(Standinfo(bot)) 
    print("Получилось загрузить ког инфо стенда!")