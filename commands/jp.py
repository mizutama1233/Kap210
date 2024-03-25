import aiohttp, json, disnake
from disnake.ext import commands

EastJPLocation = commands.option_enum({"札幌": "016010", "青森": "020010", "盛岡": "030010", "仙台": "040010", "秋田": "050010", "山形": "060010", "福島": "070010", "水戸": "080010", "宇都宮": "090010", "前橋": "100010", "さいたま": "110010", "千葉": "120010", "東京": "130010", "横浜": "140010", "新潟": "150010", "富山": "160010", "金沢": "170010", "福井": "180010", "甲府": "190010", "長野": "200010", "岐阜": "210010", "静岡": "220010", "名古屋": "230010", "津": "240010"})
WestJPLocation = commands.option_enum({ "大津": "250010", "京都": "260010", "大阪": "270000", "神戸": "280010", "奈良": "290010", "和歌山": "300010", "鳥取": "310010", "岡山": "330010", "広島": "340010", "山口": "350020", "徳島": "360010", "高松": "370000", "松山": "380010", "高知": "390010", "福岡": "400010", "佐賀": "410010", "長崎": "420010", "熊本": "430010", "大分": "440010", "宮崎": "450010", "鹿児島": "460010", "那覇": "471010"})

class JpFeature(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def jp(self, ctx):
        pass

    @jp.sub_command()
    async def east_weather(self, ctx, location: EastJPLocation):
        """
        東日本の各地域の天気を表示します

        Parameters
        ----------
        location: ~~市で選択して下さい
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://weather.tsukumijima.net/api/forecast/city/{location}") as response:
                if response.status == 200:
                    data = await response.text()
                    data = json.loads(data.replace('\u3000', ''))

                    embed = disnake.Embed(
                        title=data["title"],
                        description=data["description"]["text"]
                    )
                    embed.set_footer(text=data["publicTimeFormatted"])
                    embed.set_thumbnail(data['forecasts'][0]['image']['url'])

                    embed.add_field(data["forecasts"][0]['dateLabel'], value=f"{data['forecasts'][0]['detail']['weather']}, {data['forecasts'][0]['detail']['wind']}", inline=False)
                    embed.add_field(data["forecasts"][1]['dateLabel'], value=f"{data['forecasts'][1]['detail']['weather']}, {data['forecasts'][1]['detail']['wind']}", inline=False)

                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"Error: {response.status}")

    @jp.sub_command()
    async def west_weather(self, ctx, location: WestJPLocation):
        """
        西日本の各地域の天気を表示します

        Parameters
        ----------
        location: ~~市で選択して下さい
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://weather.tsukumijima.net/api/forecast/city/{location}") as response:
                if response.status == 200:
                    data = await response.text()
                    data = json.loads(data.replace('\u3000', ''))

                    embed = disnake.Embed(
                        title=data["title"],
                        description=data["description"]["text"]
                    )
                    embed.set_footer(text=data["publicTimeFormatted"])
                    embed.set_thumbnail(data['forecasts'][0]['image']['url'])

                    embed.add_field(data["forecasts"][0]['dateLabel'], value=f"{data['forecasts'][0]['detail']['weather']}, {data['forecasts'][0]['detail']['wind']}", inline=False)
                    embed.add_field(data["forecasts"][1]['dateLabel'], value=f"{data['forecasts'][1]['detail']['weather']}, {data['forecasts'][1]['detail']['wind']}", inline=False)

                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"Error: {response.status}")