import discord
from discord.ext import commands

class Features(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    @commands.has_permissions(administrator=True)
    async def create_offer(self, ctx, member: discord.Member):
        category = ctx.guild.get_channel(1182907397283516612)
        channel = await category.create_text_channel(f"{member.global_name}")

        await channel.set_permissions(member, view_channel=True, send_messages=True, send_messages_in_threads=True, create_public_threads=True)
        await ctx.send("Offer created!")
    @create_offer.error
    async def create_offer_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("あなたに必要な権限がありません！")

async def setup(bot):
    await bot.add_cog(Features(bot))