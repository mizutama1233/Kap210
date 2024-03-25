import disnake, random
from disnake.ext import commands

hands = ["ぐー", "ちょき", "ぱー"]
openHands = {
    "ぐー": ":punch:",
    "ちょき": ":v:",
    "ぱー": ":hand_splayed:",
}

dice = {
    1: ":one:",
    2: ":two:",
    3: ":three:",
    4: ":four:",
    5: ":five:",
    6: ":six:",
}

class JankenView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=10)

    @disnake.ui.string_select(
        placeholder="手を選ぼう",
        options=[
            disnake.SelectOption(label="ぐー"),
            disnake.SelectOption(label="ちょき"),
            disnake.SelectOption(label="ぱー"),
        ],
        min_values=1,
        max_values=1,
    )
    async def animal_callback(
        self, select: disnake.ui.StringSelect, ctx
    ):
        await ctx.send(f"Bot: {openHands[random.choice(hands)]}\n{ctx.author.global_name}: {openHands[select.values[0]]}")

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="じゃんけんをプレイします")
    async def janken(self, ctx):
        view = JankenView()
        await ctx.send("じゃんけん...", view=view)
        

    @commands.slash_command(description="サイコロを振ります")
    async def dice(self, ctx):
        await ctx.send(dice.get(random.randint(1, 6)))