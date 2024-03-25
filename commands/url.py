import disnake
from disnake.ext import commands
from httpx import AsyncClient

class Url(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="url関係のコマンドです")
    async def url(self, ctx):
        pass

    @url.sub_command(description="urlを短縮します")
    async def short(self, ctx, url: str):
        """
        Parameters
        ----------
        url: urlを入力して下さい
        """
        await ctx.send("Loading...")
        rurl = f"https://xgd.io/V1/shorten?url={url}&key=6cdeb7b6073585a6dbf32942e13f0133"
        async with AsyncClient() as client:
            response = await client.get(rurl)
            if response.status_code == 200:
                rj = response.json()
                embed = disnake.Embed(title="結果", description=f"{ctx.author.global_name}によるリクエスト")
                embed.add_field("短縮url", rj["shorturl"], inline=False)
                embed.add_field("オリジナルurl", rj["originalurl"], inline=False)
                await ctx.edit_original_response("", embed=embed)
            else:
                await ctx.edit_original_response("エラーが発生したようです。サポートが必要ですか？")