import discord
from discord.ext import commands
from random import choice as rnd
import os
import aiohttp

defmoji = [
    ":heart:",
    ":yellow_heart:",
    ":green_heart:",
    ":blue_heart:",
    ":purple_heart:"]

patlist = [
    "https://i.imgur.com/YTGnx49.gif",
    "https://i.imgur.com/U37wHs9.gif",
    "https://i.imgur.com/BU2IQym.gif",
    "https://i.imgur.com/yp6kqPI.gif",
    "https://i.imgur.com/uDyehIe.gif",
    "https://i.imgur.com/vG8Vuqp.gif",
    "https://i.imgur.com/z4uCLUt.gif",
    "https://i.imgur.com/ZIRC9f0.gif",
    "https://i.imgur.com/s8m4srp.gif",
    "https://i.imgur.com/LKvNxmo.gif",
    "https://i.imgur.com/j4W4GFt.gif",
    "https://i.imgur.com/75bX4A1.gif",
    "https://i.imgur.com/dSlfpe3.gif",
    "https://i.imgur.com/JjxaT8e.gif",
    "https://i.imgur.com/QWBlOaQ.gif",
    "https://i.imgur.com/5448px6.gif",
    "https://i.imgur.com/4WJRAGw.gif",
    "https://i.imgur.com/v1sSh5r.gif"
]

caturl = "http://random.cat/meow"
foxurl = "http://wohlsoft.ru/images/foxybot/randomfox.php"
dogurl = "https://dog.ceo/api/breeds/image/random"

class Nandeyanen:
    """Nandeyanen ~!"""

    def __init__(self, bot):
        self.bot = bot
        self.fmoji = defmoji
        self.patimg = patlist
        self.caturl = caturl
        self.foxurl = foxurl
        self.dogurl = dogurl

    async def attach(self, msg, folder):
        if msg:
            await self.bot.say(msg)
        folderPath = "data/nandeyanen/" + folder
        fileList = os.listdir(folderPath)
        gifPath = folderPath + "/" + fileList[randint(0, len(fileList) - 1)]
        await self.bot.upload(gifPath)

    @commands.command(pass_context=True)
    async def f(self, ctx, *, user: discord.Member=None):
        """Pay respects.

        THAT SIMPLE!"""
        author = ctx.message.author

        if not user:
            await self.bot.say("{} has paid their respect {}".format(author.name, rnd(self.fmoji)))
        else:
            await self.bot.say("{} has paid their respect for {} {}".format(author.name, user.name, rnd(self.fmoji)))

    @commands.command(pass_context=True)
    @commands.cooldown(6, 60, commands.BucketType.user)
    async def pat(self, ctx, *, user: discord.Member=None):
        """Pat users."""
        author = ctx.message.author

        if not user:
            await self.bot.say("{} is trying to pat the air ... and failed.".format(author.name))
        else:
            patdata = discord.Embed(description="**{}** got a pat from **{}**".format(user.name, author.name), color=discord.Color(0xffb6c1))
            patdata.set_image(url=rnd(self.patimg))
            # this line is for testing purpose
            # patdata.set_image(url="https://i.imgur.com/YTGnx49.gif")
            await self.bot.say(embed=patdata)

    @commands.command()
    @commands.cooldown(6, 60, commands.BucketType.user)
    async def cats(self):
        """The cure of boredom"""
        try:
            async with aiohttp.get(self.caturl) as r:
                result = await r.json()
            cat = discord.Embed(description="\u2063", color=discord.Color(0xffb6c1))
            cat.set_image(url=result['file'])
            # await self.bot.say(result['file'])
            await self.bot.say(embed=cat)
        except:
            await self.bot.say("Couldnt Get An Image")

    @commands.command()
    @commands.cooldown(6, 60, commands.BucketType.user)
    async def fox(self):
        """Another cure of boredom"""
        try:
            async with aiohttp.get(self.foxurl) as r:
                result = await r.json()
            fox = discord.Embed(description="\u2063", color=discord.Color(0xffb6c1))
            fox.set_image(url=result['file'])
            # await self.bot.say(result['file'])
            await self.bot.say(embed=fox)
        except:
            await self.bot.say("Couldnt Get An Image")

    @commands.command()
    @commands.cooldown(6, 60, commands.BucketType.user)
    async def doggo(self):
        """Wait! There is more cure of boredom?"""
        try:
            async with aiohttp.get(self.dogurl) as r:
                result = await r.json()
            dog = discord.Embed(description="\u2063", color=discord.Color(0xffb6c1))
            dog.set_image(url=result['message'])
            # await self.bot.say(result['file'])
            await self.bot.say(embed=dog)
        except:
            await self.bot.say("Couldnt Get An Image")

def setup(bot):
    bot.add_cog(Nandeyanen(bot))
