import discord
from discord.ext import commands
from random import choice as rnd


version = "2018.3.0"
author = "Yukirin"

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


class PDA:
    """Public Display of Affection ~!"""

    def __init__(self, bot):
        self.bot = bot
        self.patimg = patlist
        self.version = version

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
            await self.bot.say(embed=patdata)

    @commands.command(name="pdaver", no_pm=True)
    async def _version_pda(self):
        """Show PDA version"""
        ver = self.version
        await self.bot.say("You are running on PDA version {}".format(ver))


def setup(bot):
    # check_folder()
    bot.add_cog(PDA(bot))
