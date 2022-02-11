import disnake
import datetime
from disnake.ext import commands
from main import collection_name_UserData
from stand_list import stands_lst, explore_levels
from main import developers
# -------------------------------
date_format = "%a, %b %d, %Y @ %I:%M %p" 
embed2 = disnake.Embed(title="Информация о юзере {}", description=f"", color=0xffff00)
# -------------------------------
class Userinfoo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def user_info(self, ctx, *, arg: disnake.Member = None):
        """
        if arg is None:
            userr = ctx.author
        """
        if ctx.author.id not in developers and arg is not None and arg.id in developers and arg:
            embed0=disnake.Embed(title="?????", color=0x800080)
            try:
                embed0.set_image(url="https://thumbs.gfycat.com/AngryHelplessBluet-max-1mb.gif")
            except Exception as tt:
                print(tt)
            return await ctx.send(embed=embed0)
        elif collection_name_UserData.count_documents({"_id": f"{ctx.author.id}"}) == 0 and arg is None:
            try:
                embed2 = disnake.Embed(title=f"Информация о {ctx.message.author}", description=f"**Дата регистрации**:\n<t:{int(ctx.author.created_at.timestamp())}:F>\n**Дата захода на сервер**:\n <t:{int(ctx.author.joined_at.timestamp())}:F>\n**ID Пользователя**:\n{ctx.message.author.id}", color=0xffff00)
                embed2.set_thumbnail(url=f"{ctx.message.author.display_avatar}")
                embed2.add_field(name="Статус:", value="Не зарегистрирован в боте.")
                await ctx.send(embed=embed2)
            except Exception as r:
                print(r)
        elif collection_name_UserData.count_documents({"_id": f"{ctx.author.id}"}) == 1 and arg is None:
            try:
                embed3 = disnake.Embed(title=f"Информация о {ctx.author}", description=f"**Дата регистрации аккаунта**:\n<t:{int(ctx.author.created_at.timestamp())}:F>\n**Дата захода на сервер**:\n <t:{int(ctx.author.joined_at.timestamp())}:F>\n**ID Пользователя**:\n{ctx.author.id}", color=0xffff00)
                try:
                    embed3.set_thumbnail(url=ctx.author.display_avatar)
                except Exception as r:
                    print(r)
                get_ac1 = collection_name_UserData.find_one({"_id": f"{ctx.author.id}"})["achievements"]
                embed3.add_field(name="Достижения:", value=("".join(get_ac1) if len(get_ac1) != 0 else "Нету"))
                levels = collection_name_UserData.find_one({"_id": f"{ctx.author.id}"})["explore_level"]
                embed3.add_field(name="На локации:", value=f"{explore_levels[levels]}")
                await ctx.send(embed=embed3)
            except Exception as r:
                print(r)
        elif ctx.author.id in developers or ctx.author.id not in developers and arg is None and collection_name_UserData.count_documents({"_id": f"{ctx.author.id}"}) == 1:
            try:
                embed3 = disnake.Embed(title=f"Информация о {arg}", description=f"**Дата регистрации аккаунта**:\n<t:{int(arg.created_at.timestamp())}:F>\n**Дата захода на сервер**:\n <t:{int(arg.joined_at.timestamp())}:F>\n**ID Пользователя**:\n{arg.id}", color=0xffff00)
                try:
                    embed3.set_thumbnail(url=arg.display_avatar)
                except Exception as r:
                    print(r)
                get_ac1 = collection_name_UserData.find_one({"_id": f"{arg.id}"})["achievements"]
                embed3.add_field(name="Достижения:", value=("".join(get_ac1) if len(get_ac1) != 0 else "Нету"))
                levels = collection_name_UserData.find_one({"_id": f"{ctx.author.id}"})["explore_level"]
                embed3.add_field(name="На локации:", value=f"{explore_levels[levels]}")
                await ctx.send(embed=embed3)
            except Exception as r:
                print(r)
        elif ctx.author.id in developers or ctx.author.id not in developers and arg is not None and collection_name_UserData.count_documents({"_id": f"{arg.id}"}) == 1:
            try:
                embed3 = disnake.Embed(title=f"Информация о {arg}", description=f"**Дата регистрации аккаунта**:\n<t:{int(arg.created_at.timestamp())}:F>\n**Дата захода на сервер**:\n <t:{int(arg.joined_at.timestamp())}:F>\n**ID Пользователя**:\n{arg.id}", color=0xffff00)
                try:
                    embed3.set_thumbnail(url=arg.display_avatar)
                except Exception as r:
                    print(r)
                get_ac1 = collection_name_UserData.find_one({"_id": f"{arg.id}"})["achievements"]
                embed3.add_field(name="Достижения:", value=("".join(get_ac1) if len(get_ac1) != 0 else "Нету"))
                levels = collection_name_UserData.find_one({"_id": f"{ctx.author.id}"})["explore_level"]
                embed3.add_field(name="На локации:", value=f"{explore_levels[levels]}")
                await ctx.send(embed=embed3)
            except Exception as r:
                print(r)
        elif ctx.author.id in developers or ctx.author.id not in developers and arg is not None and collection_name_UserData.count_documents({"_id": f"{arg.id}"}) == 0:
            try:
                embed4 = disnake.Embed(title=f"Ошибка!", description=f"Данный пользователь не зарегестрирован в боте!", color=0xffff00)
                try:
                    embed3.set_thumbnail(url=arg.display_avatar)
                except Exception as r:
                    print(r)
                await ctx.send(embed=embed4)
            except Exception as r:
                print(r)

def setup(bot):
    bot.add_cog(Userinfoo(bot)) 
    print("Получилось загрузить ког информации юзера!")
