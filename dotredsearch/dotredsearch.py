from discord.ext import commands


class Dotred:
    """Search cogs.red. A really simple cog."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["find"], pass_context=True)
    async def dotred(self, ctx, *, keyword):
        """Search cogs.red
        I don't know why I made this"""

        await self.bot.say("http://cogs.red/cogs?search={}".format(keyword))


def setup(bot):
    bot.add_cog(Dotred(bot))
