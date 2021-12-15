import disnake
from disnake.ext import commands
# -----------------------------
class Starterss(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Ник и тэг = {self.bot.user}")
        print(f"Мой айди = {self.bot.user.id}")
# -------------------------------
def setup(bot):
    bot.add_cog(Starterss(bot))
    print("Получилось загрузить старт!")
