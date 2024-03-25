import disnake
from disnake.ext import commands
from googletrans import Translator

TL = Translator()

class Translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="翻訳など")
    async def translate(self, ctx):
        pass

    @translate.sub_command()
    async def detect(self, ctx, text: str):
        """
        入力したテキストの言語を検出します

        Parameters
        ----------
        text: 検出する元のテキスト
        """
        embed = disnake.Embed(
            title="検出結果",
            description=f"Text:\n{text}"
        )
        embed.add_field(name="言語", value=TL.detect(text).lang)

        await ctx.send(embed=embed)

    @translate.sub_command()
    async def run(self, ctx, text: str, lang: str):
        """
        入力したテキストを翻訳します

        Parameters
        ----------
        text: 翻訳する元のテキスト
        lang: 翻訳先の言語（例: en）
        """
        ed_text = TL.translate(text, dest=lang)

        embed = disnake.Embed(
            title="Translated",
            description=text
        )
        embed.add_field(name=f"{ed_text.src} to {ed_text.dest}", value=ed_text.text)

        await ctx.send(embed=embed)