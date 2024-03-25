import disnake
from disnake.ext import commands

class Count(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def count(self, ctx):
        pass

    @count.sub_command(description="ban者数のカウントをします")
    async def ban(self, ctx):
        counter = 0
        async for ban in ctx.guild.bans(limit=None):
            if not ban.user.bot:
                counter += 1

        embed = disnake.Embed(
            title="BAN者数",
            description=f"{counter}人"
        )
        await ctx.send(embed=embed)