import disnake
from disnake.ext import commands

class MsgCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(ban_members=True)
    @commands.message_command(name="Ban&DelMsg")
    async def ban(self, inter: disnake.ApplicationCommandInteraction, message: disnake.Message):
        member = await inter.guild.fetch_member(message.author.id)

        if member:
            await inter.response.send_message("BAN処理を実行しています...", ephemeral=True)
            await member.ban(clean_history_duration=604800, reason=f"{inter.author.name}によってBANされました。")
            await inter.send("処理が完了しました（お確かめ下さい）", ephemeral=True)
        else:
            await inter.response.send_message("メンバーが見つかりませんでした。", ephemeral=True)
    @ban.error
    async def ban_error(self, inter: disnake.ApplicationCommandInteraction, error):
        if isinstance(error, commands.MissingPermissions):
            await inter.response.send_message("あなたに権限がありません(ban)", ephemeral=True)
            return
        if isinstance(error, commands.BotMissingPermissions):
            await inter.response.send_message("botの権限が足りていません\n入れなおす又は管理者権限を付与してください", ephemeral=True)
            return

    @commands.has_permissions(kick_members=True)
    @commands.message_command(name="Kick")
    async def kick(self, inter, message: disnake.Message):
        member = await inter.guild.fetch_member(message.author.id)
        if member:
            await inter.response.send_message("Kick処理を実行しています...", ephemeral=True)
            await member.kick(reason=f"{inter.author.name}によってKickされました。")
            await inter.send("処理が完了しました（お確かめ下さい）", ephemeral=True)
        else:
            await inter.response.send_message("メンバーが見つかりませんでした。", ephemeral=True)
    @kick.error
    async def ban_error(self, inter: disnake.ApplicationCommandInteraction, error):
        if isinstance(error, commands.MissingPermissions):
            await inter.response.send_message("あなたに権限がありません(kick)", ephemeral=True)
            return
        if isinstance(error, commands.BotMissingPermissions):
            await inter.response.send_message("botの権限が足りていません\n入れなおす又は管理者権限を付与してください", ephemeral=True)
            return