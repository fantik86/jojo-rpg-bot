import disnake
import random as rnd
import time
from disnake.ext import commands
from main import collection_name_UserData
from stand_list import stands_lst
from stand_list import variations
from stand_list import explore_levels
# -------------------------------
embedshop=disnake.Embed(title="Магазин", description='1. Стрела - 800$\n2. Диск[сброс стенда] - 100$\n\nЧтобы приобрести вещь пропишите `stand_shop buy`', color=0xffff00)
embedshop.set_footer(text="Пропишите stand_inv чтобы узнать баланс!")
embeds=disnake.Embed(title="Список стендов", description="У вас нету ни одного стенда!", color=0xffff00)
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
        embeds.set_footer(text=f"Чтобы получить стенд, напишите $stand_get", icon_url=f"{ctx.message.author.avatar}")
        cnt = 0
        try:
            channel = self.bot.get_channel(903703988225052762)
            await channel.send(embed=disnake.Embed(title='Вызвана команда: "stand_list"', description=f"`ID Автора`: {ctx.author.id}\n`Ник Автора`: {ctx.author}\n`ID Сервера`: {ctx.guild.id}\n`Название Сервера`: {ctx.guild}"))
        except Exception:
            pass
        if collection_name_UserData.count_documents({"_id": f"{ctx.author.id}"}) != 0:
            lst = collection_name_UserData.find_one({"_id": f"{ctx.author.id}"})["stands"]
            if len(lst) != 0:
                await ctx.send(embed=disnake.Embed(title="Список стендов", description=f"\n".join([stands_lst[i] for i in lst]), color=0xffff00))
            else:
                return await ctx.send(embed=embeds)
        else:
            await ctx.send("Вам нужно иметь хотя бы 1 стенд, используйте команду `get_stand`!")

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
                if int(get_num) == 75:
                    collection_name_UserData.update_one({"_id": f'{ctx.author.id}'}, {"$push": {"achievements":"🎰"}})
            except Exception as ee:
                print("Error:", ee)
        else: # а теперь?
            await ctx.send("Вам нужен хотя бы 1 стенд чтобы использовать эту команду!\nпропишите команду `stand_get` чтобы получить стенд.")
    @commands.command(aliases=["stand_inventory"])
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def stand_inv(self, ctx):
        try:
            channel = self.bot.get_channel(903703988225052762)
            await channel.send(embed=disnake.Embed(title='Вызвана команда: "stand_inv"', description=f"`ID Автора`: {ctx.author.id}\n`Ник Автора`: {ctx.author}\n`ID Сервера`: {ctx.guild.id}\n`Название Сервера`: {ctx.guild}"))
        except Exception:
            pass 
        if collection_name_UserData.count_documents({"_id": f"{ctx.author.id}"}) != 0:
            arrows_len = collection_name_UserData.find_one({"_id": f"{ctx.author.id}"})["arrows"] 
            money_len = collection_name_UserData.find_one({"_id": f"{ctx.author.id}"})["money"]
            disc_len = collection_name_UserData.find_one({"_id": f"{ctx.author.id}"})["discs"]
            await ctx.send(embed=disnake.Embed(title=f"Инвентарь игрока {ctx.author}", description=f"**Баланс:** {money_len}$\n**Стрелы:** {arrows_len}шт.\n**Диски**: {disc_len}шт.", color=0xffff00))
        else:
            await ctx.send("У вас нет стенда, используйте команду `get_stand` чтобы получить свой первый стенд!")
    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def stand_shop(self, ctx, arg=None):
        try:
            channel = self.bot.get_channel(903703988225052762)
            await channel.send(embed=disnake.Embed(title='Вызвана команда: "stand_shop"', description=f"`ID Автора`: {ctx.author.id}\n`Ник Автора`: {ctx.author}\n`ID Сервера`: {ctx.guild.id}\n`Название Сервера`: {ctx.guild}"))
        except Exception:
            pass
        if arg is None:
            await ctx.send(embed=embedshop)
        elif arg.lower() == 'buy':
            await ctx.send("Отправьте **1** если хотите купить стрелу;\nОтправьте **2** если хотите купить диск сброса стенда")
            player_choice = await self.bot.wait_for('message', check=lambda message: "1" if message.content == "1" else "2")
            msgg1 = player_choice.content
            if msgg1 == '1' and collection_name_UserData.count_documents({"_id": f"{ctx.author.id}"}) != 0:
                if not collection_name_UserData.find_one({"_id": f"{ctx.author.id}"})["money"] - 800 < 0:
                    await ctx.send("Стрела была успешно куплена и находится у вас, проверьте командой `stand_inv`.")
                    collection_name_UserData.update_one({"_id": f'{ctx.author.id}'}, {"$inc": {"money": -800}})
                    collection_name_UserData.update_one({"_id": f'{ctx.author.id}'}, {"$inc": {"arrows": 1}})
                else:
                    return await ctx.send("Недостаточно денег для покупки!")
            elif msgg1 == '2' and collection_name_UserData.find_one({"_id": f'{ctx.author.id}'}) != 0:
                if not collection_name_UserData.find_one({"_id": f"{ctx.author.id}"})["money"] - 100 < 0:
                    await ctx.send("Диск был успешно куплен и находится у вас, проверьте командой `stand_inv`.")
                    collection_name_UserData.update_one({"_id": f'{ctx.author.id}'}, {"$inc": {"money": -100}})
                    collection_name_UserData.update_one({"_id": f'{ctx.author.id}'}, {"$inc": {"discs": 1}})
                else:
                    return await ctx.send("Недостаточно денег для покупки!")
            else:
                return await ctx.send("У вас нету инвентаря, чтобы получить его вам нужен стенд\nЧтобы получить стенд пропишите `stand_get`.")
        else:
            await ctx.send("Введено неверное значение.")
            
    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user) 
    async def stand_reset(self, ctx, stndt: int):
        try:
            channel = self.bot.get_channel(channel_id_logs)
            await channel.send(embed=disnake.Embed(title='Вызвана команда: "stand_reset"', description=f"`ID Автора`: {ctx.author.id}\n`Ник Автора`: {ctx.author}\n`ID Сервера`: {ctx.guild.id}\n`Название Сервера`: {ctx.guild}"))
        except Exception:
            pass
        if collection_name_UserData.count_documents({"_id": f"{ctx.author.id}"}) != 0:
            discs = collection_name_UserData.find_one({"_id": f"{ctx.author.id}"})["discs"]
            if stndt > 3 or stndt < 1:
                return await ctx.send("Вы указали неверный номер стенда!")
            elif discs < 1: # неправильно сделал кста, это надо проверять если всё нормально в верхнем условии, то есть это вниз в else 
                return await ctx.send("У вас нет дисков! Купите их в магазине, введя команду `$stand_shop`")
            else:
                stand_get = collection_name_UserData.find_one({"_id": f"{ctx.author.id}"})["stands"]
                try:
                    del stand_get[stndt-1]
                    collection_name_UserData.update_one({"_id": f"{ctx.author.id}"}, {"$set": {"stands": stand_get}})
                    await ctx.send("Ваш стенд был успешно сброшен.")
                except IndexError:
                    if stndt == 2:
                        await ctx.send("Вы можете указать только 1 номер стенда!")
                    elif stndt == 3:
                        await ctx.send("Вы можете указать только 1 или 2 номер стенда!")
        else:
            return await ctx.send("Чтобы использовать данную команду вам нужен хотя бы 1 стенд\nЧтобы получить его используйте `stand_get`")
# -------------------------------
def setup(bot):
    bot.add_cog(Standinfo(bot)) 
    print("Получилось загрузить ког инфо стенда!")