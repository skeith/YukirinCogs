import discord
from discord.ext import commands
from discord.ext.commands import errors, converter
from random import choice as rnd
import aiohttp


version = "2018.3.30"
author = "Yukirin"
PATH = 'data/nande/'

tkgifs = [
    "https://i.imgur.com/Gr52Duc.gif",
    "https://i.imgur.com/gCaOw21.gif",
    "https://i.imgur.com/o70X4ko.gif",
    "https://i.imgur.com/hvpCH9L.gif",
    "https://i.imgur.com/aLuU57Z.gif",
    "https://i.imgur.com/yKOCo9k.gif",
    "https://i.imgur.com/hLuJOL4.gif",
    "https://i.imgur.com/OhSZJ0w.gif",
    "https://i.imgur.com/f2wCZHb.gif",
    "https://i.imgur.com/TRPTcmh.gif",
    "https://i.imgur.com/mJqJOYa.gif",
    "https://i.imgur.com/Gfb3sUE.gif",
    "https://i.imgur.com/Sh7dQWK.gif",
    "https://i.imgur.com/wKnflYa.gif",
    "https://i.imgur.com/J40nBu2.gif"
]


class Nandeyanen:
    """Nandeyanen ~!"""

    def __init__(self, bot):
        self.bot = bot
        self.tkgifs = tkgifs
        self.version = version
        self.session = aiohttp.ClientSession()

    def __unload(self):
        self.session.close()

    @commands.command(name="nandever", no_pm=True)
    async def _version_nandeyanen(self):
        """Show Nandeyanen version"""
        ver = self.version
        await self.bot.say("You are running on Nandeyanen version {}".format(ver))

    @commands.command(pass_context=True)
    async def thaikick(self, ctx, *, user):
        """Attempt to thai kick a user"""

        author = ctx.message.author
        if user is not None:
            try:
                member = converter.MemberConverter(ctx, user).convert()
                tk = discord.Embed(description="DUN DUN ~ ! {}, THAI KICK ~ !".format(member.mention), color=discord.Color(0xffb6c1))
                tk.set_image(url=rnd(self.tkgifs))
                await self.bot.say(embed=tk)

            except errors.BadArgument:
                await self.bot.say("{} tried to thai kick something inexistent. Shame!".format(author.mention))
        else:
            await self.bot.send_cmd_help(ctx)


def setup(bot):
    bot.add_cog(Nandeyanen(bot))
