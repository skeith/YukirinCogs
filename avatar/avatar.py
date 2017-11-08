import discord
from discord.ext import commands


class Avatar:
    """Get user's avatar URL."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def avatar(self, ctx, *, user: discord.Member=None):
        """Get user's avatar URL.

        THAT SIMPLE!"""
        author = ctx.message.author

        if not user:
            user = author

        avatar = user.avatar_url
        avatar = avatar.replace('webp', 'png')
        await self.bot.say("{}'s Avatar URL : {}".format(user.name, avatar))


def setup(bot):
    bot.add_cog(Avatar(bot))
