import disnake
import time
import datetime
from disnake.ext import commands
from main import collection_name_UserData
# ---------------------------------

class Oother(commands.Cog):

    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def one_zero_one_three(self, ctx):
        if time.strftime("%H:%M", time.localtime()) == "7:13" or time.strftime("%H:%M", time.localtime()) == "07:13":
            collection_name_UserData.update_one({"_id": f'{ctx.author.id}'}, {"$push": {"achievements":"🕙"}})
            return await ctx.send("Вы удачно получили достижение.")
        else:
            return await ctx.send(f"Промах!, сейчас <t:{int(datetime.datetime.now().timestamp())}:T>")
    @commands.command()
    async def beta_get(self, ctx):
        if collection_name_UserData.count_documents({"_id": f"{ctx.author.id}"}) != 0:
            collection_name_UserData.update_one({"_id": f'{ctx.author.id}'}, {"$set": {"money": 999999}})
            collection_name_UserData.update_one({"_id": f'{ctx.author.id}'}, {"$set": {"arrows": 999999}})
            collection_name_UserData.update_one({"_id": f'{ctx.author.id}'}, {"$set": {"discs": 999999}})
            return await ctx.send("Бета тестер, проверьте свой инвентарь через `stand_inv`!\nудачного тестирования бота.")
        else:
            return await ctx.send("Чтобы использовать эту команду, сначала получите стенд через `stand_get`!")
# ---------------------------------
def setup(bot):
    bot.add_cog(Oother(bot))
    print("Получилось загрузить ког остального!")
