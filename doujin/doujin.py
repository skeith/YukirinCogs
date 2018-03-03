import discord
from discord.ext import commands
from __main__ import send_cmd_help


class Doujin:
    """Doujin commands."""

    def __init__(self, bot):
        self.bot = bot
	self.session = self.bot.http.session

    @commands.group(pass_context=True)
    async def doujin(self, ctx):
        """Doujin commands"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @doujin.command(no_pm=True)
    async def nhentai(self):
        """Sends a random doujin"""
        url = "http://nhentai.net/random/"
        async with self.session.get(url) as r:
            await self.bot.say(r.url)
			
    @doujin.command(no_pm=True)
    async def tsumino(self):
        """Sends a random doujin"""
        url = "http://www.tsumino.com/Browse/Random"
        async with self.session.get(url) as r:
            await self.bot.say(r.url)
			
    @doujin.command(no_pm=True)
    async def hbrowse(self):
        """Sends a random doujin"""
        url = "http://www.hbrowse.com/random"
        async with self.session.get(url) as r:
            await self.bot.say(r.url)

def setup(bot):
    bot.add_cog(Doujin(bot))
