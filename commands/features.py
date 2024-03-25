import disnake
from disnake import PartialEmoji
from disnake.ext import commands

class Features(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="カテゴリーを指定してチャンネルの権限を同期します")
    @commands.has_permissions(manage_channels=True)
    async def sync_permissions(ctx, category: disnake.CategoryChannel):
        await ctx.send("同期開始")
        category_id = category.id
        category = ctx.guild.get_channel(category_id)
        
        for channel in category.channels:
            await channel.edit(sync_permissions=True)
        
        await ctx.send(f"{category.name}にあるチャンネルの権限を同期しました。")
    @sync_permissions.error
    async def ban_error(self, inter: disnake.ApplicationCommandInteraction, error):
        if isinstance(error, commands.MissingPermissions):
            await inter.response.send_message("あなたに権限がありません(ManageChannels)", ephemeral=True)
            return
        if isinstance(error, commands.BotMissingPermissions):
            await inter.response.send_message("botの権限が足りていません\n入れなおす又は管理者権限を付与してください", ephemeral=True)
            return

    @commands.slash_command(description="botを招待します")
    async def invite(self, ctx):
        embed = disnake.Embed(
            title="クリックで追加",
            url=r"https://discord.com/api/oauth2/authorize?client_id=1187674374162100275&permissions=277025482752&scope=bot+applications.commands"
        )
        await ctx.send(embed=embed)

    @commands.slash_command(description="サポートサーバーの表示")
    async def support(self, ctx):
        await ctx.send("サポートが必要ですか？今すぐ参加しよう\nhttps://discord.gg/StDrDnez9g")
        

    @commands.slash_command(description="クイック投票")
    async def poll(self, ctx, title:str, answers: str):
        """
        投票を開始します

        Parameters
        ----------
        title: 投票パネルのタイトル
        answers: 投票の答え。空白で区切ってください
        """
        args = answers.split()
        r = 0

        if not len(args) > 10:
            emoji = ["🇦","🇧","🇨","🇩","🇪","🇫","🇬","🇭","🇮","🇯"]

            message = ''
            for answer in args:
                message += f"{emoji[r]} {answer}\n"
                r += 1

            embed = disnake.Embed(
                title=title,
                description=message
            )

            await ctx.send(embed=embed)

            msg = await ctx.original_response()
            r = 0
            for _ in range(len(args)):
                await msg.add_reaction(PartialEmoji(name=emoji[r]))
                r += 1
        else:
            await ctx.send("答えは10個以下でお願いします。")