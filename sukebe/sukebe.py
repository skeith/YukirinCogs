import discord
from discord.ext import commands
import random


class Sukebe:
    """Paruru sensei can detect your Sukebe-ness."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def sukebe(self, ctx, user: discord.Member):
        """Detects user's Sukebe-ness.

        157% accurate!"""

        random.seed(int(user.id) % int(ctx.message.timestamp.timestamp()),)
        x = ":fire:" * random.randint(1, 10)
        await self.bot.say("{}'s Sukebe-ness is : ".format(user.name) + x)


def setup(bot):
    bot.add_cog(Sukebe(bot))
