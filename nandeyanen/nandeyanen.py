import discord
from discord.ext import commands
from discord.ext.commands import errors, converter
from random import randint, choice as rnd
import os
import aiohttp
import asyncio
from PIL import Image
try:
    from robohash import Robohash as Rh
    Robo = True
except ImportError:
    Robo = False


version = "2.7.0"
author = "Yukirin"
PATH = 'data/nande/'

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

comments = [
    "You are not too ugly, aren't you?",
    "Oh GOD, why do I have to draw you?",
    "This is the last time I will draw someone!",
    "Finishing..."
]

caturl = "http://random.cat/meow"
foxurl = "http://wohlsoft.ru/images/foxybot/randomfox.php"
dogurl = "https://dog.ceo/api/breeds/image/random"
qturl = "http://inspirobot.me/api?generate=true"


class Nandeyanen:
    """Nandeyanen ~!"""

    def __init__(self, bot):
        self.bot = bot
        self.fmoji = defmoji
        self.patimg = patlist
        self.caturl = caturl
        self.foxurl = foxurl
        self.dogurl = dogurl
        self.qturl = qturl
        self.version = version

    async def attach(self, msg, folder):
        if msg:
            await self.bot.say(msg)
        folderPath = "data/nandeyanen/" + folder
        fileList = os.listdir(folderPath)
        gifPath = folderPath + "/" + fileList[randint(0, len(fileList) - 1)]
        await self.bot.upload(gifPath)

    @commands.group(name="nande", pass_context=True,
                    invoke_without_command=True, no_pm=True)
    async def nande(self, ctx):
        """Nandeyanen utility command"""
        await self.bot.send_cmd_help(ctx)

    @nande.command(name="version", no_pm=True)
    async def _version_nandeyanen(self):
        """Show Nandeyanen version"""
        ver = self.version
        await self.bot.say("You are running on Nandeyanen version {}".format(ver))

    @commands.command(pass_context=True)
    # async def f(self, ctx, *, user: discord.Member=None):
    async def f(self, ctx, *, user):
        """Pay respects.

        THAT SIMPLE!"""
        author = ctx.message.author
        if user is not None:
            try:
                member = converter.MemberConverter(ctx, user).convert()
                await self.bot.say("{} has paid their respect for {} {}".format(author.name, member.mention, rnd(self.fmoji)))

            except errors.BadArgument:
                await self.bot.say("{} has paid their respect for {} {}".format(author.name, user, rnd(self.fmoji)))
        else:
            await self.bot.send_cmd_help(ctx)

        # if not user:
            # await self.bot.say("{} has paid their respect {}".format(author.name, rnd(self.fmoji)))
        # else:
            # await self.bot.say("{} has paid their respect for {} {}".format(author.name, user.name, rnd(self.fmoji)))

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
    async def kitty(self):
        """The cure of boredom."""
        try:
            async with aiohttp.get(self.caturl) as r:
                result = await r.json()
            cat = discord.Embed(description="\u2063", color=discord.Color(0xffb6c1))
            cat.set_image(url=result['file'])
            # await self.bot.say(result['file'])
            await self.bot.say(embed=cat)
        except:
            await self.bot.say("Couldn't Get An Image")

    @commands.command()
    @commands.cooldown(6, 60, commands.BucketType.user)
    async def fox(self):
        """Another cure of boredom."""
        try:
            async with aiohttp.get(self.foxurl) as r:
                result = await r.json()
            fox = discord.Embed(description="\u2063", color=discord.Color(0xffb6c1))
            fox.set_image(url=result['file'])
            # await self.bot.say(result['file'])
            await self.bot.say(embed=fox)
        except:
            await self.bot.say("Couldn't Get An Image")

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
            await self.bot.say("Couldn't Get An Image")

    @commands.command()
    @commands.cooldown(6, 60, commands.BucketType.user)
    async def rquote(self):
        """To make human pointless existence worth."""
        try:
            async with aiohttp.get(self.qturl) as r:
                result = await r.text()
            qt = discord.Embed(description="\u2063", color=discord.Color(0xffb6c1))
            qt.set_image(url=result)
            await self.bot.say(embed=qt)
        except:
            await self.bot.say("Couldn't Get An Image")

    @commands.command(pass_context=True)
    @commands.cooldown(2, 60, commands.BucketType.channel)
    async def drawme(self, ctx, *, set):
        """Generate a drawing of yourself.
           140% accurately drawn

           Acceptable set options/arguments : any, set1, set2, set3, set4"""
        channel = ctx.message.channel
        hash = ctx.message.author.id
        drawed = PATH + "generated-" + hash + ".png"
        sets = ['any', 'set1', 'set2', 'set3', 'set4']
        if not Robo:
            await self.bot.say("Robohash is not installed. Install it using `pip3 install robohash`")
        else:
            pass
        if set not in sets:
            await self.bot.say("Incorrect options!\nAcceptable options are : any, set1, set2, set3, or set4")
        else:
            x = Rh(hash)
            x.assemble(roboset=set)
            with open(PATH + "generated-" + hash + ".png", "wb") as f:
                x.img.save(f, format="png")
            a = await self.bot.say("Drawing...")
            await asyncio.sleep(2)
            b = await self.bot.say(rnd(comments))
            await self.bot.delete_message(a)
            await asyncio.sleep(1)
            await self.bot.delete_message(b)
            await asyncio.sleep(1)
            await self.bot.send_file(channel, drawed)


def check_folder():
    if not os.path.exists(PATH):
        print("Creating data/nande folder...")
        os.makedirs(PATH)


def setup(bot):
    check_folder()
    bot.add_cog(Nandeyanen(bot))
