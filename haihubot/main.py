# token MTIyMDM1NzY5ODc3Njk4OTcxNg.GbqsWA.ERiZcA9rdJRjRtHq3CFnTYLFLeVrtEWt3YApLk

import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    await bot.load_extension('features')
    await bot.tree.sync()
    print('Bot is ready!')

@bot.hybrid_command()
async def reload(ctx):
    if ctx.author.id == 1182851005675749479 or ctx.author.id == 1182851005675749479:
        await bot.reload_extension('features')
        await ctx.send("リロードしました")
    else:
        await ctx.send("あなたは実行できません")

bot.run("MTIyMDM1NzY5ODc3Njk4OTcxNg.GbqsWA.ERiZcA9rdJRjRtHq3CFnTYLFLeVrtEWt3YApLk")