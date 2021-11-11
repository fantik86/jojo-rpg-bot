import disnake
from disnake.ext import commands
import random as rnd
import time
from stand_list import stands_lst
from main import collection_name_UserData
# -----------------------------
def gett():
    numb = [str(rnd.randint(1, 102)) for _ in range(50)]
    numb = rnd.choice(numb)
    return numb


class Stando(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['get_stand'])
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def stand_get(self, ctx):
        try:
            channel = self.bot.get_channel(channel_id_logs)
            await channel.send(embed=disnake.Embed(title='Вызвана команда: "stand_get"', description=f"`ID Автора`: {ctx.author.id}\n`Ник Автора`: {ctx.author}\n`ID Сервера`: {ctx.guild.id}\n`Название Сервера`: {ctx.guild}")) #
        except Exception:
            pass
        if collection_name_UserData.count_documents({"_id": f"{ctx.author.id}"}) == 0:
            messageg = await ctx.send(embed=disnake.Embed(title="Использование стрелы", description="Вы берёте стрелу в руку, и протыкаете ею себя, вы чувствуете странное чувство...", color=0xffff00))
            time.sleep(6)
            await messageg.edit(embed=disnake.Embed(title="Использование стрелы", description=f'Ваш стенд это...', color=0xffff00))
            time.sleep(2)
            stand = gett()
            await messageg.edit(embed=disnake.Embed(title="Получение стенда", description=f'Вы получили стенд **{stands_lst[stand]}**!', color=0xffff00))
            collection_name_UserData.insert_one({"_id": f'{ctx.author.id}', "nickname": f'{ctx.author}', "stands": [], "arrows": 0, "money": 0, "explore_level": 1.00})
            collection_name_UserData.update_one({"_id": f'{ctx.author.id}'}, {"$push": {"stands":f"{stand}"}})
        elif collection_name_UserData.count_documents({"_id": f"{ctx.author.id}"}) != 0 and len(collection_name_UserData.find_one({"_id": f'{ctx.author.id}'})["stands"]) == 3:
            await ctx.send("У вас и так достаточное количество стендов!")
        elif (
            collection_name_UserData.count_documents({"_id": f"{ctx.author.id}"}) != 0 and 
            len(collection_name_UserData.find_one({"_id": f'{ctx.author.id}'})["stands"]) != 3 and
            collection_name_UserData.find_one({"_id": f'{ctx.author.id}'})["arrows"] <= 0):
            await ctx.send("У вас нету стрелы чтобы получить новый стенд.")
        elif (
            collection_name_UserData.count_documents({"_id": f"{ctx.author.id}"}) != 0 and 
            not len(collection_name_UserData.find_one({"_id": f'{ctx.author.id}'})["stands"]) == 3 and
            collection_name_UserData.find_one({"_id": f'{ctx.author.id}'})["arrows"] > 0):
            messageg = await ctx.send(embed=disnake.Embed(title="Использование стрелы", description="Вы берёте стрелу в руку, и протыкаете ею себя, вы чувствуете странное чувство...", color=0xffff00))
            time.sleep(6)
            await messageg.edit(embed=disnake.Embed(title="Использование стрелы", description=f'Ваш стенд это...', color=0xffff00))
            time.sleep(2)
            stand = gett()
            await messageg.edit(embed=disnake.Embed(title="Получение стенда", description=f'Вы получили стенд **{stands_lst[stand]}**!', color=0xffff00))
            collection_name_UserData.update_one({"_id": f'{ctx.author.id}'}, {"$push": {"stands":f"{stand}"}})
            collection_name_UserData.update_one({"_id": f'{ctx.author.id}'}, {"$inc": {"arrows":-1}})
        else:
            await ctx.send("Неизвестная причина, сообщите разработчикам!")
# -------------------------------  
def setup(bot):
    bot.add_cog(Stando(bot))
    print("Получилось загрузить генерацию стендов!")
