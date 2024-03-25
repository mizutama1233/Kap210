from disnake.ext import commands
import google.generativeai as genai
# from g4f.client import Client

# client = Client()
genai.configure(api_key="AIzaSyBxhx-5K9DZ2yE0maubJpOmhX39PIRBD3A")
gemini_pro_model = genai.GenerativeModel('gemini-pro')

class AI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="AI関連のコマンドです")
    async def ai(self, ctx):
        pass

    # @ai.sub_command(description="GPT3に質問します(このコマンドでは会話はできません)")
    # async def gpt3(self, ctx, prompt: str):
    #     """
    #     Parameters
    #     ----------
    #     prompt: 質問を入力してください！
    #     """
    #     await ctx.send("Loading GPT3...")
    #     response = client.chat.completions.create(
    #         model = "gpt-3.5-turbo",
    #         messages = [{"role": "user", "content": prompt}],
    #     )
    #     await ctx.edit_original_response(response.choices[0].message.content)

    # @ai.sub_command(description="GPT4に質問します(このコマンドでは会話はできません)")
    # async def gpt4(self, ctx, prompt: str):
    #     """
    #     Parameters
    #     ----------
    #     prompt: 質問を入力してください！
    #     """
    #     await ctx.send("Loading GPT4... (URLが多く表示される場合があります)")
    #     response = client.chat.completions.create(
    #         model = "gpt-4",
    #         messages = [{"role": "user", "content": prompt}],
    #     )
    #     await ctx.edit_original_response(response.choices[0].message.content)

    @ai.sub_command(description="Geminiに質問します（このコマンドでは会話できません）")
    async def gemini(self, ctx, prompt: str):
        """
        Parameters
        ----------
        prompt: 質問を入力してください！
        """
        await ctx.send("Loading Gemini...")
        
        response = gemini_pro_model.generate_content(prompt).text
        await ctx.edit_original_response(response)