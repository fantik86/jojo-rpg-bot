import disnake
import time
import datetime
from disnake.ext import commands


class Events(commands.Cog):

    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'{ctx.author.mention},\nВремя сейчас: <t:{int(datetime.datetime.now().timestamp())}:T>\nПодождите до <t:{int(datetime.datetime.now().timestamp() + round(error.retry_after))}:T> перед использованием этой команды!')
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == f"<@!{896108733275439165}>":
            await message.channel.send(embed=disnake.Embed(title="Бонджорно!", description="Я тут, если что, вызывай меня через *$*.", color=0xFFFF00))
        
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        try:
            channel = self.bot.get_channel(903701604014891040)
            joinguild = self.bot.get_guild(self.guild.id)
            await channel.send(embed=disnake.Embed(title='Бот был приглашён на сервер', description=f"`ID Сервера`: {None}\n`Ник Автора`: {None}\n`Название Сервера`: {guild}"))
        except Exception as rrr:
            t = self.bot.get_channel(896109675873984543)
            await t.send(e)
        for chan in guild.text_channels:
            if chan.permissions_for(guild.me).send_messages:
                await chan.send(embed=disnake.Embed(title="Я Джорно Джованна, и у меня есть мечта!", description="Бон-джорно! Меня зовут Джорно Джованна, и у меня есть мечта.\nСпасибо что вы пригласили меня на сервер, я постараюсь представить себя во всей красе!\nЯ являюсь RPG ботом, где вы сможете получить свой стенд, развиваться и бороться с другими.\n\nКоманды - `$help`\nМой префикс - **$**", color=0xffff00))
                break
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        try:
            channel = self.bot.get_channel(903701604014891040)
            joinguild = self.bot.get_guild(self.guild.id)
            await channel.send(embed=disnake.Embed(title='Бот был удалён с сервера', description=f"`ID Сервера`: {None}\n`Ник Автора`: {None}\n`Количество юзеров`: {joinguild.member_count}\n`Название Сервера`: {guild}"))
        except Exception as rrrr:
            print("Send error:", rrrr)
        return
        # тут будет форма удаления из бд
    
    
    
def setup(bot):
    bot.add_cog(Events(bot))
    print("Получилось загрузить ког Ивентов!")
