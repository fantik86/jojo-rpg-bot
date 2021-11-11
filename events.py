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
def setup(bot):
    bot.add_cog(Events(bot))
    print("Получилось загрузить ког Ивентов!")