import disnake
from disnake.ext import commands
from main import collection_name_TestData, collection_name_UserData
from main import developers
import time
import random as rnd
from stand_list import stands_lst
from main import channel_id_logs
from stand_list import variations
from stand_list import explore_levels
# -------------------------------
class Devs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 8, commands.BucketType.user) # изменить на большее
    async def test_cmd2(self, ctx): # stand_explore
        if ctx.author.id in developers:
            try:
                channel = self.bot.get_channel(channel_id_logs)
                await channel.send(embed=disnake.Embed(title='Вызвана команда: "stand_explore"', description=f"`ID Автора`: {ctx.author.id}\n`Ник Автора`: {ctx.author}\n`ID Сервера`: {ctx.guild.id}\n`Название Сервера`: {ctx.guild}"))
            except Exception as eeeeee:
                print(eeeeee)
            if not collection_name_UserData.count_documents({"_id": f"{ctx.author.id}"}) == 0:
                try:
                    if collection_name_UserData.find_one({"_id": ctx.author.id})["explore_level"] == 1.70:
                        return await ctx.send("Вы уже изучили все места, вы больше не можете использовать данную команду.")
                    else:
                        user_lvl = collection_name_UserData.find_one({"_id": ctx.author.id})["explore_level"]
                        if int(rnd.randint(1, 50)) in [rnd.randint(1, 50) for _ in range(int(10-user_lvl))]:
                            await ctx.send(embed=disnake.Embed(title=f"Изучение места: {explore_levels[user_lvl]}", description="Вы удачно изучили данное место, вас множитель денег в команда `stand_adventure` умножен на 0.05!"))
                            collection_name_UserData.update_one({"_id": f"{ctx.author.id}"}, {"$inc": {"explore_level": 0.05}})
                        else:
                            mon = rnd.randint(20, 50)
                            await ctx.send(embed=disnake.Embed(title=f"Изучение места: {explore_levels[user_lvl]}", description=f"Вы изучили данное место, и безуспешно, в сочуствие вам с неба выпадает {mon}$"))
                            collection_name_UserData.update_one({"_id": f"{ctx.author.id}"}, {"$inc": {"money": mon}})
                except Exception as errr:
                    print(errr)
                    await ctx.send("Произошла какая-то ошибка! Обратитесь к разработчику.")

            else:
                await ctx.send("Чтобы использовать данную команду, вы должны иметь хотя бы 1 стенд!\nДля этого пропишите команду `get_stand`.")

    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user) 
    async def test_cmd3(self, ctx, stndt: int): # stand reset
        try:
            channel = self.bot.get_channel(channel_id_logs)
            await channel.send(embed=disnake.Embed(title='Вызвана команда: "stand_reset"', description=f"`ID Автора`: {ctx.author.id}\n`Ник Автора`: {ctx.author}\n`ID Сервера`: {ctx.guild.id}\n`Название Сервера`: {ctx.guild}"))
        except Exception:
            pass
        if collection_name_UserData.count_documents({"_id": f"{ctx.author.id}"}) != 0:
            if stndt > 3 or stndt < 1:
                return await ctx.send("Вы не указали верный номер стенда!")
            else:
                stand_get = collection_name_UserData.find_one({"_id": f"{ctx.author.id}"})["stands"]
                try:
                    del stand_get[stndt-1]
                    collection_name_UserData.update_one({"_id": f"{ctx.author.id}"}, {"$set": {"stands": stand_get}})
                    await ctx.send("Ваш стенд успешно был сброшен.")
                except IndexError:
                    if stndt == 2:
                        await ctx.send("Вы можете указать только 1 номер стенда!")
                    elif stndt == 3:
                        await ctx.send("Вы можете указать только 1 или 2 номер стенда!")
        else:
            return await ctx.send("Чтобы использовать данную команду вам нужен хотя бы 1 стенд\nЧтобы получить его используйте `stand_get`")

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
    @commands.command()
    async def update_db(self, ctx, arg0, arg1: disnake.Member, arg2, arg3):
        if ctx.author.id in developers:
            try:
                if arg0 == "1":
                    collection_name_UserData.update_one({"_id": f'{arg1.id}'}, {"$set": {arg2:int(arg3)}})
                    await ctx.send("Success!")
                elif arg0 == "2":
                    collection_name_UserData.update_one({"_id": f'{arg1.id}'}, {"$set": {arg2:str(arg3)}})
                    await ctx.send("Success!")
                elif arg0 == "3":
                    collection_name_UserData.update_one({"_id": f'{arg1.id}'}, {"$push": {arg2:str(arg3)}})
                    await ctx.send("Success!")
            except Exception as rr:
                print(rr)
    @commands.command()
    async def delete_db(self, ctx, arg: disnake.Member):
        if ctx.author.id in developers:
            try:
                collection_name_UserData.delete_one({"_id": f'{arg.id}'})
                await ctx.send("Success!")
            except Exception as errorr:
                print(errorr)
    @commands.command()
    async def say(self, ctx, *, arg):
        if ctx.author.id in developers:
            await ctx.message.delete()
            await ctx.send(arg)
        else:
            await ctx.send("Вы не разработчик!")
# -------------------------------
def setup(bot):
    bot.add_cog(Devs(bot))
    print("Получилось загрузить ког разработчиков!")