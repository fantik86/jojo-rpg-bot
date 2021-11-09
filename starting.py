import disnake
from disnake.ext import commands
# -----------------------------
class Starterss(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('------')
        print('Произошло логирование в:')
        print(f"Ник и тэг = {self.bot.user}")
        print(f"Мой айди = {self.bot.user.id}")
        print('------')
        await self.bot.change_presence(status=disnake.Status.online, activity=disnake.Game("60%"))
# -------------------------------
def setup(bot):
    bot.add_cog(Starterss(bot))
    print("Получилось загрузить старт!")