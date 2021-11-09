import disnake
from disnake.ext import commands


class Events(commands.Cog):

    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'{ctx.author.mention} Подождите {round(error.retry_after)} секунд перед использованием команды!')
def setup(bot):
    bot.add_cog(Events(bot))
    print("Получилось загрузить ког Ивентов!")