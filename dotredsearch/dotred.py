from discord.ext import commands


class DotRed:
    """Serach cogs.red. A really simple cog."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(alias="find", pass_context=True)
    async def dotred(self, ctx, *, keyword):
        """Search cogs.red
        I don't know why I make this"""

        await self.bot.say("http://cogs.red/cogs?search={}".format(keyword))


def setup(bot):
    bot.add_cog(DotRed(bot))
