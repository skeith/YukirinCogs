import discord
from discord.ext import commands
import random


class Sukebe:
    """Paruru sensei can detect your Sukebe-ness."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sukebe(self, user: discord.Member):
        """Detects user's Sukebe-ness.

        157% accurate!"""

        random.seed(user.id,)
        x = ":fire:" * random.randint(0, 10)
        await self.bot.say("Sukebe-ness: " + x)


def setup(bot):
    bot.add_cog(Sukebe(bot))
