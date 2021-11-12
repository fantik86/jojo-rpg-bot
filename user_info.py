import disnake
import datetime
from disnake.ext import commands
from main import collection_name_UserData
from stand_list import stands_lst
from main import developers
# -------------------------------
date_format = "%a, %b %d, %Y @ %I:%M %p" 
embed2 = disnake.Embed(title="Информация о юзере {}", description=f"", color=0xffff00)
# -------------------------------
class Userinfoo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def user_info(self, ctx):
        if ctx.author.id in developers:
            embed0=disnake.Embed(title="?????", color=0x800080)
            try:
                embed0.set_image(url="https://thumbs.gfycat.com/AngryHelplessBluet-max-1mb.gif")
            except Exception as tt:
                print(tt)
            return await ctx.send(embed=embed0)
        else:
            if collection_name_UserData.count_documents({"_id": f"{ctx.author.id}"}) != 0:
                try:
                    embed1 = disnake.Embed(title=f"Информация о {ctx.message.author}", description=f"**Дата регистрации**:\n<t:{int(ctx.author.created_at.timestamp())}:F>\n**Дата захода на сервер**:\n <t:{int(ctx.author.joined_at.timestamp())}:F>\n**ID Пользователя**:\n{ctx.message.author.id}", color=0xffff00)
                    embed1.set_thumbnail(url=f"{ctx.message.author.avatar}")
                    get_ac = collection_name_UserData.find_one({"_id": f"{ctx.author.id}"})["achievements"]
                    embed1.add_field(name="Достижения:", value=("".join(get_ac) if len(get_ac) != 0 else "Нету"))
                    await ctx.send(embed=embed1)
                except Exception as r:
                    print(r)
            else: # го
                try:
                    embed2 = disnake.Embed(title=f"Информация о {ctx.message.author}", description=f"**Дата регистрации**:\n<t:{int(ctx.author.created_at.timestamp())}:F>\n**Дата захода на сервер**:\n <t:{int(ctx.author.joined_at.timestamp())}:F>\n**ID Пользователя**:\n{ctx.message.author.id}", color=0xffff00)
                    embed2.set_thumbnail(url=f"{ctx.message.author.avatar}")
                    embed2.add_field(name="Статус:", value="Не зарегистрирован в боте.")
                    await ctx.send(embed=embed2)
                except Exception as r:
                    print(r)

def setup(bot):
    bot.add_cog(Userinfoo(bot)) 
    print("Получилось загрузить ког информации юзера!")