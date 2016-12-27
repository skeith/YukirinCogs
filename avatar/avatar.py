import discord
from discord.ext import commands


class Avatar:
    """Get user's avatar URL."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def Avatar(self, ctx, user: discord.Member):
        """Get user's avatar URL.

        THAT SIMPLE!"""
        author = ctx.message.author
        avatar = user.avatar_url

        if not user:
            user = author
        await self.bot.say("{}'s Avatar URL : {}".format(user.name, avatar))


def setup(bot):
    bot.add_cog(Avatar(bot))
