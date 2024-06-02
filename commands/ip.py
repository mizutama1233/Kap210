import ipinfo, disnake, json, re
from bs4 import BeautifulSoup
from disnake.ext import commands
from httpx import AsyncClient

handler = ipinfo.getHandlerAsync('')

class Ip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def ip(self, inter):
        pass

    @ip.sub_command(description="IPアドレスの危険度を確認します")
    async def risk(self, ctx, ip:str):
        """
        Parameters
        ----------
        ip: IPアドレスを入力してください。(例: 1.2.3.4)
        """
        if not re.search("^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})$", ip):
            await ctx.send("IPアドレスではないようです。")
            return
        await ctx.send("Loading...")
        async with AsyncClient() as client:
            response = await client.get("https://scamalytics.com/ip/" + ip)
            if response.status_code == 200:
                page = BeautifulSoup(response.text, "lxml")
                risk = json.loads(page.find('pre').text)

                embed = disnake.Embed(title=f"{ip}の危険度")
                embed.add_field("Score", risk["score"], inline=False)
                embed.add_field("Risk", risk["risk"], inline=False)
                embed.set_footer(text=f"{ctx.author.name}によってリクエストされました")

                await ctx.edit_original_response("", embed=embed)
            else:
                await ctx.edit_original_response("エラーが発生したようです。サポートが必要ですか？")

    @ip.sub_command(description="IPアドレスの詳細を取得します。")
    async def info(self, ctx, ip:str):
        """
        Parameters
        ----------
        ip: IPアドレスを入力してください。(例: 1.2.3.4)
        """
        if not re.search("^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})$", ip):
            await ctx.send("IPアドレスではないようです。")
            return
        details = await handler.getDetails(ip)
        d_all = details.all

        embed = disnake.Embed(title=f"{ip}の結果")
        embed.set_footer(text=f"{ctx.author.name}によってリクエストされました")
        embed.set_thumbnail(url=d_all["country_flag_url"])

        embed.add_field('city', d_all["city"], inline=False)
        embed.add_field('hostname', d_all["hostname"], inline=True)
        embed.add_field('anycast', d_all["anycast"], inline=True)
        embed.add_field('region', d_all["region"], inline=False)
        embed.add_field('country', d_all["country"], inline=True)
        embed.add_field('location', d_all["loc"], inline=True)
        embed.add_field('origin', d_all["org"], inline=False)
        embed.add_field('postal', d_all["postal"], inline=True)
        embed.add_field('timezone', d_all["timezone"], inline=True)
        embed.add_field('country_name', d_all["country_name"], inline=True)
        await ctx.send(embed=embed)
