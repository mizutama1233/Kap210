import disnake
from disnake.ext import commands

class UserCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.user_command(name="Avatar")
    async def avatar(self, inter: disnake.ApplicationCommandInteraction, user: disnake.User):
        e = disnake.Embed()
        e.set_image(url=f"{user.avatar.url}")
        await inter.response.send_message(embed=e)