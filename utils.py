import disnake
from disnake.ext import commands
# --------------------------
channel_id_logs = 903703988225052762
# --------------------------
embedhelp=disnake.Embed(title="Команды бота", description="`Префикс бота:` $\n\n`other` - Другие команды", color=0xFFFF00)
# \n)
embedhelp.set_thumbnail(url="https://cdn.discordapp.com/app-icons/896108733275439165/d789e7dc810989b6e476f6f815296d1c.png?size=256")
# -------------------------- 
embedinformation=disnake.Embed(title="Информация о боте", color=0xffff00)
embedinformation.set_thumbnail(url="https://media.discordapp.net/attachments/896109675873984543/903350823365537802/0fd5e79f1cd36c4045b9b822faae409c4d64b66c.png")
embedinformation.add_field(name="Бот написан на:", value="Python3", inline=True)
embedinformation.add_field(name="Версия бота:", value="0.5 Alpha", inline=True)
embedinformation.add_field(name='Разработчики:', value='ViZus#9667\nФантик#1111', inline=False)
# ------------------------------- 
class Utilits(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
# -------------------------- 
    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def ping(self, ctx):
        await ctx.send(f'Мой пинг... составляет {round(self.bot.latency * 1000)} милли-секунд.')
        try:
            channel = self.bot.get_channel(channel_id_logs)
            await channel.send(embed=disnake.Embed(title='Вызвана команда: "ping"', description=f"`ID Автора`: {ctx.author.id}\n`Ник Автора`: {ctx.author}\n`ID Сервера`: {ctx.guild.id}\n`Название Сервера`: {ctx.guild}")) #
        except Exception:
            pass
    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def information(self, ctx):
        await ctx.send(embed=embedinformation)
        try:
            channel = self.bot.get_channel(channel_id_logs)
            await channel.send(embed=disnake.Embed(title='Вызвана команда: "information"', description=f"`ID Автора`: {ctx.author.id}\n`Ник Автора`: {ctx.author}\n`ID Сервера`: {ctx.guild.id}\n`Название Сервера`: {ctx.guild}"))
        except Exception:
            pass
    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def help(self, ctx, arg=None):
        if arg == None:
            await ctx.send(embed=disnake.Embed(title=":book: | Меню выбора", description="\n`main` - Главные команды бота\n`other` - Другие команды бота\n\n**:link: [Пригласить меня](https://discord.com/api/oauth2/authorize?client_id=896108733275439165&permissions=518083968512&scope=bot%20applications.commands)**\n:link: **[Сервер сообщества бота](https://discord.gg/jntsZ2F3cQ)**", color=0xFFFF00))
        elif arg == "main":
            await ctx.send(embed=disnake.Embed(title="Главные команды", description="`stand_get` - Вонзить стрелу в себя\n`stand_info` - Информация о стенде\n`stand_list` - Информация о ваших стендах\n`stand_adventure` - Приключения для заработка", color=0xffff00))
        elif arg == "other":
            await ctx.send(embed=disnake.Embed(title="Другие команды", description="`ping` - Проверить отклик бота\n`stats` - Проверить статистику бота\n`information` - Информация о боте", color=0xFFFF00))
        try:
            channel = self.bot.get_channel(channel_id_logs)
            await channel.send(embed=disnake.Embed(title='Вызвана команда: "help"', description=f"`ID Автора`: {ctx.author.id}\n`Ник Автора`: {ctx.author}\n`ID Сервера`: {ctx.guild.id}\n`Название Сервера`: {ctx.guild}"))
        except Exception:
            pass
    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def stats(self, ctx):
        embedstats = disnake.Embed(title="Статистика бота", color=0xffff00)
        embedstats.add_field(name='Количество серверов:', value=f'{len(self.bot.guilds)}', inline=True)
        embedstats.add_field(name='Количество юзеров на серверах:', value=f'{len(self.bot.users)}', inline=False)   
        await ctx.send(embed=embedstats)
        try:
            channel = self.bot.get_channel(channel_id_logs)
            await channel.send(embed=disnake.Embed(title='Вызвана команда: "stats"', description=f"`ID Автора`: {ctx.author.id}\n`Ник Автора`: {ctx.author}\n`ID Сервера`: {ctx.guild.id}\n`Название Сервера`: {ctx.guild}"))
        except Exception:
            pass
# ---------------------------
def setup(bot):
    bot.add_cog(Utilits(bot))
    print("Получилось загрузить ког утилиты!")