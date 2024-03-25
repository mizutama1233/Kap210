import disnake
from disnake.ext import commands

class Discord(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(description="discord関連のコマンドです")
	async def discord(self, ctx):
		pass

	@discord.sub_command()
	async def find_id(self, ctx, id:str):
		"""
		DiscordのユーザーIDからユーザーを検索します

		Parameters
		----------
		id: Enter the user id
		"""
		try:
			user = await self.bot.fetch_user(int(id))

			em = disnake.Embed(
				title="取得結果"
			)
			em.set_author(
				name=user,
				icon_url=user.avatar
			)
			em.set_thumbnail(url=user.avatar)
			em.set_image(url=user.banner)

			em.add_field(name="UserName", value=user.name, inline=True)
			em.add_field(name="GlobalName", value=user.global_name, inline=True)
			em.add_field(name="Id", value=user.id, inline=True)
			em.add_field(name="Flags", value=user.public_flags, inline=True)
			em.add_field(name="Is bot?", value=user.bot, inline=True)

			await ctx.send(embed=em)
		except:
			await ctx.send("取得に失敗。（存在しないか、その他のエラーです）")

	@discord.sub_command()
	async def find_invite(self, ctx, invite:str):
		"""
		Discordの招待リンクからユーザーを検索します

		Parameters
		----------
		invite: サーバーの招待URL
		"""
		try:
			invite = await self.bot.fetch_invite(invite)
			guild = invite.guild

			em = disnake.Embed(
				title="取得結果",
			)
			em.set_author(
				name=guild.name,
				icon_url=guild.icon
			)
			em.set_thumbnail(url=guild.icon)
			em.set_image(url=guild.banner)

			em.add_field(name="Id", value=guild.id, inline=True)
			em.add_field(name="Nsfw_level", value=guild.nsfw_level, inline=True)
			em.add_field(name="Features", value=', '.join(guild.features), inline=False)
			em.add_field(name="Vanity", value=guild.vanity_url_code, inline=True)
			em.add_field(name="Verification", value=guild.verification_level, inline=False)

			await ctx.send(embed=em)
		except:
			await ctx.send("取得に失敗。（存在しないか、その他のエラーです）")
