import disnake, subprocess
cmd = "python3 haihubot/main.py"
subprocess.call(cmd.split())

from disnake.ext import commands
from commands import discord, minigame, jp, translate, features, ai, msgCmd, userCmd, count, url, ip

csf = commands.CommandSyncFlags.default()
csf.sync_commands_debug = True

bot = commands.Bot(command_prefix=";", command_sync_flags=csf, activity=disnake.Game(name='多機能BOT'))

@bot.event
async def on_ready():
    print("Kap210 is online!")
    for guild in bot.guilds:
        print(guild.name)

bot.add_cog(discord.Discord(bot))
bot.add_cog(count.Count(bot))
bot.add_cog(minigame.Games(bot))
bot.add_cog(jp.JpFeature(bot))
bot.add_cog(translate.Translate(bot))
bot.add_cog(features.Features(bot))
bot.add_cog(ai.AI(bot))
bot.add_cog(msgCmd.MsgCmd(bot))
bot.add_cog(userCmd.UserCmd(bot))
bot.add_cog(url.Url(bot))
bot.add_cog(ip.Ip(bot))

@bot.slash_command(guild_ids=[1182907395450613851])
@commands.has_permissions(administrator=True)
async def create_offer(ctx, member: disnake.Member):
    category = ctx.guild.get_channel(1182907397283516612)
    channel = await category.create_text_channel(f"{member.global_name}")

    await channel.set_permissions(member, view_channel=True, send_messages=True, send_messages_in_threads=True, create_public_threads=True)
    await ctx.send("Offer created!")
@create_offer.error
async def create_offer_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("あなたに必要な権限がありません！")

bot.run("MTE4NzY3NDM3NDE2MjEwMDI3NQ.GIM9Aj.uPoUM5o-QE0LbOjBxaNg2slGA2JfFsq7ee-17A")